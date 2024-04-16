import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

months = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12]
years = [2016, 2017, 2018, 2019, 2020]

news_dtypes = {
    'year': pd.Int64Dtype(),
    'month': pd.Int64Dtype(),
    'day': pd.Int64Dtype(),
    'author': str,
    'title': str,
    'article': str,
    'url': str,
    'section': str,
    'publication': str
    }
parse_dates = ['date']


def dataframe_concatenation_year(url):
    df_csv = pd.DataFrame()
    for year in years:
        url_year = url + 'data_{}/news_data_{}_'.format(year, year)
        print('For year: {}'.format(year))
        df_csv_yearly = dataframe_concatenation_month(url_year, year)
        df_csv = pd.concat([df_csv, df_csv_yearly])
    return df_csv

def dataframe_concatenation_month(url, month):
    df_csv_monthly = pd.DataFrame()
    for month in months:
        url_month = url + '{:02d}.csv.gz'.format(month)
        print('For month:{} \nDownloading from:{}'.format(month, url_month))
        df_aux = pd.read_csv(url_month, sep=',', compression='gzip', dtype=news_dtypes, parse_dates=parse_dates)
        df_csv_monthly = pd.concat([df_csv_monthly, df_aux])
    return df_csv_monthly


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    base_url = 'https://github.com/Cerpint4xt/All_the_News_2_0_Component_One/releases/download/'
    
    df_csv = dataframe_concatenation_year(base_url)
    df_csv.drop(columns=['title', 'article'], inplace=True)
    
    return df_csv

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
