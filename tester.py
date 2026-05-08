import requests
import tkinter as tk


def getFruit():
    text = entry.get()
    url = requests.get(f"https://fruityvice.com/api/fruit/{text}")
    if url.status_code != 200:
        print("Error fetching data!")
        return None
    data  = url.json()
    name_label.config(text = data["name"])
    family_label.config(text = data["family"])
    genus_label.config(text = data["genus"])
    nutritions_label.config(text = data["nutrition"])
    

window = tk.Tk()
window.title("Diet For You")
window.geometry("400x300")
window.resizable(False,False)

ask = tk.Label(window, text = "What Fruit Would You Like To Find About??", font = ("Arial", 14, "bold"), fg = "yellow")
ask.pack()

name_label = tk.Label(window, text = "", font = ("Arial", 14, "bold"))
name_label.pack()
family_label = tk.Label(window, text = "", font = ("Arial", 14, "bold"))
family_label.pack()
genus_label = tk.Label(window,text= "", font = ("Arial", 14, "bold"))
genus_label.pack()
nutritions_label = tk.Label(window, text = "", font = ("Arial", 14, "bold"))
nutritions_label.pack()

entry = tk.Entry(window, font = ("Arial", 14, "bold"), fg= "yellow")
entry.pack(pady=5)

search_button = tk.Button(window, text = "Search", font = ("Arial", 14, "bold"), command=getFruit)
search_button.pack()
window.mainloop()
