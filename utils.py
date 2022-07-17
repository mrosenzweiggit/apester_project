import re


def clean_url(df, column_name):
    """
    This function clean the URL string
    :param column_name: name of the column to be cleaned
    :param df: pandas dataframe
    :return: pandas dataframe
    """
    df[column_name] = [re.sub('/.*', '', i.replace('www.', '').replace('https://', '').replace('http://', '')) for i in
                       df[column_name]]

    return df


def filter_df(df, column_name, strfilter):
    """
    This function filter the pandas dataframe
    :param df: pandas dataframe
    :param column_name: column name to be filtered
    :param strfilter: filter condition
    :return: pandas dataframe
    """
    df = df.loc[df[column_name] == strfilter]

    return df
