import subprocess

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
    u'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    u'\u0441\u043e\u043a\u0435\u0442',
    u'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440',
]

# presenter(words, online_converted_words)

"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""   

bytes_words= [
    b'class',
    b'function',
    b'method',
]

# presenter(bytes_words)

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

# impossible_byte_type(*some_words)

"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

def codec(*args):
    for word in args:
        encoded_word = word.encode('utf-8')
        print(f'Байты: {encoded_word}, строка - {encoded_word.decode("utf-8")}')

words_to_codec = [
    'разработка',
    'администрирование',
    'protocol',
    'standart',
]

# codec(*words_to_codec)

"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
""" 
LIMIT_OF_LINES = 5

hosts = [
    'yandex.ru',
    'youtube.com',
]

for host in hosts:
    ping_out = subprocess.Popen(args=('ping', host), stdout=subprocess.PIPE)
    lines = 0
    for line in ping_out.stdout:
        lines += 1
        print(line.decode('utf-8').strip())
        if lines > LIMIT_OF_LINES:
            ping_out.terminate()

"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""