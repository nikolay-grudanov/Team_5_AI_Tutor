---
source_image: page_394.png
page_number: 394
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.51
tokens: 6285
characters: 1292
timestamp: 2025-12-24T04:04:29.825728
finish_reason: stop
---

proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "Upgrade";
proxy_read_timeout 6h;
proxy_send_timeout 6h;
client_body_timeout 6h;
send_timeout 6h;

Отредактируйте /usr/share/bbb-web/WEB-INF/classes/bigbluebutton.properties и обновите свойство bigbluebutton.web.serverURL для использования HTTPS:

#-------------------------------------------------------------
# This URL is where the BBB client is accessible. When a user successfully
# enters a name and password, she is redirected here to load the client.
bigbluebutton.web.serverURL=https://bigbluebutton.example.com

Отредактируйте файл /usr/share/red5/webapps/screenshare/WEB-INF/screenshare.properties и обновите свойство jnlpUrl и jnlpFile - укажите HTTPS (везде по мере редактирования конфигурации указывайте точное имя вашего сервера):

streamBaseUrl=rtmp://bigbluebutton.example.com/screenshare
jnlpUrl=https://bigbluebutton.example.com/screenshare
jnlpFile=https://bigbluebutton.example.com/screenshare/screenshare.jnlp

Также нужно обновить файл /var/www/bigbluebutton/client/conf/config.xml чтобы сообщить клиенту BigBlueButton о загрузке компонентов через HTTPS. Вы можете сделать такое обновление с помощью одной команды:

$ sudo sed -e 's|http://|https://|g' -i /var/www/bigbluebutton/client/conf/config.xml