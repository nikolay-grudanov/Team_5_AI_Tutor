---
source_image: page_867.png
page_number: 867
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.75
tokens: 7497
characters: 1622
timestamp: 2025-12-24T05:09:29.857672
finish_reason: stop
---

3. Скопируйте файлы house1 и house5 в каталог $HOME/projects/houses/:

$ cp $HOME/projects/house[15] $HOME/projects/houses

4. Рекурсивно скопируйте каталог /usr/share/doc/initscripts* в домашний каталог $HOME/projects/:

$ cp -ra /usr/share/doc/initscripts*/ $HOME/projects/

5. Рекурсивно перечислите содержимое каталога $HOME/projects/. Передайте выходные данные в команду less, чтобы просмотреть их на странице:

$ ls -lR $HOME/projects/ | less

6. Удалите файлы house6, house7 и house8 без запроса о подтверждении:

$ rm -f $HOME/projects/house[678]

7. Переместите файлы house3 и house4 в каталог $HOME/projects/houses/doors:

$ mv $HOME/projects/house{3,4} $HOME/projects/houses/doors/

8. Удалите каталог $HOME/projects/houses/doors и его содержимое:

$ rm -rf $HOME/projects/houses/doors/

9. Измените права доступа к файлу $HOME/projects/house2 таким образом, чтобы он мог быть прочитан и записан только владельцем, мог быть прочитан только группой и не имел прав для других:

$ chmod 640 $HOME/projects/house2

10. Рекурсивно измените права каталога $HOME/projects/ так, чтобы никто не мог записывать ни в какие файлы или каталоги, расположенные ниже этой точки файловой системы:

$ chmod -R a-w $HOME/projects/
$ ls -lR $HOME/projects/
/home/joe/projects/:

total 12

-r--r--r--. 1 joe joe   0 Jan 16 06:49 house1
-r--r-----. 1 joe joe   0 Jan 16 06:49 house2
-r--r--r--. 1 joe joe   0 Jan 16 06:49 house5
-r--r--r--. 1 joe joe   0 Jan 16 06:49 house9
dr-xr-xr-x. 2 joe joe 4096 Jan 16 06:57 houses
dr-xr-xr-x. 2 joe joe 4096 Jul  1 2014 initscripts-9.03.40
dr-xr-xr-x. 3 joe joe 4096 Jan 16 06:53 outdoors
...