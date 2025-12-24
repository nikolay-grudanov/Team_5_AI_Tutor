---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.78
tokens: 7431
characters: 1895
timestamp: 2025-12-24T02:23:12.027248
finish_reason: stop
---

Цикл обучения

Цикл обучения использует созданные в начале объекты для обновления параметров модели так, чтобы ее эффективность со временем росла. Точнее говоря, цикл обучения состоит из двух циклов: внутреннего цикла по мини-пакетам из набора данных и внешнего цикла, повторяющего внутренний нужное число раз. Во внутреннем цикле для каждого мини-пакета вычисляется функция потерь, а параметры модели обновляются с помощью оптимизатора. Соответствующий код приведен в примере 3.21; более подробное описание происходящего следует далее.

Пример 3.21. Простейший цикл обучения

for epoch_index in range(args.num_epochs):
    train_state['epoch_index'] = epoch_index

    # Проход в цикле по обучающему набору данных

    # Настройки: создаем генератор пакетов, устанавливаем значения переменных loss и acc равными 0, включаем режим обучения
    dataset.set_split('train')
    batch_generator = generate_batches(dataset,
        batch_size=args.batch_size,
        device=args.device)
    running_loss = 0.0
    running_acc = 0.0
    classifier.train()

    for batch_index, batch_dict in enumerate(batch_generator):
        # Процедура обучения состоит из пяти шагов:

        # Шаг 1. Обнуляем градиенты
        optimizer.zero_grad()

        # Шаг 2. Вычисляем выходные значения
        y_pred = classifier(x_in=batch_dict['x_data'].float())

        # Шаг 3. Вычисляем функцию потерь
        loss = loss_func(y_pred, batch_dict['y_target'].float())
        loss_batch = loss.item()
        running_loss += (loss_batch - running_loss) / (batch_index + 1)

        # Шаг 4. Получаем градиенты на основе функции потерь
        loss.backward()

        # Шаг 5. Оптимизатор обновляет значения параметров по градиентам
        optimizer.step()

        # ---------------------------------------------
        # Вычисляем точность
        acc_batch = compute_accuracy(y_pred, batch_dict['y_target'])