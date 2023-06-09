Portal
==============================================

Portal - корпоративный портал (база знаний) для крупной компании. Любой сотрудник может зайти на портал, найти нужную инструкцию или ответ на популярный вопрос.
Бизнес-ценность такого проекта: работа идет быстрей, а процессы прозрачные и стандартизированные.


Запуск виртуального окружения
==============================================

Самое первое, что необходимо сделать, это создать папку для нового проекта "portal".
Для запуска портала необходимо создать виртуальное окружение с помощью инструмента venv.
Команда для создания виртуального окружения:

python -m venv venvPortal

Далее необходимо запустить виртуальное окружение в терминале командой:

 .\venvPortal\Scripts\activate

При необходимости деактировать виртуальное окружение можно командой:

 deactivate

Далее необходимо открыть VScode, нажать комбинацию клавиш CTRL + SHIFT + P и выбрать интерпретатор из папки виртуального окружения venvPortal.


Установка и запуск фреймворка django на VSCode
==============================================

Для установки django в виртуальное окружение используется команда:

 pip install django

Следующим шагом создаётся проект:

 python -m startproject django_portal

Запуск сервера производится непосредственно через команду:

 python manage.py runserver

Для проверки работы сервера необходимо ввести в браузере адрес: http://127.0.0.1:8000/

Чтобы остановить сервер можно воспользоваться сочетанием клавиш CTRL + C.

Добавление приложений
==============================================

В проекте было создано два приложения. Для это использовались следующие команды:

 python manage.py startapp employees - для создания приложения с сотрудниками;

 python manage.py startapp instructions - для создания приложения с инструкциями;

 python manage.py startapp questions - для создания приложения с ответами на часто задаваемые вопросы.

Состав проекта
==============================================

Проект имеет главную страницу по адресу http://127.0.0.1:8000/ с текстом: "Это главная страница нашего корпоративного портала."
Приложение с сотрудниками по адресу: http://127.0.0.1:8000/employee;
Приложение с инструкциями по адресу: http://127.0.0.1:8000/instruction;
И приложение с ответами на часто задаваемые вопросы по адресу: http://127.0.0.1:8000/question

Создание моделей
==============================================

Для использования приложения необходимо создать модель в каждом приложении.
После создания моделей, их следует прописать в файле settings.py в основной папке проекта в списке **INSTALLED_APPS**.

Применение миграций
==============================================

Для создания миграций необходимо использовать команду:

 python manage.py makemigrations

А затем, для их применения используется команда:

 python manage.py migrate

Создание суперюзера
==============================================

Введя в консоли команду:
 
 python manage.py createsuperuser

Терминал предложит ввести Вам:
 - логин пользователя. В нашем случае использовался логин admin.
 - почту пользователя. Например admin@admin.ru
 - пароль пользователя. к вышеназванному логину использовался "12345"

После запуска сервера, для использования админкой панели в строку браузера следует ввести адрес: 

 http://127.0.0.1:8000/admin

И воспользоваться только что созданным суперпользователем.
