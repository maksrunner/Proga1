header = '+---------Число--------' \
         '+--------Квадрат-------' \
         '+----------Куб---------' \
         '+'
line_fmt = '| {0:20.3f} | {1:20.3f} | {2:20.3f} |'
inv = False # Переменная inv...
while True:
    try:
        name = input('Введите имя входного файла: ').replace('\n', '')# Ввод названия файла...
        inv = open(name, "r") # Происходит процесс записи содержимого входного файла в память python...
        break
    except:  # Обработка всех возникающих ошибок...
        print('Такого файла не существует!!!')
outv = False # Переменная outv...
while True:
        name = input('Введите имя выходного файла: ').replace('\n', '')
        outv = open(name, "w")# Происходит процесс записи содержимого входного файла из памяти python в выходной файл...
        break
def double_print(s, fout):
    print(s)
    print(s, file=fout)
 
with inv as fin, \
     outv as fout:
    double_print(header, fout)
    for n in map(float, fin):
        double_print(
            line_fmt.format(n, n ** 2, n ** 3),
            fout)