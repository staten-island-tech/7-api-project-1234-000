import tkinter
from tkinter import messagebox
import requests


def getPoke(poke):
    respond = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if respond.status_code != 200:
        print("None")
        return None
    data = respond.json()
    return {
        "name": data["name"],
        "weight": data["weight"],
        "height": data["height"],
        "types":[t["type"]["name"]for t in data["types"]]
    }
    
