import pandas as pd
import utils
import etl


def main():

    # Extract the data from the files
    df_all_video_advertisers = etl.extract("./sources/all_video_advertisers.csv", "csv", 6)
    df_rubicon = etl.extract("./sources/Rubicon.json", "json")

    # work with rubicon files.
    df_rubicon = utils.filter_df(df_rubicon, 'Ad Format', 'Video')
    df_rubicon = df_rubicon.rename(columns={"Date Ad": "Date", "Referring Domain": "Domain", "Publisher Net Revenue":
                                   "Revenue"})
    df_rubicon.insert(1, 'Advertiser Name', 'Rubicon')
    df_rubicon = df_rubicon.drop(columns=['Ad Format'])
    df_rubicon['Date'] = [i.to_pydatetime().strftime('%d/%m/%Y') for i in df_rubicon['Date']]

    # Merge both dataframes and keep the most accurate data if is possible
    df_result = etl.merge_df(df_all_video_advertisers, df_rubicon, 'outer', ['Date', 'Advertiser Name', 'Domain'])

    # clean the url column according to business rules.
    df_result = utils.clean_url(df_result, 'Domain')

    # create the result
    df_aggregated_result = df_result.groupby(["Date", "Advertiser Name", "Domain"])['Revenue'].sum().reset_index()
    df_aggregated_result.to_csv('./output/advertiser_revenue.csv', index=False)


if __name__ == '__main__':
    print('Starting ETL')
    main()
    print('finish ETL')
