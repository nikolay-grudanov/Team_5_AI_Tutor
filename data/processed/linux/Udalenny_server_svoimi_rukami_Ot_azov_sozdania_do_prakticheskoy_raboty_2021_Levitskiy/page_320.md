---
source_image: page_320.png
page_number: 320
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.26
tokens: 6395
characters: 1014
timestamp: 2025-12-24T04:03:06.598446
finish_reason: stop
---

#add_header "X-UA-Compatible" "IE=Edge,chrome=1";

# Правила rewrite для версированного CSS + JS через директиву filemtime
location ~* ^.+\.(css|js)$ {
    rewrite ^(.+)\.(\\d+)\.(css|js)$ $1.$3 last;
# Задаем, сколько будет храниться кэш
expires 31536000s;
# Выключаем логирование
access_log off;
log_not_found off;
# Добавляем заголовки (хеадеры)
add_header Pragma public;
add_header Cache-Control "max-age=31536000, public";
}

# Агрессивное кэширование для статических файлов
location ~* \.(asf|asx|wax|wmv|wmx|avi|bmp|class|divx|doc|docx|eot|exe|gif|gz|gzip|ico|jpg|jpeg|jpe|mdb|mid|midi|mov|qt|mp3|m4a|mp4|m4v|mpeg|mpg|mpe|mpp|odb|odc|odf|odg|odp|ods|odt|ogg|ogv|otf|pdf|png|pot|pps|ppt|pptx|ra|ram|svg|svgz|swf|tar|t?gz|tif|tiff|ttf|wav|webm|wma|woff|wri|xla|xls|xlsx|xlw|zip)$ {
# Задаем сколько будет храниться кэш
expires 31536000s;
# Выключаем логирование
access_log off;
log_not_found off;
# Добавляем заголовки (хеадеры)
add_header Pragma public;
add_header Cache-Control "max-age=31536000, public";
}