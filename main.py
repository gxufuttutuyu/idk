import tkinter as tk
import requests
from bs4 import BeautifulSoup


def search():
    word = entry.get().strip().lower()
    url = f"https://wikipedia.org{word.replace(' ', '_')}"

    try:
        html = requests.get(url, timeout=5).text
        text = " ".join(BeautifulSoup(html, "html.parser").get_text().split())

        sentences = text.split(". ")

        found_sentence = None
        for s in sentences:
            if word in s.lower():
                found_sentence = s
                break

        if found_sentence:
            result_label.config(text=f"Знайшов:\n\n{found_sentence}.:)", fg="green")
        else:
            result_label.config(text="Слова не бачу:(", fg="red")
    except:
        result_label.config(text="Помилка зв'язку з Вікі:(", fg="red")

root = tk.Tk()
root.geometry("400x200")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Знайти", command=search).pack()

result_label = tk.Label(root, text="", wraplength=380, justify="left")
result_label.pack(pady=10)

root.mainloop()