# import datetime
from datetime import datetime


def s2d(s1):
    ms = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября",
          "декабря"]
    ds = ["первого", "второго", "третьего", "четвертого", "пятого", "шестого", "седьмого", "восьмого", "девятого",
          "десятого", "одинадцатого", "двенадцатого", "тринадцатого", "четырнадцатого", "пятнадцатого", "шестнадцатого",
          "семнадцатого", "восемнадцатого", "девятнадцатого", "двадцатого"]
    n1 = s1.split('.')
    # for j in date.split('.'):
    id = int(n1[0])
    if id <= 20:
        s = ds[id - 1]
    elif id > 20 | id < 30:
        s = "двадцать " + ds[id - 21]
    elif id == 30:
        s = "тридцатого"
    elif id > 30:
        s = "тридцать " + ds[id - 31]

    s = s + " " + ms[int(n1[1])-1] + " " + n1[2] + " года."
    return(s.capitalize())

date = '31.01.1962'

#d = datetime.strptime(date, "%d.%m.%Y")

print(s2d(date))

# get month name short version
# print(d.strftime("%d.%m.%Y"))
