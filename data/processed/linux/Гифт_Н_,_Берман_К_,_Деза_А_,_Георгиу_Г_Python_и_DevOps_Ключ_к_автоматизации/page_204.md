---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.57
tokens: 7277
characters: 1432
timestamp: 2025-12-24T03:06:10.912063
finish_reason: stop
---

import wikipedia

app = Flask(__name__)
@app.route('/')
def hello():
    """Возвращает дружеское HTTP-приветствие."""
    return 'Hello I like to make AI Apps'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Возвращает пользовательский HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/noahgift/sugar/\master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/wikipedia/<company>')
def wikipedia_route(company):

    # Импортируем клиентскую библиотеку Google Cloud
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    result = wikipedia.summary(company, sentences=10)

    client = language.LanguageServiceClient()
    document = types.Document(
        content=result,
        type=enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    return str(entities)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

В этом разделе мы показали и как создать с нуля приложение App Engine в командной оболочке Google Cloud, и как осуществлять непрерывную поставку с помощью GCP Cloud Build.