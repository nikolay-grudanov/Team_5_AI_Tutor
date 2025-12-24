---
source_image: page_264.png
page_number: 264
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.55
tokens: 6079
characters: 1048
timestamp: 2025-12-24T10:07:49.428212
finish_reason: stop
---

SDK и установить его несложно: как только вы загрузили SDK, запустите Android SDK Manager. С помощью данной утилиты установите утилиты платформы (Android SDK Platform tools), которые и содержат утилиту adb. Просто установите соответствующий флажок и нажмите кнопку Install. На рис. 7.18 показан Android SDK Manager на моем Mac.

Установка всего, что предлагает установить Android SDK Manager, займет очень много времени, поэтому если вам нужен только adb, отключите все остальные флажки и нажмите кнопку Install. Как только инструмент будет установлен, в основном дереве SDK появится каталог platform-tools. Теперь вам нужно подключить ваш телефон к вашему компьютеру по USB. После чего запустите adb следующим образом:

% ./adb forward tcp:9222 localabstract:chrome_devtools_remote

На вашем настольном Chrome подключитесь к http://localhost:9222 и вы увидите список URL на каждой вкладке браузера Chrome на вашем телефоне. Щелкните по вкладке, которую нужно отладить и

![Android SDK Manager](../images/ch7_18.png)

Рис. 7.18. Android SDK Manager