---
source_image: page_461.png
page_number: 461
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.23
tokens: 7254
characters: 1074
timestamp: 2025-12-24T03:12:49.265877
finish_reason: stop
---

```
},
    "TAX": {
        "0": 296.0
    },
    "PTRATIO": {
        "0": 15.3
    },
    "B": {
        "0": 396.9
    },
    "LSTAT": {
        "0": 4.98
    }
}

Результаты имеют следующий вид:
{ "prediction": [ 20.35373177134412 ] }
"""

json_payload = request.json
LOG.info(f"JSON payload: {json_payload}")
inference_payload = pd.DataFrame(json_payload)
LOG.info(f"inference payload DataFrame: {inference_payload}")
scaled_payload = scale(inference_payload)
prediction = list(clf.predict(scaled_payload))
return jsonify({'prediction': prediction})

if __name__ == "__main__":
    clf = joblib.load("boston_housing_prediction.joblib")
    app.run(host='0.0.0.0', port=80, debug=True)

Файл run_docker.sh:

#!/usr/bin/env bash

# Сборка образа [Docker]
docker build --tag=flasksklearn .

# Вывод списка образов Docker
docker image ls

# Запуск приложения Flask
docker run -p 8000:80 flasksklearn

Файл run_kubernetes.sh:

#!/usr/bin/env bash

dockerpath="noahgift/flasksklearn"

# Запускаем в контейнере Docker Hub с помощью Kubernetes
kubectl run flaskskearlndemo\
```