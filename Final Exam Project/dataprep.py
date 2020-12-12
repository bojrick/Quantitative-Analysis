
import pandas as pd

if __name__ == '__main__':
    data_link = 'https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r00/access/csv/ibtracs.ALL.list.v04r00.csv'
    hurrican_data = pd.read_csv(data_link)
    print('Hurrican Data Loaded..!!')
    hurrican_data['ISO_TIME'] = pd.to_datetime(hurrican_data['ISO_TIME'],errors='coerce')
    selected_cols = ['SID','SEASON','NUMBER','BASIN',
                     'ISO_TIME','NATURE','LAT','LON',
                     'WMO_WIND','USA_WIND','USA_SSHS','USA_STATUS',
                     'TOKYO_WIND','TOKYO_GRADE','CMA_CAT',
                     'CMA_WIND','HKO_CAT','HKO_WIND',
                     'NEWDELHI_GRADE','NEWDELHI_WIND',
                     'REUNION_TYPE','REUNION_WIND',
                     'BOM_TYPE','BOM_WIND',
                     'NADI_CAT','NADI_WIND',
                     'WELLINGTON_WIND','DS824_WIND',
                     'NEUMANN_WIND','MLC_WIND','STORM_SPEED','STORM_DIR']

    filtered = hurrican_data[hurrican_data['ISO_TIME'].dt.year>1969][selected_cols]
    filtered['DATE'] = filtered['ISO_TIME'].dt.date
    print('Hurrican data clenaed..!!')
    oil_prices = pd.read_csv('wtiDaily1970.csv',names=['DATE','PRICE'],skiprows=1)
    oil_prices['DATE'] = pd.to_datetime(oil_prices['DATE'],format='%Y%m%d').dt.date
    oil_prices.merge(filtered,on='DATE',how='left').to_csv('merged_data.csv')
    print('combined data saved as merged_data.csv..!!')

