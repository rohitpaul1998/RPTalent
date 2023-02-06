import json
import requests
# from connection import cursor
from bs4 import BeautifulSoup
import pandas as pd

#below headers dictionary is used as a way of spoofing when making API calls to let the server know we are not trying to hack their website
HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US, en;q=0.9",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Cache-Control":"max-age=0, no-cache, no-store",
    "Upgrade-Insecure-Requests":"1"
}

final_data = []

#looping over the pages
for i in range(2,30,1):
    page = requests.get(f"https://www.yellowpages.com/los-angeles-ca/restaurants?page={i}", headers=HEADERS)
    page_content = page.content
    soup = BeautifulSoup(page.content, 'html.parser')

    restaurant_containers = soup.find_all('div', {'class': 'info'})
    for container in restaurant_containers:
        data = {}
        restaurant_name = container.find('a', {'class': 'business-name', 'href': True})
        if restaurant_name:
            span = restaurant_name.find('span')
            if span:
                data["Restaurant_Name"] = span.text

        restaurant_rating = container.find('div', class_='ratings')
        if restaurant_rating:
            if 'data-tripadvisor' in restaurant_rating.attrs:
                rating = json.loads(restaurant_rating['data-tripadvisor'])
                data["TripAdvisor_Rating"] = rating['rating']
                data["TripAdvisor_Rating_Count"] = rating['count']

            cnt = restaurant_rating.find('span')
            if cnt:
                data["Review_Count"] = cnt.text

            if 'data-foursquare' in restaurant_rating.attrs:
                data["Foursquare_Rating"] = json.loads(restaurant_rating['data-foursquare'])

        phone = container.find('div', class_='phones phone primary')
        if phone:
            data["Restaurant_Number"] = phone.text

        address = container.find('div', class_='adr')
        if address:
            street_address = address.find('div', class_='street-address')
            if street_address:
                data["Restaurant_Address"] = street_address.text

            locality = address.find('div', class_='locality')
            if locality:
                data["Restaurant_Locality"] = locality.text

        final_data.append(data)

# print(final_data)

# using pandas dataframe to store my json data

df = pd.DataFrame(final_data)

# df.to_csv("top_restaurants_data2.csv", index=False)


























#
# final_data = [] #where we will store our restaurant data
#
#
# #looping over the pages
# for i in range(1,6,1):
#     # print(f"page {i}")
#     page = requests.get(f"https://www.yellowpages.com/los-angeles-ca/restaurants?page={i}", headers=HEADERS)
#     page_content = page.content
#     soup = BeautifulSoup(page.content, 'html.parser')
#
#     restaurant_name = soup.find_all('a', {'class':'business-name','href':True})
#     for j in restaurant_name:
#         span = j.find('span')
#         if span:
#             final_data.append({"Restaurant_Name": span.text})
#
#
#
#     restaurant_rating = soup.findAll('div', class_='ratings')
#     for k in restaurant_rating:
#         if 'data-tripadvisor' in k.attrs:
#             data = k['data-tripadvisor']
#             rating = json.loads(data)['rating']
#             counts = json.loads(data)['count']
#             final_data.append({"TripAdvisor_Rating":rating})
#             final_data.append({"TripAdvisor_Rating_Count": counts})
#
#     restaurant_rating_count = soup.findAll('div', class_='ratings')
#     for l in restaurant_rating_count:
#         cnt = l.find('span')
#         if cnt:
#             final_data.append({"Review_Count":cnt.text})
#
#     restaurant_foursquare = soup.findAll('div', class_='ratings')
#     for m in restaurant_foursquare:
#         if 'data-foursquare' in m.attrs:
#             dat = m['data-foursquare']
#             foursqr = json.loads(dat)
#             final_data.append({"Foursquare_Rating":foursqr})
#
#     restaurant_phone = soup.findAll('div', class_='info')
#     for n in restaurant_phone:
#         num = n.find('div', class_='phones phone primary')
#         if num:
#             final_data.append({"Restaurant_Number": num.text})
#
#     restaurant_address = soup.findAll('div', class_='adr')
#     for o in restaurant_address:
#         addr = o.find('div', class_='street-address')
#         if addr:
#             final_data.append({"Restaurant_Address": addr.text})
#
#     restaurant_locality = soup.findAll('div', class_='adr')
#     for p in restaurant_locality:
#         loca = p.find('div', class_='locality')
#         if loca:
#             lac = loca.text
#             final_data.append({"Restaurant_Locality": loca.text})
#
#
#
#
# # using pandas dataframe to store my json data
#
# df = pd.DataFrame(final_data)
# # df.to_csv("top_restaurants_data.csv", index=False)
# print(df)
#
