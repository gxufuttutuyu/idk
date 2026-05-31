import requests
from bs4 import BeautifulSoup

urls = [
    "https://uk.wikipedia.org/wiki/Python",
]

search_word = input("Що хочеш знайти в вікіпедії?   ").strip().lower()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

print("\n--- Починаєм пошук ---")

for url in urls:
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        for script in soup(["script", "style"]):
            script.decompose()

        site_text = soup.get_text().lower()

        preview = " ".join(site_text.split())[:120]
        print(f"\nСайт відкрито: {url}")
        print(f"Початок тексту на сайті: \"{preview}...\"")

        if search_word in site_text:
            print(f"Результат: Знайдено слово '{search_word}':)")
        else:
            print(f"Результат: Слово '{search_word}' не знайдено:(")

    except Exception as error:
        print(f"\n⚠️ Помилка: немає зв'язку з сайтом {url}: {error}")