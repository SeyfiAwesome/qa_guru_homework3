from datetime import datetime
import math

'''TASK 1. Создайте словарь email, содержащий следующие поля:
"subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма)'''

email = {
    "subject": "Quarterly Report",
    "from": " willbuyers@gmail.COM ",
    "to": " lukassinclair@yahoo.COM",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}

'''TASK 2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].'''

send_date = datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

'''TASK3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
Запишите обратно в email["from"] и email["to"].'''

email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

'''TASK4. Извлеките логин и домен отправителя в две переменные login и domain.'''

login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]

'''TASK5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
Сохраните в новый ключ словаря: email["short_body"].'''

email["short_body"] = email["body"][0:10] + "..."

'''TASK6. Списки доменов: создайте список личных доменов
['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
и список корпоративных доменов
['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']. с учетом того что там должны быть только уникальные значение'''

personal_domains = list(
    {'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'yandex.ru', 'mail.ru', 'list.ru',
     'bk.ru', 'inbox.ru'})
corporate_domains = list(
    {'company.ru', 'corporation.com', 'university.edu', 'organization.org', 'company.ru', 'business.net'}
)

'''TASK7. Проверьте что в списке личных и корпоративных доменов нет пересечений: ни один домен не должен входить в оба списка одновременно.'''

# Вводим переменную intersection -> Преобразуем списки в множества
intersection = set(personal_domains) & set(corporate_domains)
assert not intersection, f"Найдены пересечения доменов: {intersection}"

'''TASK8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки вхождения домена отправителя в список корпоративных доменов.'''

# Создаем переменную is_corporate, проверяем вхождение домане отправителя в списке корпоративных доменов
is_corporate = domain in corporate_domains
print("Корпоративный отправитель:", is_corporate)
# результат false свидетельствует о том, что в company нет в corporate_domains


'''TASK 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
Сохраните в email["clean_body"].'''

email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ").strip()

'''TASK 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}'''

email["sent_text"] = f"""
Кому: {email["to"]}, от {email["from"]}
Тема: {email["subject"]}, дата {email["date"]}
{email["clean_body"]}
"""

'''TASK 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.'''

sent_text_len = len(email["sent_text"])
pages = math.ceil(sent_text_len / 500)
print("Количество страниц:", pages)

'''TASK 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty, is_body_empty в котором будет хранится что тема письма содержит данные.'''

is_subject_empty = not email["subject"].strip()
print("Тема пустая: ", is_subject_empty)
is_body_empty = not email["body"].strip()
print("Тело пустое: ", is_body_empty)

'''TASK 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
Запишите в email["masked_from"].'''

email["masked_from"] = login[:2] + "***@" + domain

'''TASK 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".'''

personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")
print("Обновленный список личных доменов: ", personal_domains)

'''КОНЕЧНЫЙ ВЫВОД'''
print("\n--- FINAL RESULTS ---")
print(email)
print("is_corporate:", is_corporate)
print("pages:", pages)
print("is_subject_empty:", is_subject_empty)
print("is_body_empty:", is_body_empty)
