---
source_image: page_150.png
page_number: 150
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.70
tokens: 7557
characters: 2689
timestamp: 2025-12-24T02:25:11.214573
finish_reason: stop
---

функции потерь, либо применяется многомерная логистическая функция для создания распределения вероятности по фамилиям¹.

Аргументы модели: размер вложений, число вложений (то есть размер словаря), число классов и размер скрытого состояния RNN. Два из этих аргументов — число вложений и число классов — определяются данными. Остальные гиперпараметры: размер вложений и размер скрытого состояния. Хотя они могут принимать произвольные значения, обычно имеет смысл начать с маленьких значений, чтобы выполнить обучение быстро и проверить, что модель работает.

Пример 6.4. Реализация модели SurnameClassifier с помощью RNN Элмана

class SurnameClassifier(nn.Module):
    """ RNN для извлечения признаков & и MLP для классификации """
    def __init__(self, embedding_size, num_embeddings, num_classes,
                 rnn_hidden_size, batch_first=True, padding_idx=0):
        """
        Аргументы:
            embedding_size (int): размер вложений символов
            num_embeddings (int): количество символов для создания вложений
            num_classes (int): размер вектора предсказаний
                Примечание: количество национальностей
            rnn_hidden_size (int): размер скрытого состояния RNN
            batch_first (bool): указывает, будут ли в нулевом измерении входных тензоров находиться данные пакета или последовательности
            padding_idx (int): индекс для дополнения нулями тензора;
                см. torch.nn.Embedding
        """
        super(SurnameClassifier, self).__init__()
        self.emb = nn.Embedding(num_embeddings=num_embeddings,
                                embedding_dim=embedding_size,
                                padding_idx=padding_idx)
        self.rnn = ElmanRNN(input_size=embedding_size,
                            hidden_size=rnn_hidden_size,
                            batch_first=batch_first)
        self.fc1 = nn.Linear(in_features=rnn_hidden_size,
                             out_features=rnn_hidden_size)
        self.fc2 = nn.Linear(in_features=rnn_hidden_size,
                             out_features=num_classes)

    def forward(self, x_in, x_lengths=None, apply_softmax=False):
        """ Прямой проход классификатора

        Аргументы:
            x_in (torch.Tensor): тензор входных данных
                Значение x_in.shape должно быть (batch, input_dim)
            x_lengths (torch.Tensor): длины всех последовательностей пакета,

¹ В этом примере число классов невелико. Во многих же ситуациях в NLP число классов на выходе может достигать тысяч или даже сотен тысяч. В подобных случаях будет оправданым использование иерархической многомерной логистической функции вместо «наивной» многомерной.