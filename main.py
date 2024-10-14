from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_wikipedia(query):
    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Ждем, пока страница загрузится

def list_paragraphs():
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    for i, paragraph in enumerate(paragraphs):
        print(f"{i + 1}: {paragraph.text}\n")
    return paragraphs

def get_related_links():
    links = driver.find_elements(By.XPATH, '//a[@href and not(ancestor::table)]')
    return [link for link in links if link.get_attribute('href').startswith('https://en.wikipedia.org/wiki/')]

def main():
    global driver
    driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver
    try:
        while True:
            query = input("Введите ваш запрос для поиска в Википедии (или 'q' для завершения): ")
            if query.lower() == 'q':
                break

            search_wikipedia(query)
            print(f"Результаты для запроса: {query}\n")

            while True:
                print("Выберите действие:")
                print("1. Листать параграфы статьи")
                print("2. Перейти на одну из связанных страниц")
                print("3. Выйти из программы")
                action = input("Введите номер действия: ")

                if action == '1':
                    paragraphs = list_paragraphs()
                elif action == '2':
                    related_links = get_related_links()
                    if not related_links:
                        print("Нет связанных страниц.")
                        continue

                    for i, link in enumerate(related_links[:5]):  # Ограничиваем до 5 ссылок
                        print(f"{i + 1}: {link.text} - {link.get_attribute('href')}")


                    link_choice = int(input("Выберите номер страницы для перехода: ")) - 1
                    if 0 <= link_choice < len(related_links):
                        related_links[link_choice].click()
                        time.sleep(2)  # Ждем, пока новая страница загрузится
                    else:
                        print("Неверный выбор, попробуйте снова.")

                elif action == '3':
                    driver.quit()
                    return
                else:
                    print("Неверный выбор, попробуйте снова.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()


### Инструкции по запуску:
# 1. Убедитесь, что у вас установлен Python и библиотека Selenium.
# 2. Установите веб-драйвер для вашего браузера (например, ChromeDriver для Google Chrome).
# 3. Сохраните код в файл, например, `wiki_search.py`.
# 4. Запустите файл с помощью Python:
#
# python wiki_search.py
