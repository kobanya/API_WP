import requests

# A WordPress weboldal REST API 1 végpontja a településekhez
telepules_api_url = "https://kozlekedes.org/wp-json/mo/v1/TELEPULES"

# Inputként kérj be egy település nevet
keresett_telepules = input("Kérem, adja meg a keresett település nevét: ")

# Kérjük le az összes település adatát a TELEPULES API-ból
telepules_data = requests.get(telepules_api_url).json()

# Keresd meg a bekért települést a "nev" kulcs alapján
talalatok = [telepules for telepules in telepules_data if telepules.get("nev") == keresett_telepules]

# Ellenőrizzük, hogy van-e találat
if talalatok:
    talalt_telepules = talalatok[0]
    print("Talált település adatai:")
    print(f"Név: {talalt_telepules.get('nev')}")
    print(f"Jogállás: {talalt_telepules.get('joglls')}")
    print(f"Járás: {talalt_telepules.get('jrs')}")
    print(f"Járás székhelye: {talalt_telepules.get('jrsszkhelye')}")
    print(f"Vármegye: {talalt_telepules.get('varmegye')}")
    print(f"Lakossága: {talalt_telepules.get('lakos')} fő")

else:
    print(f"Nincs találat a(z) '{keresett_telepules}' településre.")
