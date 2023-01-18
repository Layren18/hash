import PySimpleGUI as sg
import hashlib
import time

# интерфейс
sg.theme('DefaultNoMoreNagging')
layout = [
    [sg.Text('Файл'), sg.InputText(k='-IN-'), sg.FileBrowse('Найти...'),
     sg.Radio('MD5', 'RADIO', key='MD', enable_events=True),
     sg.Radio('SHA256', 'RADIO', key='SHA', enable_events=True)],
    [sg.Text(k='-OUTPUT-')],
    [sg.Button('Запустить'), sg.Cancel('Выйти')]
]
window = sg.Window('Хэширование', layout)

# логика
while True:
    event, values = window.read()

    # завершение работы программы
    if event in (None, 'Exit', 'Выйти'):
        break

    # работа с файлами
    file = open(values['-IN-'], 'r')
    file1 = values['-IN-']
    file1 = file1[values['-IN-'].rfind("/") + 1:]
    hash = open('hash_' + file1, 'w')
    strings = file.readlines()

    # реализация алгоритма MD5
    if event == 'Запустить' and values['MD'] == True:
        for string in strings:
            hash_object = hashlib.md5(string.encode())
            hash_object = hash_object.hexdigest()
            hash.write(hash_object + "\n")
        window['-OUTPUT-'].update('Файл успешно захэширован!')
    # реализация алгоритма SHA256
    elif event == 'Запустить' and values['SHA'] == True:
        for string in strings:
            hash_object = hashlib.sha256(string.encode())
            hash_object = hash_object.hexdigest()
            hash.write(hash_object + "\n")
        window['-OUTPUT-'].update('Файл успешно захэширован!')
    elif event == 'Запустить':
        window['-OUTPUT-'].update('Не выбран алгоритм шифрования!')

    file.close()
    hash.close()

window.close()

