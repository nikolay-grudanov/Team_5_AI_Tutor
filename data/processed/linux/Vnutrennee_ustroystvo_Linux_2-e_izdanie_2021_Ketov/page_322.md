---
source_image: page_322.png
page_number: 322
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.61
tokens: 7167
characters: 1089
timestamp: 2025-12-24T04:41:13.200371
finish_reason: stop
---

Листинг 7.35. Интерпретатор Python и библиотека интерфейсных элементов Gtk

homer@ubuntu:~$ cat gtk-hello.py
#!/usr/bin/python

import gtk

w = gtk.Window()
box = gtk.VBox()
w.add(box)

l = gtk.Label("Hello, world!")
box.add(l)

b = gtk.Button("Quit")
box.add(b)

def terminate(o):
    gtk.main_quit()

b.connect("clicked", terminate)
w.show_all()
gtk.main()

Каждая библиотека виджетов при ее использовании для построения пользовательского интерфейса обладает своей спецификой, но в целом имеет много общего с другими библиотеками интерфейсных элементов. Для сравнения в листинге 7.36 приведена программа на языке Python, использующая библиотеку Qt1, в которой можно найти много общего с программой из листинга 7.35, написанной на том же языке, но использующей библиотеку Gtk.

Листинг 7.36. Интерпретатор Python и библиотека интерфейсных элементов QtGui

homer@ubuntu:~$ cat qt-hello.py
#!/usr/bin/python

import sys
from PyQt4 import QtGui, Qt

a = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
box = QtGui.QVBoxLayout()
w.setLayout(box)

1 Требует установленного пакета python-qt4.