import requests



def getFruit(fruit):
    url = requests.get(f"https://fruityvice.com/api/fruit/{fruit.lower()}")
    if url.status_code != 200:
        print("Error fetching data!")
        return None
    data  = url.json()
    return {
        "name": data["name"],
        "family": data["family"],
        "genus": data["genus"],
        "nutritions": data["nutritions"]
    }


teat = getFruit("Orange")
print(teat["name"])

