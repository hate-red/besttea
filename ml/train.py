import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from dataset import EncoderDataset
from neural_net import AutoEncoder

from config import (
    dataset_dir, 
    dataset_preprocessed_name, 
    models_dir, 
    encoder_name, 
    decoder_name, 
)


random_state = 42

np.random.seed(random_state)
torch.manual_seed(random_state)
torch.cuda.manual_seed(random_state)

df = pd.read_pickle(dataset_dir / dataset_preprocessed_name)
X_train, X_test = train_test_split(df, test_size=0.2, random_state=random_state)

train_dataset = EncoderDataset(X_train)
test_dataset = EncoderDataset(X_test)

batch_size = 4096

train_loader = DataLoader(
    dataset=train_dataset, 
    batch_size=batch_size, 
    shuffle=True,
    pin_memory=True,
)
test_loader = DataLoader(
    dataset=test_dataset, 
    batch_size=batch_size, 
    shuffle=False,
    pin_memory=True,
)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
train_epochs = 100
lr = 0.003

model = AutoEncoder().to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=lr)

train_losses = []
test_losses = []

for epoch in range(1, train_epochs + 1):
    train_loss = []

    model.train()
    for X, y in train_loader:
        X, y = X.to(device), y.to(device)
        
        y_pred = model(X)

        loss = criterion(y_pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        train_loss.append(loss.item())


    test_loss = []

    model.eval()
    for X, y in test_loader:
        X, y = X.to(device), y.to(device)

        y_pred = model(X)

        loss = criterion(y_pred, y)
        test_loss.append(loss.item())

    mean_train_loss = np.mean(train_loss)
    mean_test_loss = np.mean(test_loss)
    
    train_losses.append(mean_train_loss)
    test_losses.append(mean_test_loss)

    print(
        f'Epoch [{epoch}/{train_epochs}]\t'
        f'Train Loss: {mean_train_loss:.4f}\t'
        f'Test Loss: {mean_test_loss:.4f}'
    )

torch.save(model.encoder.state_dict(), models_dir / encoder_name)
torch.save(model.decoder.state_dict(), models_dir / decoder_name)
