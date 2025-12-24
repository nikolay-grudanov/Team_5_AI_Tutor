---
source_image: page_324.png
page_number: 324
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.65
tokens: 6453
characters: 1207
timestamp: 2025-12-24T04:03:17.687915
finish_reason: stop
---

```html
<html><body>
<p>&lt;/filesMatch&gt;</p> 
 <p># Задаем 30 дней для данного типа файла</p> 
 <p>&lt;filesMatch "\.(css|js)$"&gt;</p> 
 <p>Header set Cache-Control "max-age=2592000, public"</p> 
 <p>&lt;/filesMatch&gt;</p> 
 <p># Задаем 2 дня для данного типа файла</p> 
 <p>&lt;filesMatch "\.(xml|txt)$"&gt;</p> 
 <p>Header set Cache-Control "max-age=172800, public, must-revalidate"</p> 
 <p>&lt;/filesMatch&gt;</p> 
 <p># Задаем 1 день для данного типа файла</p> 
 <p>&lt;filesMatch "\.(html|htm|php)$"&gt;</p> 
 <p>Header set Cache-Control "max-age=172800, private, must-revalidate"</p> 
 <p>&lt;/filesMatch&gt;</p> 
 <p>&lt;/ifModule&gt;</p> 
 <p># использование кеша браузеров</p> 
 <p>FileETag MTime Size</p> 
 <p>&lt;ifmodule mod_expires.c&gt;</p> 
 <p>&lt;filesmatch ".(jpg|jpeg|gif|png|ico|css|js)$"&gt;</p> 
 <p>ExpiresActive on</p> 
 <p>ExpiresDefault "access plus 1 year"</p> 
 <p>&lt;/filesmatch&gt;</p> 
 <p>&lt;/ifmodule&gt;</p> 
 <p>#Запрет отдачи HTTP-заголовков Vary браузерам семейства MSIE</p> 
 <p>&lt;IfModule mod_setenvif.c&gt;</p> 
 <p>BrowserMatch "MSIE" force-no-vary</p> 
 <p>BrowserMatch «Mozilla/4.[0-9]{2}» force-no-vary</p> 
 <p>&lt;/IfModule&gt;</p> 
</body></html>
```