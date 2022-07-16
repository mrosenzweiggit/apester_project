import re


def clean_url(df):
    """
    This function clean the URL string
    :param df: pandas dataframe
    :return: pandas dataframe
    """
    df['Domain'] = [re.sub('/.*', '', i.replace('www.', '').replace('https://', '').replace('http://', '')) for i in
                    df['Domain']]

    return df
