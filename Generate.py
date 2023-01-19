import numpy as np
import pandas as pd
import random
import time

from bs4 import BeautifulSoup
import requests, lxml

# df = pd.read_csv("./Combined-Data.csv")

# try:

#     userAgents = [
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
#        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9"
#         "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12D508 Safari/600",
#     ]

#     for i in range(len(df["School"]) - 1):
#         randomUserAgent = random.choice(userAgents)
#         headers = {
#             "User-Agent": randomUserAgent
#         }
#         time.sleep(random.random())

#         request = requests.get("https://www.google.com/search?q=" + df["School"][i] + "School Alabama" + "&hl=en", headers=headers)
        
#         if (request.status_code == 429):
#             df.to_pickle("./MCDC-Data.pkl")

#         soup = BeautifulSoup(request.text, "lxml")
#         address = soup.find_all("span", class_="BNeawe tAd8D AP7Wnd")
        
#         if (address != [] and address != None):
#             tokenizedAddress = address[0].get_text().split(",")
#             print(i, tokenizedAddress)
#             # Some school addresses don't list the road (e.g. Forest Avenue Elementary School)
#             if (len(tokenizedAddress) == 1 or len(tokenizedAddress) == 2):
#                 df.loc[i, ["Town"]] = [tokenizedAddress[0].strip()]
#             else:
#                 df.loc[i, ["Town"]] = [tokenizedAddress[1].strip()]
#         else:
#             print(None)
#             # No address on Google can be found.
#             df.loc[i, ["Town"]] = [None]


# except Exception as e:
#     print(e)
#     df.to_pickle("./Combined-Data.pkl")

df1 = pd.read_pickle("./Combined-Data.pkl")
df2 = pd.read_csv("./Population.csv")
cities = []

for i in range(len(df2["NAME"]) - 1):

    element = df2.loc[i, ["NAME"]].to_string().split(" ")
    try:
        element.remove("NAME")
    except:
        pass
    try:
        element.remove("(pt.)")
    except:
        pass
    try:
        element.remove("city")
    except:
        pass
    try:
        element.remove("town")
    except:
        pass
    cities.append(" ".join(element).strip())
# print(cities)

# For city in combined data, 
# print(df1["Town"])

for i in range(len(df1["Town"]) - 1):
    try:
        index = cities.index(df1["Town"][i])
        # df1["Town"][i] = df2["POPESTIMATE2021"][index]
        df1.loc[i, "Population"] = df2["POPESTIMATE2021"][index]
    except Exception as e:
        print(e,df1["Town"][i])

# print(df1.head(100))
df1.to_csv("~/Desktop/out.csv")

# Check to see if it is in the cities array.

# If it is, use that index to pull the population from df2 and put it in df1 at the current index

