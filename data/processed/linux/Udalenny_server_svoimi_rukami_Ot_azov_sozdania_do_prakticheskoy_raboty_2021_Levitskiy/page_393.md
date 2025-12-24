---
source_image: page_393.png
page_number: 393
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.22
tokens: 6390
characters: 1232
timestamp: 2025-12-24T04:04:29.797442
finish_reason: stop
---

server {
    server_name bigbluebutton.example.com;
    listen 80;
    listen [::]:80;
    listen 443 ssl;
    listen [::]:443 ssl;
        ssl_certificate /etc/letsencrypt/live/bigbluebutton.example.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/bigbluebutton.example.com/privkey.pem;
        ssl_session_cache shared:SSL:10m;
        ssl_session_timeout 10m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers "ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS:!AES256";
        ssl_prefer_server_ciphers on;
        ssl_dhparam /etc/nginx/ssl/dhp-4096.pem;
}

Перезапустите ngnix. Напоминаем, что сертификаты Let's Encrypte действительно в течение 90 дней и могут быть автоматически продлены. Чтобы автоматически запрашивать обновление раз в неделю, отредактируйте файл crontab для root:

$ sudo crontab -e

Добавьте в него две строки:

30 2 * * 1 /usr/bin/certbot renew >> /var/log/le-renew.log
35 2 * * 1 /bin/systemctl reload nginx

Откройте файл /etc/bigbluebutton/nginx/sip.nginx и измените протокол и порт в строке proxy_pass:

location /ws {
    proxy_pass https://203.0.113.1:7443;
    proxy_http_version 1.1;