import urllib.request

import json

def get_waste_sorting_points():

    url = "https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=..."
    try:

        with urllib.request.urlopen(url) as response:

            if response.status != 200:

                print("Kļūda: Serveris neatbild vai ir pieejams ar kļūdu kodu", response.status)

                return

           

            data = json.loads(response.read().decode())

            if not data.get("result") or not data["result"].get("records"):

                print("Kļūda: Saņemta tukša atbilde no servera.")

                return

           

            records = data["result"]["records"]

           

            for record in records:

                address = record.get("Adrese", "Nav norādīts")

                region = record.get("Novads", "Nav norādīts")

               

                battery = record.get("8 : Baterijas un akumulatori") == "x"

                tires = record.get("10 : Nolietotās riepas") == "x"

                metal = record.get("3 : Metāls") == "x"

               

                if battery or tires or metal:

                    print("--------------------------------")

                    print(f"Adrese: {address}")

                    print(f"Novads: {region}")

                    if battery:

                        print("✔ Pieņem baterijas un akumulatorus")

                    if tires:

                        print("✔ Pieņem nolietotās riepas")

                    if metal:

                        print("✔ Pieņem metālu")

   

    except urllib.error.URLError as e:

        print("Kļūda: Neizdevās piekļūt ārējam resursam.", e)

get_waste_sorting_points()