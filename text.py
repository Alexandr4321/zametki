import datetime
now=str(datetime.datetime.now())
main_menu = '''\nГлавное меню: 
        1. Открыть файл
        2. Записать файл
        3. Показать заметки
        4. Добавить заметку
        5. Найти заметку
        6. Изменить заметку
        7. Удалить заметку
        8. Выход'''


input_choice='Выберите пункт меню: '

load_successful='Заметки успешно открыты!'
save_successful='Заметки успешно сохранены'
load_error="Заметки пусты или не открыты"

input_contact={'name':'Введите заголовок: ',
               'telo':'Что будем записывать: ',
               'time': str(now)}

new_contact = {'name':'Введите заголовок: ',
               'telo':'Что будем записывать: ',
               'time': str(now)}
def new_contact_successful(name: str)->str:
    return f'Заметка{name} успешно добавлена '


cancel_input='Отмена ввода'
index_del_contact='Введите индекс Заметки которую хотите удалить: '
search_contact='Результаты поиска : '

def del_contact(name:str):
    return f'Заметка{name} успешно удалена '

input_search = 'Что будем искать: '

def empty_search(word) -> str:
    return f'Заметки содержащие слово "{word}" не найдены'

input_change = 'Какую заметку будем менять (тело заметки): '
input_index = 'Введите индекс заметки: '

change_contact = 'Введите новые данные или оставьте поле пустым, чтоб не менять: '

def change_successful(name: str) -> str:
    return f'Заметка {name} успешно изменена!'