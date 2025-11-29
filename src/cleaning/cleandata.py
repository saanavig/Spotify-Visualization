import os
import pandas as pd

def load_raw_data(filename="SpotifyFeatures.csv"):
    script_dir = os.path.dirname(__file__)
    data_path = os.path.join(script_dir, "../../data", filename)

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"CSV file not found at {data_path}")

    df = pd.read_csv(data_path)
    return df

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

def remove_duplicates(df):
    before = df.shape[0]
    df = df.drop_duplicates(subset=["track_name", "artist_name"], keep="first")
    after = df.shape[0]
    print(f"Removed {before - after} duplicates.")
    return df


def handle_missing(df):
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    cat_cols = df.select_dtypes(include=["object"]).columns
    df[cat_cols] = df[cat_cols].fillna("Unknown")

    return df


def save_clean_data(df, filename="cleanDataset.csv"):
    script_dir = os.path.dirname(__file__)
    save_path = os.path.join(script_dir, "../../data", filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    df.to_csv(save_path, index=False)
    print(f"Clean dataset saved to {save_path}!")

def clean_spotify_dataset():
    df = load_raw_data()
    df = clean_column_names(df)
    df = remove_duplicates(df)
    df = handle_missing(df)
    save_clean_data(df)

if __name__ == "__main__":
    clean_spotify_dataset()
