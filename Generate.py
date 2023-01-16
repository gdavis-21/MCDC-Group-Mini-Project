import numpy as np
import pandas as pd
import random
import time

from bs4 import BeautifulSoup
import requests, lxml

# df = pd.read_csv("MCDC-Data.csv")

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
#     df.to_pickle("./MCDC-Data.pkl")

df = pd.read_pickle("./MCDC-Data.pkl")
print(df.head(100))
