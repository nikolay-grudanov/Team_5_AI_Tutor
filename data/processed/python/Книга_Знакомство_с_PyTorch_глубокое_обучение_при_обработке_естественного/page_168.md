---
source_image: page_168.png
page_number: 168
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.43
tokens: 7493
characters: 2046
timestamp: 2025-12-24T02:25:35.301089
finish_reason: stop
---

Пример 7.8. Отображение выборок индексов в строковые значения для фамилий

def decode_samples(sampled_indices, vectorizer):
    """ Преобразование индексов в строковое представление фамилий

    Аргументы:
        sampled_indices (torch.Tensor): индексы из функции `sample_from_model`
        vectorizer (SurnameVectorizer): соответствующий векторизатор
    """
    decoded_surnames = []
    vocab = vectorizer.char_vocab

    for sample_index in range(sampled_indices.shape[0]):
        surname = ""
        for time_step in range(sampled_indices.shape[1]):
            sample_item = sampled_indices[sample_index, time_step].item()
            if sample_item == vocab.begin_seq_index:
                continue
            elif sample_item == vocab.end_seq_index:
                break
            else:
                surname += vocab.lookup_index(sample_item)
        decoded_surnames.append(surname)
    return decoded_surnames

С помощью этих функций можно просмотреть результаты работы модели, показанные в примере 7.9, и составить представление о том, научилась ли она генерировать адекватные фамилии. Какие выводы можно сделать из просмотра этих выходных данных? Хотя фамилии вроде бы следуют нескольким морфологическим паттернам, не похоже, чтобы каждая из них соответствовала одной национальности. Возможно, наша общая модель фамилий при обучении перепутала распределения символов между различными национальностями. Контекстно обусловленная модель SurnameGenerationModel призвана решить эту проблему.

Пример 7.9. Выборка из контекстно не обусловленной модели

<table>
  <tr>
    <th>Input[0]</th>
    <td>
      samples = sample_from_model(unconditioned_model, vectorizer,<br>
      num_samples=10)<br>
      decode_samples(samples, vectorizer)
    </td>
  </tr>
  <tr>
    <th>Output[0]</th>
    <td>
      ['Aqtaliby',<br>
      'Yomaghev',<br>
      'Mauasheev',<br>
      'Unander',<br>
      'Virrovo',<br>
      'NInev',<br>
      'Bukhumohe',<br>
      'Burken',<br>
      'Rati',<br>
      'Jzirmar']
    </td>
  </tr>
</table>