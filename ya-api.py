import requests
import openpyxl
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

#with open('log.csv') as inf:
#    for line in inf:
#        line = line.strip()

numbers =["8-495-783-83-09", "8(495)739-22-22", "89852520306","088124017283"]

# Скачиваем информацию из api в формате json и формируем список с ответами
company = list()
for i in range(len(numbers)):
    number = str(numbers[i])
    api_url = "https://search-maps.yandex.ru/v1/?text=" + number + "&type=biz&lang=ru_RU&apikey=85377e7a-bb31-47f7-b80f-9ca10b36335a"
    res = requests.get(api_url)
    tabs = res.json()

#Проверка на существование в справочнике
    if len(tabs['features']) > 0:
        CompanyName = tabs['features'][0]['properties']['CompanyMetaData']['name']
        company.append(CompanyName)
    else:
        company.append("Не найдено")

# Заполнение таблицы
ws['A1'] = "Номер телефона"
ws['B1'] = "Название организации"
for i in range(len(numbers)):
    xla = 'A' + str(i + 2)
    xlb = 'B' + str(i + 2)
    ws[xla] = numbers[i]
    ws[xlb] = company[i]
wb.save('test.xlsx')

