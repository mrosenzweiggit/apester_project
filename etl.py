import pandas as pd


def extract(source, file_type, skip_rows=0):
    """
    This function connect to source and extract the data
    :param source: filepath of the source
    :param file_type: csv, json, other
    :param skip_rows: number of rows to skip
    :return: pandas dataframe
    """
    df = pd.DataFrame()

    if file_type == 'csv':
        df = pd.read_csv(source, skiprows=skip_rows, infer_datetime_format=True)
    elif file_type == 'json':
        df = pd.read_json(source)
    else:
        print("[INFO] No data source founded")

    # pd.to_datetime(df, format="%d-%m-%y")
    return df


def merge_df(df_l, df_r, how, on):
    """
    This function merge 2 dataframes and keep the most accurate data
    :param on:
    :param df_l: left pandas dataframe
    :param df_r: right pandas dataframe
    :param how: type of merge (inner, left, right, outer, cross)
    :return:
    """
    df_result = df_l.merge(df_r, how=how, on=on, suffixes=('_left', '_right'))
    pd.set_option('mode.chained_assignment', None)
    for index, value in enumerate(df_result['Revenue_right']):
        if pd.isna(value):
            df_result['Revenue_right'][index] = df_result['Revenue_left'][index]

    df_result = df_result.drop(columns=['Revenue_left'])
    df_result = df_result.rename(columns={'Revenue_right': 'Revenue'})

    return df_result
