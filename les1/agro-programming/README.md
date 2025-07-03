# Задание: Облёт площадки и сканирование ArUco-маркеров

## Описание

Вам необходимо запрограммировать траекторию полёта квадрокоптера, чтобы он облетел площадку 1,3х4,3х2 м метра и просканировал ArUco-маркеры, расположенные на ней. Обнаруженные идентификаторы маркеров выводятся в консоль. После облёта участники должны будут присвоить каждому ID значение 1 или 2.

## Скачивание проекта

1. Установите Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)

2. Откройте терминал (или командную строку).

3. Выполните команду:

```bash
git clone https://github.com/pavlentiod/agro-programming.git
```

4. Перейдите в папку проекта:

   ```bash
   cd agro-programming
   ```

---

## Структура проекта

```
agro-programming/
├── fly_task.py           # Ваша функция полёта (сюда нужно дописывать код)
└── src/                  # Основная логика
    ├── launch.py         # Запускает полёт и сканирование
    ├── scan.py           # Сканирование ArUco-маркеров с камеры
    └── requirements.txt  # Зависимости проекта
```

---

## Установка и настройка

### 1. Установка Python

* Перейдите на сайт: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Выберите версию **Python 3.9** (поддерживаются версии 3.7–3.10).
* При установке обязательно установите галочку **"Add Python to PATH"**.

📷
![Add to PATH](https://storage.yandexcloud.net/pioneer-doc.geoscan.ru-static/images/programming/python/prep/img01.png)

---

### 2. Установка среды разработки PyCharm

* Скачайте [PyCharm Community Edition](https://www.jetbrains.com/ru-ru/pycharm/download/).
* Запустите программу → нажмите **New Project**.
* В разделе *"New environment using"* выберите **Virtualenv**.

📷
![Создание проекта](https://storage.yandexcloud.net/pioneer-doc.geoscan.ru-static/images/programming/python/prep/img04.png)

---

### 3. Установка зависимостей

Откройте терминал (в PyCharm или отдельно) и выполните:

```bash
pip install -r src/requirements.txt
```

---

## Настройка среды

После создания проекта убедитесь, что:

* используется виртуальное окружение (в корне есть папка `venv`);
* внизу PyCharm указан терминал внутри окружения.

📷
![venv и терминал](https://storage.yandexcloud.net/pioneer-doc.geoscan.ru-static/images/programming/python/prep/img05.png)

Если окружение неактивно — проверьте настройки:
`File → Settings → Tools → Terminal → Shell path → cmd`

📷
![Настройка терминала](https://storage.yandexcloud.net/pioneer-doc.geoscan.ru-static/images/programming/python/prep/img06.png)

---

## Инструкция по выполнению задания

1. Откройте файл `fly_task.py`.
2. Найдите функцию `fly_task()`.
3. Допишите туда свою траекторию облёта площадки 3×3 м.
4. Убедитесь, что программа:

   * взлетает;
   * облетает все 9 точек (шаг 1 метр);
   * завершает работу посадкой.

📘 Методы управления дроном:
🔗 [https://docs.geoscan.ru/pioneer/programming/python/pioneer-sdk-methods.html](https://docs.geoscan.ru/pioneer/programming/python/pioneer-sdk-methods.html)

---

## Запуск

Для запуска программы:

```bash
python fly_task.py
```

Откроется окно с изображением с камеры. Обнаруженные ArUco-маркеры будут:

* выделены рамками на видео;
* выведены в консоль.

---

## Правила

* Не изменяйте файлы в папке `src/`.
* Ваш код должен быть только в `fly_task.py`, внутри функции `fly_task()`.
* Обязательно завершайте полёт посадкой дрона (`drone.land()`).

## ⚠️ Важно
Всё программирование должно выполняться только внутри функции fly_task() в файле fly_task.py.

Изменение других файлов (в папке src/) запрещено.


