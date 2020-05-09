import pandas as pd


def load_admissions():
    return pd.read_csv('../datasets/admissions.csv')


def load_mall_customers():
    return pd.read_csv('../datasets/mall_customers.csv')


def load_sat_gpa():
    return pd.read_csv('../datasets/sat_gpa.csv')


def load_social_network_ads():
    return pd.read_csv('../datasets/social_network_ads.csv')

