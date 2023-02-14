import subprocess
import chardet

"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.
"""


def presenter(*args):
    for item in args:
        for word in item:
            print(f'Тип {word} -> {type(word)}, длина {len(word)}')


words = [
    'разработка',
    'сокет',
    'декоратор',
]

online_converted_words = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440',
]

presenter(words, online_converted_words)

"""
Тип сокет -> <class 'str'>, длина 5
Тип декоратор -> <class 'str'>, длина 9
Тип разработка -> <class 'str'>, длина 10
Тип сокет -> <class 'str'>, длина 5
Тип декоратор -> <class 'str'>, длина 9
Тип разработка -> <class 'str'>, длина 10
"""


"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""


def presenter_one_more_time(*args):
    for item in args:
        for word in item:
            print(f'Тип {word} -> {type(word)}, длина {len(word)}')


bytes_words = [
    b'class',
    b'function',
    b'method',
]

presenter_one_more_time(bytes_words)

"""
Тип b'class' -> <class 'bytes'>, длина 5
Тип b'function' -> <class 'bytes'>, длина 8
Тип b'method' -> <class 'bytes'>, длина 6
"""

"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""


def impossible_byte_type(*args):
    for word in args:
        try:
            eval(f'b"{word}"')
        except SyntaxError:
            print(f'Слово {word} невозможно записать в байтовом типе')


some_words = [
    'attribute',
    'класс',
    'функция',
    'type',
]

impossible_byte_type(*some_words)

"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""


def codec(*args):
    for word in args:
        encoded_word = word.encode('utf-8')
        print(
            f'Байты: {encoded_word}, строка - {encoded_word.decode("utf-8")}')


words_to_codec = [
    'разработка',
    'администрирование',
    'protocol',
    'standart',
]

codec(*words_to_codec)

"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
"""

LIMIT_OF_LINES = 5


def ping_hosts(*args) -> None:
    for host in args:
        ping_out = subprocess.Popen(
            args=('ping', host), stdout=subprocess.PIPE)
        lines = 0
        for line in ping_out.stdout:
            lines += 1
            encoding = chardet.detect(line)['encoding']
            print(line.decode(f'{encoding}').strip())
            if lines > LIMIT_OF_LINES:
                ping_out.terminate()


hosts = [
    'yandex.ru',
    'youtube.com',
]

ping_hosts(*hosts)

"""
Обмен пакетами с yandex.ru [5.255.255.80] с 32 байтами данных:
Ответ от 5.255.255.80: число байт=32 время=20мс TTL=247
Ответ от 5.255.255.80: число байт=32 время=20мс TTL=247
Ответ от 5.255.255.80: число байт=32 время=20мс TTL=247
Ответ от 5.255.255.80: число байт=32 время=20мс TTL=247

Статистика Ping для 5.255.255.80:
Пакетов: отправлено = 4, получено = 4, потеряно = 0
(0% потерь)
Приблизительное время приема-передачи в мс:
Минимальное = 20мсек, Максимальное = 20 мсек, Среднее = 20 мсек

Обмен пакетами с youtube.com [64.233.165.136] с 32 байтами данных:
Ответ от 64.233.165.136: число байт=32 время=28мс TTL=107
Ответ от 64.233.165.136: число байт=32 время=25мс TTL=107
Ответ от 64.233.165.136: число байт=32 время=25мс TTL=107
Ответ от 64.233.165.136: число байт=32 время=25мс TTL=107

Статистика Ping для 64.233.165.136:
Пакетов: отправлено = 4, получено = 4, потеряно = 0
(0% потерь)
Приблизительное время приема-передачи в мс:
Минимальное = 25мсек, Максимальное = 28 мсек, Среднее = 25 мсек
"""


"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
path = 'test_file.txt'

strings = [
    'сетевое программирование',
    'сокет',
    'декоратор',
]

with open(path, 'w') as f:
    for chunk in strings:
        f.write(chunk + '\n')

with open(path, 'rb') as f:
    print(f'Кодировка: {chardet.detect(f.read())["encoding"]}')

with open(path, 'r', encoding='raw_unicode_escape') as f:
    print(f.read())

"""
Кодировка: windows-1251
ñåòåâîå ïðîãðàììèðîâàíèå
ñîêåò
äåêîðàòîð
"""
