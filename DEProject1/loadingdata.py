import csv
from connection import conn
from datacleaning import df7

# LOADING RESTAURANTS DATA TO POSTGRES DB INSTANCE
# cursor = conn.cursor()
# csv_data = csv.reader(open('Restaurant Table.csv'))
# header = next(csv_data)
#
# print("Importing file to postgres.....")
#
# for row in csv_data:
#     print(row)
#     cursor.execute("INSERT INTO Restaurants(Restaurant_ID, Restaurant_Name, Restaurant_Number, Restaurant_Address, City, State, ZipCode) VALUES(%s, %s, %s, %s, %s, %s, %s)", row)
#
# conn.commit()
# conn.close()



# LOADING TRIPADVISOR RATINGS DATA TO POSTGRES DB INSTANCE

# cursor1 = conn.cursor()
# csv_data1 = csv.reader(open('Tripadvisor Ratings Table.csv'))
# header1 = next(csv_data1)
#
# print("Importing file to postgres.....")
#
# for row1 in csv_data1:
#     print(row1)
#     cursor1.execute("INSERT INTO Tripadvisor_Ratings(Tripadvisor_ID, TripAdvisor_Rating, TripAdvisor_Rating_Count, Restaurant_ID) VALUES(%s, %s, %s, %s)", row1)
#
# conn.commit()
# conn.close()



# LOADING FOURSQUARE RATINGS DATA TO POSTGRES DB INSTANCE

cursor2 = conn.cursor()
csv_data2 = csv.reader(open('Foursquare Rating table.csv'))
header2 = next(csv_data2)

print("Importing file to postgres.....")

for row2 in csv_data2:
    print(row2)
    cursor2.execute("INSERT INTO Foursquare_Ratings(Foursquare_ID, Foursquare_Rating, Restaurant_ID) VALUES(%s, %s, %s)", row2)

conn.commit()
conn.close()
