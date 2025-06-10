## Введение
RU

Wine — это программа, которая позволяет запускать программы Microsoft Windows.
Она состоит из загрузчика программ, который загружает и выполняет двоичный файл 
Microsoft Windows, и библиотеки (называемой Winelib), которая реализует вызовы 
Windows API с использованием их эквивалентов в Unix, X11 или Mac. Библиотека 
также может использоваться для переноса кода Windows в собственные исполняемые 
файлы Unix.
Wine - проект с открытым исходным кодом, выпущенный под лицензией GNU.

Новичкам часто тяжело начать использовать этот инструмент( я и сам был таким) ),
поэтому я написал интуитивно понятную программу на python с визуалом.

Проект проверен на linux mint,так что на других дистрах возможно не будет работать.

!ВАЖНО! Вам никто не гарантирует адекватный запуск приложения, но по личному 
опыту всё работало отлично.

## Начало работы

Для начала работы вам нужно установить саму программу и библиотеки tkinter и pyperclip:

```
pip install tkinter
pip install pyperclip
```

Или если не сработало,но не рекомендуется:

```
pip install tkinter --break-system-packages
pip install pyperclip --break-system-packages
```

Далее вам нужно сделать скачанный файл исполняемым,а для этого нажмите:

ПКМ>Свойства>Права>Разрешить исполнять как программу

Запустите программу и следуйте инструкциям.
Удачи...

## Introduction
EN

Wine is a program that allows you to run Microsoft Windows programs.
It consists of a program loader that loads and saves a binary file.
Microsoft Windows and a library (called Winelib) that makes calls to the
Windows API using their equivalents in Unix, X11, or Mac. The library
can also be used to wrap Windows code in stand-alone executables.
Unix files.
Wine is an open source project released under the GNU license.

It is often difficult for beginners to start using this tool (I was one myself) ),
so I wrote a clear Python program with a visual.

The project has been tested on Linux Mint, so it may not work on other distros.

!IMPORTANT! No one guarantees that the application will run properly, but in my personal
experience everything worked fine.


## Getting Started

To get started, you need to install the program itself and the tkinter and pyperclip libraries:

```
pip install tkinter
pip install pyperclip
```

Or if it didn't work, but not recommended:

```
pip install tkinter --break-system-packages
pip install pyperclip --break-system-packages
```

Next, you need to make the downloaded file executable, and to do this, click:

RMB>Properties>Permissions>Allow executing as a program

Run the program and follow the instructions.
Good luck...
