import torch
import numpy as np
import pandas as pd

from dataset import EncoderDataset
from neural_net import Encoder

from config import (
    models_dir, 
    encoder_name, 

    dataset_dir, 
    dataset_cleaned_name,
    dataset_preprocessed_name, 
    dataset_with_embeddings_name, 
)


model = Encoder()
state_dict = torch.load(models_dir / encoder_name, weights_only=True)
model.encoder.load_state_dict(state_dict)

df_preprocessed = pd.read_pickle(dataset_dir / dataset_preprocessed_name)
dataset = EncoderDataset(df_preprocessed)

embeddings = []

model.eval()
with torch.no_grad():
    for x, _ in dataset:
        embedding = model(torch.tensor(x))
        embeddings.append(embedding.numpy())

df_cleaned = pd.read_pickle(dataset_dir / dataset_cleaned_name)
df_cleaned['embedding'] = pd.Series(embeddings, index=df_preprocessed.index)
df_cleaned.to_pickle(dataset_dir / dataset_with_embeddings_name)

print(df_cleaned.info())
