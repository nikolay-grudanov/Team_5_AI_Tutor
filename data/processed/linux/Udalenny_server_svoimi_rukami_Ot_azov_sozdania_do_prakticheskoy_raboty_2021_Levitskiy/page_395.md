---
source_image: page_395.png
page_number: 395
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.73
tokens: 6241
characters: 971
timestamp: 2025-12-24T04:04:29.427806
finish_reason: stop
---

Удаленный сервер своими руками

Откройте файл /usr/share/meteor/bundle/programs/server/assets/app/config/settings.yml и найдите в нем следующий код:

kurento:
    wsUrl: ws://bbb.example.com/bbb-webrtc-sfu

Замените на:

kurento:
    wsUrl: wss://bigbluebutton.example.com/bbb-webrtc-sfu

Также найдите код:

note:
    enabled: true
    url: http://bbb.example.com/pad

Замените его на:

note:
    enabled: true
    url: https://bigbluebutton.example.com/pad

Редактируем /usr/local/bigbluebutton/core/scripts/bigbluebutton.yml для работы видеозаписей через https:

playback_protocol: https

Поскольку флеш уже устарел, включим использование html5 по умолчанию. Отредактируйте /usr/share/bbb-web/WEB-INF/classes/bigbluebutton.properties и замените false на true в строчках

# Force all attendees to join the meeting using the HTML5 client
attendeesJoinViaHTML5Client=true
# Force all moderators to join the meeting using the HTML5 client
moderatorsJoinViaHTML5Client=true