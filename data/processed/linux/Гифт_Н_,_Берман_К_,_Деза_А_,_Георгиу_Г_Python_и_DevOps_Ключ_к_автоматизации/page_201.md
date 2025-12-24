---
source_image: page_201.png
page_number: 201
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.19
tokens: 7383
characters: 1464
timestamp: 2025-12-24T03:06:13.729000
finish_reason: stop
---

val = {"value": value}
return jsonify(val)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

16. Передайте параметры для проверки работы этой функции:

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

Например, обращение к следующему маршруту приведет к передаче слова lion в функцию name в Flask:

https://8080-dot-3104625-dot-devshell.appspot.com/name/lion

При этом возвращается значение в веб-браузере:

{
value: "lion"
}

17. Разверните приложение:

gcloud app deploy

Учтите, что в первый раз развертывание займет около десяти минут. Кроме того, возможно, вам придется включить облачное API сборки.

Do you want to continue (Y/n)? y
Beginning deployment of service [default]...

Uploading 934 files to Google Cloud Storage

18. Выполните потоковую передачу файлов журналов:

gcloud app logs tail -s default

19. Приложение для промышленной эксплуатации развернуто, что должно выглядеть примерно так:

Setting traffic split for service [default]...done.
Deployed service [default] to [https://helloml-xxx.appspot.com]
You can stream logs from the command line by running:
    $ gcloud app logs tail -s default

    $ gcloud app browse
(venv) noah_gift@cloudshell:~/python-docs-samples/appengine/\
    standard_python37/hello_world (helloml-242121)$ gcloud app logs tail -s default
Waiting for new log entries...
2019-05-29 22:45:02 default[2019]   [2019-05-29 22:45:02 +0000] [8]