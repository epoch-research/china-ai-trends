import pandas as pd


def load_pcd_df():
    return pd.read_csv('data/All ML Systems - full view.csv')


def load_hardware_df():
    return pd.read_csv('data/Chip dataset-Grid view.csv')


def load_price_df():
    return pd.read_csv('data/Hardware prices.csv')
