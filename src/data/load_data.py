import joblib
import pandas as pd


def read_and_dump_pos_neg_texts(data_dir, dump_filename):
    pos_texts, neg_texts = [], []
    for file in data_dir.glob(f"pos/*txt"):
        with open(file, "r") as f:
            pos_texts.append(f.read())
    for file in data_dir.glob(f"neg/*txt"):
        with open(file, "r") as f:
            neg_texts.append(f.read())

    df = pd.DataFrame({"text": pos_texts + neg_texts, "label": 0})
    df.iloc[: len(pos_texts), 1] = 1
    joblib.dump(df, dump_filename)
    return df
