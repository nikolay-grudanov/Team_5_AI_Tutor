---
source_image: page_337.png
page_number: 337
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.36
tokens: 7580
characters: 1887
timestamp: 2025-12-24T03:09:46.669235
finish_reason: stop
---

STATUS      PORTS                NAMES
Up 3 minutes   0.0.0.0:5000->5000/tcp    heuristic_roentgen

[ec2-user@ip-10-0-0-111 hello-world-docker]$ docker logs 9d67dc321ffb
* Serving Flask app "app" (lazy loading)
* Debug mode: on
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 306-476-204
72.203.107.13 - - [19/Aug/2019 04:43:34] "GET / HTTP/1.1" 200 -
72.203.107.13 - - [19/Aug/2019 04:43:35] "GET /favicon.ico HTTP/1.1" 404 -
* Detected change in '/app/app.py', reloading
* Restarting with stat
* Debugger is active!
* Debugger PIN: 306-476-204

Теперь при запросе к http://54.187.189.51:5000<sup>1</sup> будет отображаться новое приветствие — Hello, World! (from a Docker container on an EC2 Linux 2 AMI instance).

Отметим, что для запуска приложения нам не пришлось устанавливать ничего относящегося к Python или Flask. Для использования возможностей переносимости Docker достаточно было просто запустить приложение в контейнере. Не случайно Docker выбрал название «контейнеры» для продвижения своей технологии — на это воодушевил пример грузовых транспортных контейнеров, которые произвели революцию в сфере грузоперевозок.

Немало статей об упаковке приложений Python в контейнеры Docker имеется в коллекции «Создание подходящих для промышленной эксплуатации контейнеров Docker для разработчиков на языке Python» (Production-ready Docker packaging for Python developers (https://pythonspeed.com/docker) Итамара Тюрнер-Траурина (Itamar Turner-Trauring).

Запуск нескольких контейнеров Docker с помощью Docker Compose

В этом разделе мы воспользуемся руководством «Flask в примерах» (Flask By Example, https://oreil.ly/prNg7), в котором описывается, как создать приложение Flask для вычисления пар «слово — частотность» для текста, расположенного по заданному URL.

<sup>1</sup> И вновь ваш IP-адрес будет другим.