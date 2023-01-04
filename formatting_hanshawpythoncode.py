########################################
import pandas as pd
import numpy as np

### read in initial files - UPDATE THESE
hail_file = "Maiana.Cases.xlsx"
null_file = "HVT3Null.Maiana.xlsx"
user_id = "MNH"

hail_df = pd.read_excel(hail_file)
null_df = pd.read_excel(null_file)

## add "NULL" to EVENT TYPE from NULL file so that they don't show up as NANs
null_df['event_type'] = null_df.event_type.fillna("NULL")

## merge dataframes
df = pd.concat([hail_df, null_df], axis=0, ignore_index=True)

del(hail_file)
del(null_file)
del(hail_df)
del(null_df)

## rename columns
df.rename(columns={'Unnamed: 0':'new_id'}, inplace=True)
df.rename(columns={'magnitude_value':'size'}, inplace=True)
df.rename(columns={'magnitude_units':'units'}, inplace=True)

## create unique ids for each row incorporting user_id
df['new_id'] = range(1, 1+len(df))
df['id'] = user_id + df['new_id'].astype(str)

## get new date/time stamp
# get new hh mm ss from adjusted_time column
df['hh'] = df['adjusted_time'].str[:2]
df['mm'] = df['adjusted_time'].str[2:4]
df['ss'] = df['adjusted_time'].str[5:7]

# get the null point times also
df['hh'] = np.where(df['hh'].isnull(), df['timestamp_utc'].dt.hour, df['hh']).astype(str)
df['mm'] = np.where(df['mm'].isnull(), df['timestamp_utc'].dt.minute, df['mm']).astype(str)
df['ss'] = np.where(df['ss'].isnull(), df['timestamp_utc'].dt.second, df['ss']).astype(str)
# ensure each value is 2 digits, eg. 03 instead of just 3
df['hh']=df['hh'].apply(lambda x: '{0:0>2}'.format(x))
df['mm']=df['mm'].apply(lambda x: '{0:0>2}'.format(x))
df['ss']=df['ss'].apply(lambda x: '{0:0>2}'.format(x))

df['adj_time'] = df['hh'] + ':' + df['mm'] + ':' + df['ss']

## extract yyyy mm dd from original timestamp_utc
df['orig_date'] = pd.to_datetime(df['timestamp_utc']).dt.date

## search in notes for #dayforward and #daybackwards to adjust
df['notes'] = df.notes.fillna("#none")
df['adj_date'] = df['orig_date']

df['adj_date'] = np.where(df['notes'].str.contains('dayback'), df['orig_date'] - pd.Timedelta(days=1), df['adj_date'])
df['adj_date'] = np.where(df['notes'].str.contains('dayfor'), df['orig_date'] + pd.Timedelta(days=1), df['adj_date'])

df['adj_date_str'] = df['adj_date'].astype(str)
df['orig_date'] = pd.to_datetime(df['timestamp_utc']).dt.date

## get date into format wanted by matt
df['datetime'] = df['adj_date_str'] + 'T' + df['adj_time']

## delete obsolete columns
df.drop('new_id', axis=1, inplace=True)
df.drop('user_id', axis=1, inplace=True)
df.drop('hh', axis=1, inplace=True)
df.drop('mm', axis=1, inplace=True)
df.drop('ss', axis=1, inplace=True)
df.drop('timestamp_utc', axis=1, inplace=True)
df.drop('adj_time', axis=1, inplace=True)
df.drop('orig_date', axis=1, inplace=True)
df.drop('adj_date', axis=1, inplace=True)
df.drop('adj_date_str', axis=1, inplace=True)
df.drop('adjusted_time', axis=1, inplace=True)

## update latitudes and longitudes
df['lat'] = df['latitude']
df['lon'] = df['longitude']

df['lat'] = np.where(df['adjusted_lat'].notnull(), df['adjusted_lat'], df['lat'])
df['lon'] = np.where(df['adjusted_lon'].notnull(), df['adjusted_lon'], df['lon'])

## delete obsolete columns
df.drop('latitude', axis=1, inplace=True)
df.drop('longitude', axis=1, inplace=True)
df.drop('adjusted_lat', axis=1, inplace=True)
df.drop('adjusted_lon', axis=1, inplace=True)

## replace "," with "_"
df['analyst_comments'] = df['analyst_comments'].str.replace(',', '_')

## replace "\n" with "|"
df['analyst_comments'] = df['analyst_comments'].str.replace('\n', '|')

## save to csv
df.to_csv("maiana.csv")
########################################