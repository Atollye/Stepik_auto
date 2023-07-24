#### Содержание репозитория

В этом репозитории хранятся начальные задачи курса [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/syllabus)

#### Запуск (c помощью виртуального окружения python3-venv): 

1. Создание окружения
```
sudo apt-get install python3-venv
python3 -m venv my_test_venv
```


2. Активация окружения
```
source my_test_venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r test_automation/requirements.txt
```

3. Запуск самих тестов
```
cd Stepik_auto
pytest -s -v
```
