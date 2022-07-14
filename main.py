import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Starting the ETL')

    df_all_video_advertisiers = pd.read_csv(
        "/Users/martin.rosenzweig/Downloads/Apester_Home_Assignment_Data_engineer/all_video_advertisers.csv",
    skiprows=6)

    # df_all_video_advertisiers.groupby("Date", "Advertiser Name", "Domain").Revenue.sum()

    print(df_all_video_advertisiers.to_string())
    print(df_all_video_advertisiers.groupby(["Date", "Advertiser Name", "Domain"]).Revenue.sum())

    # df_rubicon = pd.read_json("/Users/martin.rosenzweig/Downloads/Apester_Home_Assignment_Data_engineer/Rubicon.json")


    # print(df_rubicon.to_string())