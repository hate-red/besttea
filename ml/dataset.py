from torch.utils.data import Dataset
import pandas as pd
import numpy as np


class EncoderDataset(Dataset):
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.numeric_df = self.df.select_dtypes(include=['int', 'float'])
        self.array_df = self.df.select_dtypes(include='object')

        numetic_data = self.numeric_df.to_numpy()
        array_data = np.array([
            *self.array_df.apply(lambda x: np.concatenate(x.to_numpy()), axis=1)
        ])

        self.data = np.concatenate((numetic_data, array_data), axis=1, dtype=np.float32)

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx) -> tuple[np.ndarray, np.ndarray]:
        return self.data[idx], self.data[idx]
