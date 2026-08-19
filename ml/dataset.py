import kagglehub

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import ast

from pathlib import Path


matplotlib.use('qtagg')

dataset_dir = Path(__file__).parent / 'dataset'

if not dataset_dir.iterdir():
    _ = kagglehub.dataset_download(
        handle="ursmaheshj/top-10000-popular-movies-tmdb-05-2023",
        output_dir=dataset_dir # type: ignore
    )

df = pd.read_csv(dataset_dir / 'top_1000_popular_movies_tmdb.csv', engine='python') # type: ignore
df = df.dropna().drop(['Unnamed: 0'], axis=1).set_index('id')

df.to_csv(dataset_dir / 'top_movies_tmdb_cleaned.csv')
