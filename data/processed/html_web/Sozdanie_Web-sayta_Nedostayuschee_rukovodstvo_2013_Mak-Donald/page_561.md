---
source_image: page_561.png
page_number: 561
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 60.03
tokens: 11878
characters: 2244
timestamp: 2025-12-24T09:51:16.624999
finish_reason: stop
---

граммистов в цейтноте (или ленивых), потому что не требует практически никакой работы. Вам не нужно загружать ни единого файла, поскольку код для плейера находится на Web-серверах Yahoo. Вы просто вставляете на свою Web-страницу единственную ссылку на сценарий, например, такую:

<script src="http://mediaplayer.yahoo.com/js"></script>

Как вы узнали в разд. "Внешние файлы сценариев" главы 15, ссылка на сценарий позволяет вашей Web-странице применять код на JavaScript, хранящийся в отдельном файле. Это избавляет вас от необходимости копирования и вставки больших фрагментов кода на каждую страницу. Код на JavaScript для медиаплеяра Yahoo особенно остроумен. Он реагирует на события на Web-странице. Как только браузер загружает вашу страницу, код на JavaScript просматривает ее в поисках обычных ссылок <a>, указывающих на поддерживаемые медиафайлы, например формата MP3. Каждый раз, когда он находит связанный MP3-файл, браузер вставляет рядом со ссылкой крошечную пиктограммку воспроизведения. (Конечно, весь процесс занимает всего несколько микросекунд.) На рис. 17.6, вверху, показан результат.

Самое интересное происходит, когда вы щелкаете кнопкой мыши одну из этих пиктограмм. Вместо предложения загрузить файл или попытки загрузки плагина, Yahoo раскрывает плавающий музыкальный Flash-плейер (рис. 17.6, внизу). В плавающем окне начинает проигрываться песня без всяких раздражающих предупреждений системы безопасности.

Далее приведена разметка для страницы, показанной на рис. 17.6. Как видите, это обычная страница с гиперссылками. Магия медиаплеяра создается присутствием единственного элемента <script>.

<!DOCTYPE html>
<html>

<head>
    <title>A Page with the Yahoo Media Player</title>
    <style>...</style>
    <script src="http://mediaplayer.yahoo.com/js" />
</head>

<body>
    <h1>More Awesome than Awesome Itself</h1>
    <p>My band has released a number of hit songs that are so awesome, they turn sand to diamonds and make small crying babies cry less. Check them out.</p>
    <p>Our first release was <a href="song.mp3">Please Don't Forget (That I Stopped Loving You)</a>.</p>
    <p>We followed up with <a href="soundfile.mp3">Happy Times Have Gone Away</a> and <a href="song.mp3">Hot Bananas</a>.
</body>
<html>