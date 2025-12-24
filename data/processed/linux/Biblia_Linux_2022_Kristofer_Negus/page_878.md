---
source_image: page_878.png
page_number: 878
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.40
tokens: 7394
characters: 1445
timestamp: 2025-12-24T05:09:48.363714
finish_reason: stop
---

3. Чтобы установить пакет, содержащий команду mogrify, введите следующее:

# yum install ImageMagick

4. Чтобы перечислить все файлы документации, содержащиеся в пакете команды mogrify, введите следующее:

# rpm -qd ImageMagick
...
/usr/share/doc/ImageMagick/README.txt
...
/usr/share/man/man1/identify.1.gz
/usr/share/man/man1/import.1.gz
/usr/share/man/man1/mogrify.1.gz

5. Чтобы просмотреть журнал изменений пакета команды mogrify, введите следующее:

# rpm -q --changelog ImageMagick | less

6. Чтобы удалить команду mogrify из системы и проверить ее пакет по базе данных RPM, убедившись, что эта команда действительно удалена, введите следующее:

# type mogrify
mogrify is /usr/bin/mogrify
# rm /usr/bin/mogrify
rm remove regular file '/usr/bin/mogrify'? y
# rpm -V ImageMagick
missing   /usr/bin/mogrify

7. Чтобы переустановить пакет, предоставляющий команду mogrify, и убедиться, что весь пакет снова установлен, введите следующее:

# yum reinstall ImageMagick
# rpm -V ImageMagick

8. Чтобы загрузить пакет, предоставляющий команду mogrify, в текущий каталог, введите следующее:

# yum download ImageMagick
ImageMagick-6.9.10.28-1.fc30.x86_64.rpm

9. Чтобы отобразить общую информацию о пакете, который вы только что загрузили, запросив файл RPM пакета в текущем каталоге, введите следующее:

# rpm -qip ImageMagick-6.9.10.28-1.fc30.x86_64.rpm
Name        : ImageMagick
Epoch       : 1
Version     : 6.9.10.28
Release     : 1.fc30

...