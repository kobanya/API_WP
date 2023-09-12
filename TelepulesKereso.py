import requests
import pandas as pd

# A WordPress weboldal REST API 1 végpontja
api_url = "https://kozlekedes.org/wp-json/mo/v1/IRSZ"
iranyitoszam = requests.get(api_url)
data = iranyitoszam.json()
df_isz = pd.DataFrame(data)

api_url = "https://kozlekedes.org/wp-json/mo/v1/TELEPULES"
telepules = requests.get(api_url)
data = telepules.json()
df_telepules = pd.DataFrame(data)


