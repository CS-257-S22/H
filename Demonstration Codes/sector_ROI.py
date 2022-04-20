'''
DISCOUNTINUED FUNCTION DUE TO A CHANGE IN DATA
'''

def terminal_input_for_sector_ROI():
    # authors: Geoffrey, Jack

    # write your code here

    # call terminal_input_for_sector_ROI
    # build a prompt that pops up to


    return sector # dataformat: string

def sector_ROI(sector, prices_df, list_df):
    # authors: Nguyen, Miles

    # find all securities that are in the chossen sector
    codes_of_sector = list(list_df.loc[(list_df['GeneralSectorName'] == sector)].SecuritiesCode)

    # here are the earliest and latest dates that our data records
    earliest_date = datetime.datetime(2021, 12, 6)
    latest_date = datetime.datetime(2022, 2, 28)

    # temporary variable for future tally
    sector_value_earliest = 0
    sector_value_latest = 0

    # loop through all securities codes of the given sector, and tally up the sector's value
    for securities in codes_of_sector:

        if (securities in prices_df.SecuritiesCode.unique()) == True:

            first_value = prices_df.loc[(prices_df['Date'] == earliest_date) & (prices_df['SecuritiesCode'] == securities), "Open"]
            sector_value_earliest += float(first_value)

            last_value = prices_df.loc[(prices_df['Date'] == latest_date) & (prices_df['SecuritiesCode'] == securities), "Close"]
            sector_value_latest += float(last_value)

        else:
            pass

    # calculate ROI for the given sector
    # THIS VALUE IS IN PERCENTAGE
    ROI = (sector_value_latest - sector_value_earliest)/sector_value_earliest * 100

    return ROI