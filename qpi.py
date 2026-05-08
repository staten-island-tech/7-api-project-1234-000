import requests
import tkinter as tk


def getFruit():
    text = entry.get()
    url = requests.get(f"https://fruityvice.com/api/fruit/{text}")
    if url.status_code != 200:
        error.config(text = "none try again")
        return
    error.config(text = "")
    data  = url.json()
    name_label.config(text = f"Name: {data["name"]}")
    family_label.config(text = f"Family: {data["family"]}")
    genus_label.config(text = f"Genus: {data["genus"]}")
    nutrition_label.config(text =  f"Calories: {data["nutritions"]["calories"]}")
    fat_label.config(text = f"Fat: {data["nutritions"]["fat"]}")
    proteinlabel.config(text = f"Protein: {data["nutritions"]["protein"]}")
    carbslabel.config(f"Carbs: {data["nutritions"]["carb"]}")

window = tk.Tk()
window.title("Diet")
window.geometry("1200x800")
window.resizable(False,False)

ask = tk.Label(window, text = "What Fruit Would You Like To Find About??", font = ("Arial", 50, "bold"), fg = "yellow")
ask.pack()

name_label = tk.Label(window, text = "", font = ("Arial", 25, "bold"))
name_label.pack()
family_label = tk.Label(window, text = "", font = ("Arial", 25, "bold"))
family_label.pack()
genus_label = tk.Label(window,text= "", font = ("Arial", 25, "bold"))
genus_label.pack()
nutrition_label = tk.Label(window, text = "", font = ("Arial", 25, "bold"))
nutrition_label.pack()

fat_label = tk.Label(window,text = "",font = ("Arial", 25, "bold"))
fat_label.pack()
proteinlabel = tk.Label(window, text = "", font = ("Arial", 25, "bold"))
proteinlabel.pack()
carbslabel = tk.Label(window, text = "", font = ("Arial", 25, "bold"))
carbslabel.pack()

error = tk.Label(window, text = "",font = ("Arial",50,"bold"))
error.pack()
entry = tk.Entry(window, font = ("Arial", 14, "bold"), fg= "yellow")
entry.pack(pady=5)

search_button = tk.Button(window, text = "Search", font = ("Arial", 14, "bold"), command=getFruit, bg = "blue")
search_button.pack()
window.mainloop()
