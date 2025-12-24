---
source_image: page_322.png
page_number: 322
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.71
tokens: 6339
characters: 1319
timestamp: 2025-12-24T04:03:06.587432
finish_reason: stop
---

AddOutputFilterByType DEFLATE application/xhtml+xml
AddOutputFilterByType DEFLATE application/xml
AddOutputFilterByType DEFLATE font/opentype
AddOutputFilterByType DEFLATE font/otf
AddOutputFilterByType DEFLATE font/ttf
AddOutputFilterByType DEFLATE image/svg+xml
AddOutputFilterByType DEFLATE image/x-icon
AddOutputFilterByType DEFLATE text/css
AddOutputFilterByType DEFLATE text/html
AddOutputFilterByType DEFLATE text/javascript
AddOutputFilterByType DEFLATE text/plain
AddOutputFilterByType DEFLATE text/xml
# Следующая строка для .js и .css
AddOutputFilter DEFLATE js css
AddOutputFilterByType DEFLATE text/plain text/xml application/xhtml+xml text/css application/javascript application/xml application/rss+xml application/atom_xml application/x-javascript application/x-httpd-php application/x-httpd-fastphp text/html
</IfModule>
<IfModule mod_setenvif.c>
# Удалить ошибки браузера (требуется только для очень старых браузеров)
BrowserMatch ^Mozilla/4 gzip-only-text/html
BrowserMatch ^Mozilla/4\.0[678] no-gzip
BrowserMatch \bMSIE !no-gzip !gzip-only-text/html
</IfModule>
<IfModule mod_headers.c>
Header append Vary User-Agent env=!dont-vary
</IfModule>
<ifModule mod_gzip.c>
mod_gzip_on Yes
mod_gzip_dechunk Yes
mod_gzip_item_include file .(html?|txt|css|js|php|pl)$
mod_gzip_item_include handler ^cgi-script$