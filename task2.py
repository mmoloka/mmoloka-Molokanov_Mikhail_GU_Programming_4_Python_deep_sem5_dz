# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def devide_path(path: str) -> tuple[str]:
    path_list = path.split('\\')
    file_name = path_list[len(path_list) - 1].split('.')[0]
    file_extension = path_list[len(path_list) - 1].split('.')[1]
    path_list.pop()
    file_path = '\\'.join(i for i in path_list)
    return file_path, file_name, file_extension
  
path = r'C:\Users\Михаил\Desktop\sem_5dz\task2.py'
print(*devide_path(path), sep='     ')

