# Статусы PEP и их буквенные обозначения
EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}

# URL для парсинга
PEP_URL = 'https://peps.python.org/'

# Папка для результатов
RESULTS_DIR_NAME = 'results'

# Имя файла для FEEDS
PEP_FILENAME = 'pep_%(time)s.csv'

# Формат даты для имён файлов
DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S'

# Заголовки CSV
PEP_CSV_HEADER = 'number,name,status\n'
SUMMARY_CSV_HEADER = 'Статус,Количество\n'
SUMMARY_CSV_TOTAL = 'Total,{total}\n'
