import requests
import tkinter as tk



def search():
    print("FINDING.....")

    asker = entry.get()

    rep  = requests.get(f"https://pokeapi.co/api/v2/pokemon/{asker}")
    data = rep.json()
    label.config(text=data["name"])
    weight_label.config(text=f"Weight: {data['weight']}")
    height_label.config(text=f"Height: {data['height']}")
    base_label.config(text=f"Base States: {data['base_experience']}")

    xp_label.config(text=f"Base XP: {data['base_experience']}")

    abilities_text = ""
    for i in data["abilities"]:
        abilities_text += i["ability"]["name"] + "\n"
    abilities_label.config(text=abilities_text)

    stats_text = ""
    for i in data["stats"]:
        stats_text += f"{i['stat']['name']}: {i['base_stat']}\n"
    stats_label.config(text=stats_text)

window = tk.Tk()
window.title("Pokedex Dictionary")
window.geometry("500x600")

label = tk.Label(window, text="Welcome to the Pokedex!", font=("Arial", 30))
label.pack()

abilities_label = tk.Label(window, text="")
abilities_label.pack()

xp_label = tk.Label(window, text="")
xp_label.pack()

stats_label = tk.Label(window, text="")
stats_label.pack()

weight_label = tk.Label(window, text="")
weight_label.pack()

height_label = tk.Label(window, text="")
height_label.pack()

base_label = tk.Label(window, text="")
base_label.pack()

entry = tk.Entry(window)
entry.pack()
btn = tk.Button(window, text="Search", command = search)
btn.pack()
window.mainloop()