# Домашнее задание #10

### 1. Логирование LRUCache

Добавить логирование разного уровня в файл cache.log для LRUCache.
По аргументу командной строки "-s" дополнительно логировать в stdout с отдельным форматированием.

Логирование должно покрывать как минимум следующие случаи:
- get существующего ключа
- get отсутствующего ключа
- set отсутствующего ключа
- set отсутствующего ключа, когда достигнута ёмкость
- set существующего ключа
- различные debug записи в дополнение и в зависимости от реализации

При запуске модуля должны выполняться все перечисленные операции с кэшом (через функцию в `if __name__ == "__main__"`).

Код решения должен быть целиком в каталоге данного ДЗ без ссылок/импортов на домашки про LRUCache.
Корректность LRUCache в данном задании не проверяется.

### 2. flake8 и pylint

~~~
python lru_cache_dict.py -s
~~~