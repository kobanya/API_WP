import requests
import pandas as pd

# A WordPress weboldal REST API végpontja
api_url = "https://kozlekedes.org/wp-json/mo/v1/IRSZ"
response = requests.get(api_url)
data = response.json()
df = pd.DataFrame(data)
print(df)


# 1. Olvassuk ki a "countymegye" kulcsokat és távolítsuk el a duplikációkat
countymegye_set = set(item["countymegye"] for item in data)

# 2. Kérjünk be egy vármegye számát a felhasználótól
print("Válassz egy vármegyét a következő számok közül:")
for i, megye in enumerate(countymegye_set, start=1):  # Start értékkel kezdünk számolni
    print(f"{i}. {megye}")

try:
    selected_index = int(input("Válassz egy számot: "))
    selected_megye = list(countymegye_set)[selected_index - 1]

    selected_data = [item for item in data if item["countymegye"] == selected_megye]

    print(f"\n{selected_megye} vármegye települései és irányítószámaik:")
    for item in selected_data:
        print(f"{item['placenametelepls']}: {item['postalcodeirnytszm']}")
except (ValueError, IndexError):
    print("Hibás választás vagy érvénytelen szám.")
