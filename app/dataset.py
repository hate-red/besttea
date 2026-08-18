import kagglehub
import pandas as pd

from config import project_root


path = kagglehub.dataset_download(
    handle="ursmaheshj/top-10000-popular-movies-tmdb-05-2023",
    output_dir=project_root / 'dataset' # type: ignore
)

df = pd.read_csv(path / 'top_1000_popular_movies_tmdb.csv', engine='python') # type: ignore

df_cleaned = df.dropna()

df_cleaned.to_csv(project_root / 'dataset' / 'top_movies_tmdb_cleaned.csv')
