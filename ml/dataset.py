import kagglehub

import pandas as pd

from ml.config import (
    dataset_dir, 
    dataset_handle, 
    dataset_name, 
    dataest_cleaned_name,
)


if not dataset_dir.iterdir():
    _ = kagglehub.dataset_download(
        handle=dataset_handle,
        output_dir=dataset_dir # type: ignore
    )

df = pd.read_csv(dataset_dir / dataset_name, engine='python') # type: ignore
df = df.dropna().drop(['Unnamed: 0'], axis=1).set_index('id')

df.to_csv(dataset_dir / dataest_cleaned_name)
