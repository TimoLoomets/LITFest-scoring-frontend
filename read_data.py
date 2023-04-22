import pandas as pd
import urllib.request
import io
from collections import defaultdict

def read_from_web(SHEET_NAME = 'Folkrace'):
    SHEET_ID = '1msDLIZ1Z6N3q54tYqgO1w_dIS5ZW9dCk2JEGfrkWmBg'

    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    df = pd.read_csv(url, sep=",", dtype=str)

    index = [idx for idx, s in enumerate(list(df.columns)) if 'Unnamed' in s][0]
    results_df = df[df.columns[:index]]
    results_df = results_df[results_df[results_df.columns[0]].notna()]

    return results_df

if __name__ == "__main__":
    print(read_from_web())