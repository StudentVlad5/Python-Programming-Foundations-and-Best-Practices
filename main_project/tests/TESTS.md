## Запуск тестів

### Запуск всіх тестів

```bash
pytest
```

### Запуск окремого тесту

#### Запуск з поточного каталогу tests

```bash
python test_address_book_manager.py
```

#### Використання абсолютного імпорту (якщо це доцільно):

Якщо ви запускаєте тест безпосередньо і не плануєте використовувати цей файл як частину іншого пакета, ви можете змінити імпорт на абсолютний, додавши шлях кореневого каталогу до sys.path:

У файлі tests/test_address_book_manager.py:

```python

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from modules.AddressBook_m.addressbook_m import AddressBook

# Ваш тестовий код далі
```

#### Запуск скрипта як модуля пакета з кореневого каталогу проекта:

```bash
python -m tests.test_address_book_manager
```

#### Створити файл **init**.py у каталозі tests

Хоча каталог tests може не бути логічним пакетом у вашому проєкті, наявність файлу **init**.py в ньому може допомогти Python краще розуміти структуру каталогів при використанні відносних імпортів.

Запуск з кореневого каталогу проекту

```bash
python tests/test_address_book_manager.py
```
