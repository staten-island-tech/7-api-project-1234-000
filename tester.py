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

ask = tk.Label(window, text = "What Fruit Would You Like To Find About??", font = ("Arial", 14, "bold"))
ask.pack()

search = tk.Entry(window, font = ("Arial", 14))
search.pack()
window.mainloop()
