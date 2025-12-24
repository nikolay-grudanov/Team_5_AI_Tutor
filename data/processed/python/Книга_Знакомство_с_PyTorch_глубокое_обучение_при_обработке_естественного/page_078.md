---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.85
tokens: 7498
characters: 2098
timestamp: 2025-12-24T02:23:17.158437
finish_reason: stop
---

running_acc += (acc_batch - running_acc) / (batch_index + 1)

train_state['train_loss'].append(running_loss)
train_state['train_acc'].append(running_acc)

# Проход в цикле по проверочному набору данных

# Настройки: создаем генератор пакетов, устанавливаем значения переменных loss и acc равными 0, включаем режим проверки
dataset.set_split('val')
batch_generator = generate_batches(dataset,
    batch_size=args.batch_size,
    device=args.device)

running_loss = 0.
running_acc = 0.
classifier.eval()

for batch_index, batch_dict in enumerate(batch_generator):

    # Шаг 1. Вычисляем выходные значения
    y_pred = classifier(x_in=batch_dict['x_data'].float())

    # Шаг 2. Вычисляем функцию потерь
    loss = loss_func(y_pred, batch_dict['y_target'].float())
    loss_batch = loss.item()
    running_loss += (loss_batch - running_loss) / (batch_index + 1)

    # Шаг 3. Вычисляем точность
    acc_batch = compute_accuracy(y_pred, batch_dict['y_target'])
    running_acc += (acc_batch - running_acc) / (batch_index + 1)

train_state['val_loss'].append(running_loss)
train_state['val_acc'].append(running_acc)

В первой строке используется цикл for, в котором мы проходим по эпохам. Количество эпох задается в гиперпараметре. Оно определяет количество проходов по набору данных, выполняемых процедурой обучения. На практике лучше воспользоваться чем-то вроде критерия раннего останова, чтобы завершить этот цикл, а не дожидаться его окончания. В прилагаемых к книге материалах показано, как это сделать.

Вверху цикла for видим несколько объявлений и задания начальных значений. Во-первых, устанавливается значение индекса для эпохи состояния обучения. Далее указывается нужный фрагмент набора данных (сначала 'train', затем, когда мы хотим оценить эффективность модели в конце эпохи, — 'val' и, наконец, 'test' для окончательной оценки эффективности модели). Учитывая архитектуру нашего набора данных, необходимо всегда задавать фрагмент до вызова generate_batches(). После создания batch_generator задаются начальные значения двух переменных с плавающей точкой для отслеживания изменения потерь