# Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных
# (https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате `beasts.csv`
# количество животных на каждую букву алфавита. Содержимое результирующего файла:
# ```
#
# А,642
# Б,412
# В,....
# ```
#
# Примечание: анализ текста производить не нужно, считается любая запись из категории
# (в ней может быть не только название, но и, например, род)


# WARNING pip install requests
import csv
import warnings

import requests
from bs4 import BeautifulSoup


def save_letters(letters: dict):
    # letters = {'А': 1286, 'Б': 1752, 'В': 549, 'Г': 1046, 'Д': 798, 'Е': 108, 'Ж': 423, 'З': 664, 'И': 366, 'Й': 4, 'К': 2410, 'Л': 732, 'М': 1348, 'Н': 495, 'О': 834, 'П': 1858, 'Р': 607, 'С': 1901, 'Т': 1049, 'У': 280, 'Ф': 200, 'Х': 296, 'Ц': 240, 'Ч': 727, 'Ш': 289, 'Щ': 160, 'Э': 234, 'Ю': 146, 'Я': 222, 'A': 3452, 'B': 1075, 'C': 2699, 'D': 1149, 'E': 1125, 'F': 240, 'G': 746, 'H': 1174, 'I': 393, 'J': 91, 'K': 251, 'L': 1151, 'M': 1884, 'N': 915, 'O': 916, 'P': 2976, 'Q': 45, 'R': 530, 'S': 1973, 'T': 1542, 'U': 162, 'V': 201, 'W': 100, 'X': 188, 'Y': 53, 'Z': 231}
    with open('eggs.csv', 'w', newline='') as csvfile:
        spam_writer = csv.writer(csvfile, quotechar=';', quoting=csv.QUOTE_MINIMAL)
        for letter in letters:
            spam_writer.writerow([letter, letters[letter]])


def count_letter_group(letters: dict, pages_container):
    groups = pages_container.find_all('div', class_='mw-category-group')
    for group in groups:
        letter = group.find('h3').text
        # print(group)
        links = group.find_all('a')
        # print(len(links))

        count_letters = len(links)
        if letter not in letters:
            letters[letter] = count_letters
        else:
            letters[letter] += count_letters
    print(letters)


def parse_page(url: str, letters: dict):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    pages_container = soup.find('div', id='mw-pages')

    count_letter_group(letters, pages_container)

    # get next page url
    next_page_tag = soup.find("a", string="Следующая страница")
    if next_page_tag:
        href = next_page_tag['href']
        # print(href)
        new_url = DOMAIN + href
        parse_page(new_url, letters)


DOMAIN = 'https://ru.wikipedia.org'
URL = f'{DOMAIN}/wiki/Категория:Животные_по_алфавиту'

if __name__ == '__main__':
    warnings.warn('перед запуском скачать библиотеки: requests, BeautifulSoup, lxml')

    letters = {}
    parse_page(URL, letters)
    print(letters)
    # {'А': 1286, 'Б': 1752, 'В': 549, 'Г': 1046, 'Д': 798, 'Е': 108, 'Ж': 423, 'З': 664, 'И': 366, 'Й': 4,
    # 'К': 2410, 'Л': 732, 'М': 1348, 'Н': 495, 'О': 834, 'П': 1858, 'Р': 607, 'С': 1901, 'Т': 1049, 'У': 280,
    # 'Ф': 200, 'Х': 296, 'Ц': 240, 'Ч': 727, 'Ш': 289, 'Щ': 160, 'Э': 234, 'Ю': 146, 'Я': 222, 'A': 3452, 'B': 1075,
    # 'C': 2699, 'D': 1149, 'E': 1125, 'F': 240, 'G': 746, 'H': 1174, 'I': 393, 'J': 91, 'K': 251, 'L': 1151,
    # 'M': 1884, 'N': 915, 'O': 916, 'P': 2976, 'Q': 45, 'R': 530, 'S': 1973, 'T': 1542, 'U': 162, 'V': 201, 'W': 100,
    # 'X': 188, 'Y': 53, 'Z': 231}
    total_count = sum(letters.values())
    print(total_count)  # 46286
    save_letters(letters)
