import pandas as pd
import utils
import etl


def main():
    # df_all_video_advertisers = pd.read_csv("./sources/all_video_advertisers.csv", skiprows=6)
    df_all_video_advertisers = etl.extract("./sources/all_video_advertisers.csv", "csv", 6)
    df_rubicon = etl.extract("./sources/Rubicon.json", "json")

    df_rubicon = df_rubicon.loc[df_rubicon['Ad Format'] == 'Video']
    df_rubicon = df_rubicon.rename(columns={"Date Ad": "Date", "Referring Domain": "Domain", "Publisher Net Revenue": "Revenue"})
    df_rubicon.insert(1, 'Advertiser Name', 'Rubicon')
    df_rubicon = df_rubicon.drop(columns=['Ad Format'])
    df_rubicon = utils.clean_url(df_rubicon)

    df_all_video_advertisers = utils.clean_url(df_all_video_advertisers)

    df_rubicon['Date'] = [i.to_pydatetime().strftime('%d/%m/%Y') for i in df_rubicon['Date']]
    df_result = df_all_video_advertisers.merge(df_rubicon, how='outer', on=['Date', 'Advertiser Name', 'Domain'],
                                               suffixes=('_left', '_right'))

    for index, value in enumerate(df_result['Revenue_right']):
        if pd.isna(value):
            df_result['Revenue_right'][index] = df_result['Revenue_left'][index]

    df_result = df_result.drop(columns=['Revenue_left'])
    df_result = df_result.rename(columns={'Revenue_right': 'Revenue'})

    df_aggregated = df_result.groupby(["Date", "Advertiser Name", "Domain"])['Revenue'].sum().reset_index()

    df_aggregated.to_csv('./output/advertiser_revenue.csv', index=False)


if __name__ == '__main__':
    print('Starting ETL')
    main()
    print('finish ETL')