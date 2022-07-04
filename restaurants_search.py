#!/usr/bin/python

### File            : search.py
### Description     : Script accept an outcode as a parameter
###                   and showing information about each restaurant
###                   that delivers to that outcode (name, rating, types of food).
### Author          : Oleh Sharudin
### Version history :
### 20180111 1.0    : Script reday for use
###
### Needed libs     : requests, json
###
### Example of use  : run the script from cmd in format - python script.py

import requests
import json

url = "https://public.je-apis.com/restaurants" #API link
postCode = input("Please enter the outcode: ") #User input of postCode

#Checking user input
def checker():
    global postCode
    if len (postCode) == 0:
        postCode = input("Please enter the outcode: ")
        checker()
    else:
        print("Searching restaurants for the outcode -",postCode)
checker()

#Transfering headers
headers = {"Host":"public.je-apis.com", "Authorization":"*Basic Auth Token Here*", "Accept-Language":"en-GB", "Accept-Tenant":"uk"}
payload = {'q':postCode}

response = requests.get(url=url, headers=headers, params=payload)
status = response.status_code #Getting http status code

#Checking the connection
if status==200:
    print("A connection was successfully established with the server")
elif status !=200:
    print("Connection to the server cannot be established")

data = response.json() #Json output

#Writing the output to the json file (for debugging)
filepath = "restaurants.json"
with open(filepath, 'w') as outfile:
    json.dump(data, outfile)

#Looping through data in order to get Name, RatingStars, CuisineTypes
for value in data['Restaurants']:
    if 'Name' in value:
        name = value['Name']
        rating = value['RatingStars']
        cuisine = value['CuisineTypes']
        print("*************************************************")
        print("Name of the restaurant: %s\nRating: %s stars\nCuisineType: %s" %(name, rating, cuisine))
#EOF
