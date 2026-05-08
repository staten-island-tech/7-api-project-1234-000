import requests
import tkinter as tk


def getFruit():
    text = entry.get()
    url = requests.get(f"https://fruityvice.com/api/fruit/{text}")
    if url.status_code != 200:
        print("Error fetching data!")
        return None
    data  = url.json()
    name_label.config(text = f"Name: {data["name"]}")
    family_label.config(text = f"Family: {data["family"]}")
    genus_label.config(text = f"Genus: {data["genus"]}")
    nutrition_label.config(text =  data["nutritions"]["calories"])
    

window = tk.Tk()
window.title("Diet For You")
window.geometry("1200x800")
window.resizable(False,False)

ask = tk.Label(window, text = "What Fruit Would You Like To Find About??", font = ("Arial", 14, "bold"), fg = "yellow")
ask.pack()

name_label = tk.Label(window, text = "", font = ("Arial", 14, "bold"))
name_label.pack()
family_label = tk.Label(window, text = "", font = ("Arial", 14, "bold"))
family_label.pack()
genus_label = tk.Label(window,text= "", font = ("Arial", 14, "bold"))
genus_label.pack()
nutrition_label = tk.Label(window, text = "", font = ("Arial", 14, "bold"))
nutrition_label.pack()

entry = tk.Entry(window, font = ("Arial", 14, "bold"), fg= "yellow")
entry.pack(pady=5)

search_button = tk.Button(window, text = "Search", font = ("Arial", 14, "bold"), command=getFruit)
search_button.pack()
window.mainloop()
