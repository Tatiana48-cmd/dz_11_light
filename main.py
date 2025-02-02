import os
import subprocess
from my_functions import (
    new_folder,
    delete_path,
    copy_path,
    directory_view,
    get_subdirectories,
    get_files,
    get_system_info,
)

project_path = os.path.dirname(os.path.abspath(__file__)) # Корень проекта

while True:
    print('\n1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории (*необязательный пункт)')
    print('12. Выход')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        folder_name = input('Введите название папки: ')
        new_folder(folder_name)

    elif choice == '2':
        name = input('Введите название файла/папки: ')
        delete_path(name)

    elif choice == '3':
         src_name = input('Введите название файла/папки, который/ую нужно скопировать: ')
         new_name = input('Введите название файла/папки, под которым его/её нужно записать: ')
         copy_path(src_name, new_name)

    elif choice == '4':
        directory_view(project_path)

    elif choice == '5':
        get_subdirectories(project_path)
        print(f'Список папок в директории <console file manager>: ', get_subdirectories('.'))

    elif choice == '6':
        get_files(project_path)
        print(f'Список файлов в директории <console file manager>: ', get_files('.'))

    elif choice == '7':
        system_info = get_system_info()
        for key, value in system_info.items():
            print(f"{key}: {value}")

    elif choice == '8':
        prog_creator = ('Tatiana Rostkova')
        print(f'Автор программы -', prog_creator)

    elif choice == '9':
        subprocess.run(["python", "victory.py"], check=True)

    elif choice == '10':
        subprocess.run(["python", "my_bill.py"], check=True)

    elif choice == '11':
        print('Этот пункт сделаем позже')

    elif choice == '12':
        break

    else:
        print('Неправильный пункт меню')