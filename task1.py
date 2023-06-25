# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


way = r'C:\Stady\immersion-in-python-Sem5-homeWork\Seminar\Lesson5.txt'
# way = A:\study\dive into python\seminar\seminar5(Integrators and generators)\home_work\immersion-in-python-Sem5-homeWork\README.md
def split_path(way: str) -> tuple():
    list_abs_path = way.split('\\')
    list_last_elem = list_abs_path[-1].split('.')
    path = '\\'.join(list_abs_path[0:-1])
    name = list_last_elem[0]
    file_extension = list_last_elem[1]
    return path, name, file_extension


print(split_path(way))

