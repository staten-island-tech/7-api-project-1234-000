import tkinter as tk
from tkinter import messagebox
import requests
import random

def creature():
    dex_number = random.randint(1,151)
    url = f"https://pokeapi.co/api/v2/pokemon/{dex_number}"
    res = requests.get(url)
    payload = res.json()
    creature_name = payload["name"]
    creature_types = [t["type"]["name"] for t in payload["types"]]
    return creature_name, creature_types

def start_round():
    global current_name, current_types
    current_name, current_types = creature()
    input_box.delete(0, tk.END)
    type_label.config(text="")
    feedback_label.config(text="Who's that Pokémon?")

def submit_answer():
    answer = input_box.get().lower()
    if not answer:
        messagebox.showwarning("Oops", "Type a Pokémon name first.")
        return
    if answer == current_name:
        feedback_label.config(text="That's right!", fg="green")
    else:
        feedback_label.config(text="Nope! Try again.", fg="red")

def reveal_type():
    joined = ", ".join(t.capitalize() for t in current_types)
    type_label.config(text=f"Type(s): {joined}")



window = tk.Tk()
window.title("Pokémon Quiz")
window.geometry("400x300")

header = tk.Label(window, text="Who's that Pokémon?", font=("Arial", 16))
header.pack(pady=10)

input_box = tk.Entry(window, width=25)
input_box.pack(pady=5)

submit_btn = tk.Button(window, text="Submit", command=submit_answer)
submit_btn.pack(pady=5)

clue_btn = tk.Button(window, text="Clue", command=reveal_type)
clue_btn.pack(pady=5)

type_label = tk.Label(window, text="", font=("Arial", 10))
type_label.pack(pady=5)

feedback_label = tk.Label(window, text="Who's that Pokémon?", font=("Arial", 12))
feedback_label.pack(pady=10)

start_round()
window.mainloop()
    