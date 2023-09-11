import requests
import pandas as pd

# A WordPress weboldal REST API végpontja
api_url = "https://kozlekedes.org/wp-json/mo/v1/IRSZ"

try:
    response = requests.get(api_url)

    # Ellenőrizze a válasz státuszkódját
    if response.status_code == 200:
        # Az API válasza JSON formátumban érkezik
        data = response.json()

        # Most rendezzük a DataFrame-be
        df = pd.DataFrame(data)

        # Kiírhatjuk a DataFrame-et a táblázatban
        print(df)

    else:
        print(f"Hiba történt a kérés során. Státuszkód: {response.status_code}")
except Exception as e:
    print(f"Hiba történt a kérés során: {str(e)}")
