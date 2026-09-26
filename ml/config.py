from pathlib import Path


dataset_dir = Path(__file__).parent / 'dataset'

# raw dataset
dataset_name = 'films.csv'

# dataset without duplicates and NA values 
# but not suitable for model training
dataset_cleaned_name = 'films_cleaned.pickle'

# dataset with text values encoded, categorical values encoded,
# and numerical values normalized
dataset_preprocessed_name = 'films_preprocessed.pickle'
