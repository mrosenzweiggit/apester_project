import pandas as pd
import utils
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def main():
    df_all_video_advertisers = pd.read_csv("./sources/all_video_advertisers.csv", skiprows=6)

    df_rubicon = pd.read_json("./sources/Rubicon.json")
    df_rubicon = df_rubicon.loc[df_rubicon['Ad Format'] == 'Video']
    df_rubicon = df_rubicon.rename(columns={"Date Ad": "Date", "Referring Domain": "Domain", "Publisher Net Revenue": "Revenue"})
    df_rubicon.insert(1, 'Advertiser Name', 'Rubicon')
    df_rubicon = df_rubicon.drop(columns=['Ad Format'])
    df_rubicon = utils.clean_url(df_rubicon)
    df_all_video_advertisers = utils.clean_url(df_all_video_advertisers)

    df_rubicon['Date'] = [i.to_pydatetime().strftime('%d/%m/%Y') for i in df_rubicon['Date']]
    df_result = df_all_video_advertisers.merge(df_rubicon, how='outer', on=['Date','Advertiser Name','Domain'],
          suffixes=('_left', '_right'))

    for index, value in enumerate(df_result['Revenue_right']):
        if pd.isna(value):
            df_result['Revenue_right'][index] = df_result['Revenue_left'][index]

    df_result = df_result.drop(columns=['Revenue_left'])
    df_result = df_result.rename(columns={'Revenue_right': 'Revenue'})

    df_aggregated = df_result.groupby(["Date", "Advertiser Name", "Domain"])['Revenue'].sum().reset_index()

    df_aggregated.to_csv('./output/advertiser_revenue.csv', index=False)


    # print(df_rubicon['Date'][0])

    # print(df_all_video_advertisers.head())
    # print(set(df_all_video_advertisers['Advertiser Name']))
    # print(df_rubicon.head())
    # print(df_all_video_advertisers.groupby(["Date", "Advertiser Name", "Domain"]).Revenue.sum())


    print('finish ETL')



if __name__ == '__main__':
    print_hi('Starting ETL')
    main()
