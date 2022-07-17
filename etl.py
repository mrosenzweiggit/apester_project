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
        df = pd.read_csv(source, skiprows=skip_rows)
    elif file_type == 'json':
        df = pd.read_json(source)
    else:
        print("[INFO] No se ha encontrado source")

    return df
