from random import *
import json
pb = {}
help = ['/add - добавить контакт', '/showall - показать все контакты', '/edit - добавить номер к существующему контакту',
        '/search - поиск контакта', '/deleteall - удалить контакт',
        '/deletenum - удалить телефон в контакте', '/help - вызвать данную подсказку']

try:
    with open('phonebook.json', 'r', encoding='utf-8') as fh:
        pb = json.load(fh)
    print('< Телефонная книга успешно загружена! >')
except:
    print('У вас нет сохраненной телефонной книги, пожалуйста создайте новую!')

def add_contact():
    x = input('Введите фамилию абонента: ')
    y = input('Введите номер телефона абонента: ')
    pb[x] = [y]
    save()

def edit_contact():
    x = input('Введите фамилию для поиска: ')
    for key in pb:
        if key == x:
            y = input('Введите дополнительный номер телефона абонента: ')
            pb[key].append(y.strip(''))

def save():
     with open('phonebook.json', 'w', encoding='utf-8') as fh:
         fh.write(json.dumps(pb, ensure_ascii=False))
     print('Данные успешно сохранены в телефонной книге!')

#-----------------------------------------------------------------------------------------------------------------------

while True:
    print('\nДобро пожаловать в телефонный справочник!\nДля вызова списка комманд наберите: /help')
    cmd = input('\nВведите команду: ')
    if cmd == '/add':
        add_contact()
    elif cmd == '/showall':
        if pb == {}:
            print('Ваша телефонная книга пуста!')
        else:
            print('\nСписок ваших контактов: \n')
            for key in pb:
                print(key + ', тел: ' + str(pb[key]).strip('[]'))
    elif cmd == '/edit':
        edit_contact()
        save()
    elif cmd == '/search':
        x = input('Введите фамилию абонента для поиска: ')
        for key in pb:
            if key == x:
                print('\n'+ key + ', тел: ' + str(pb[key]).strip('[]'))
                break
            print('Абонента с такой фамилией нет в телефонной книге!')
            break
    elif cmd == '/deleteall':
        x = input('Введите фамилию абонента для поиска и удаления: ')
        if x in pb:
            pb.pop(x)
            save()
        else:
            print('Абонента с такой фамилией нет в телефонной книге!')
    elif cmd == '/deletenum':
        x = input('Введите фамилию абонента для поиска и удаления: ')
        if x in pb:
            print('\n'+ 'Какой из номеров телефона: ' + str(pb[x]).strip('[]') + ' пользователя ' + x + ' удалить?')
            y = int(input('Укажите номер для удаления: '))
            pb[x].remove(y)
            print('Указанный номер успешно удален!')
            save()
        else:
            print('Абонента с такой фамилией нет в телефонной книге!')
    elif cmd == '/help':
        print('\nСписок доступных команд:\n')
        print('\n'.join(help))
    else:
        print('\nНеопознанная команда!\nВведите /help для просмотра доступных команд.')