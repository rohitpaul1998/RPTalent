from scraper1 import df
import numpy as np


#space to clean my data

# df['Restaurant_Name'] = df['Restaurant_Name'].str.replace('!','',regex=True)
# df['Restaurant_Name'] = df['Restaurant_Name'].str.replace('|','',regex=True)
# print(df.head(24))
# df['Restaurant_Name'] = df['Restaurant_Name'].str.replace('@','',regex=True)
# df['Restaurant_Name'] = df['Restaurant_Name'].str.replace('è','e',regex=True)
# df['Review_Count'] = df['Review_Count'].str.replace('-','')
df1 = df.drop(columns=['Review_Count'])
df2 = df1.reindex(columns=['Restaurant_Name','Restaurant_Number','Restaurant_Address','Restaurant_Locality','TripAdvisor_Rating','TripAdvisor_Rating_Count','Foursquare_Rating'])
df2.fillna(value='NA', inplace=True)

#assigning new dataframe
df3 = df2

#splitting restaurant_locality into two new columns
df3[['Locality', 'ZipCode']] = df3['Restaurant_Locality'].str.rsplit(', ', 1, expand=True)

#dropping the restaurant_locality column
df4 = df3.drop(columns=['Restaurant_Locality']) #dropping unwanted Restaurant_Locality column

#assigning new dataframe df5 that has columns in order
df5 = df4.reindex(columns=['Restaurant_Name','Restaurant_Number','Restaurant_Address','Locality','ZipCode','TripAdvisor_Rating','TripAdvisor_Rating_Count','Foursquare_Rating'])


#i am separating CA and putting them into a new column called state
df5['State'] = df5['ZipCode'].str.extract(r'(CA)').astype(str)



#extracting only the numeric value out of zipcode column
df5['ZipCode'] = df5['ZipCode'].str.extract(r'(\d+)').astype(int)

#rearranging columns
df6 = df5.reindex(columns=['Restaurant_Name','Restaurant_Number','Restaurant_Address','Locality','State','ZipCode','TripAdvisor_Rating','TripAdvisor_Rating_Count','Foursquare_Rating'])


#renaming locality to city
df6 = df6.rename(columns={'Locality':'City'})
# df6.to_csv('DF6UPDATED.csv',index=False)

#adding a new column serial number for each restaurant
df6['Sl_No'] = range(1, len(df6) + 1)

# df6.to_csv('DF6UPDATED111111111111.csv',index=False)

#rearrangin columns
df7 = df6.reindex(columns=['Sl_No','Restaurant_Name','Restaurant_Number','Restaurant_Address','City','State','ZipCode','TripAdvisor_Rating','TripAdvisor_Rating_Count','Foursquare_Rating'])

# df7.to_csv('DF7.csv',index=False)

# print(df7)