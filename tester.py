import requests
import tkinter as tk


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


search = tk.Entry(window, font = ("Arial", 14, "bold"), fg= "yellow")
search.pack()
window.mainloop()
