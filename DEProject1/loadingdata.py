import csv
from connection import conn
from datacleaning import df7

cursor = conn.cursor()
csv_data = csv.reader(open('DF7.csv'))
header = next(csv_data)

print("Importing file to postgres.....")

for row in csv_data:
    print(row)
    cursor.execute("INSERT INTO RestaurantData(Sl_No, Restaurant_Name, Restaurant_Number, Restaurant_Address, City, State, ZipCode, TripAdvisor_Rating, TripAdvisor_Rating_Count, Foursquare_Rating) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)

conn.commit()
conn.close()
