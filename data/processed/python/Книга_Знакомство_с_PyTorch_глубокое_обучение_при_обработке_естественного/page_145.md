---
source_image: page_145.png
page_number: 145
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.17
tokens: 7474
characters: 2160
timestamp: 2025-12-24T02:25:01.752528
finish_reason: stop
---

ElmanRNN с помощью RNNCell создает вышеописанные матрицы весов «скрытый в скрытый» и «входной в скрытый». Каждый вызов RNNCell() принимает в качестве аргументов матрицу входных и матрицу скрытых векторов и возвращает матрицу скрытых векторов, получившуюся в результате данного шага.

Пример 6.1. Реализация RNN Элмана с помощью класса RNNCell фреймворка PyTorch

class ElmanRNN(nn.Module):
    """ RNN Элмана, созданная с помощью RNNCell """
    def __init__(self, input_size, hidden_size, batch_first=False):
        """
        Аргументы:
            input_size (int): размер входных векторов
            hidden_size (int): размер векторов скрытого состояния
            batch_first (bool): будут ли в нулевом измерении располагаться данные пакета
        """
        super(ElmanRNN, self).__init__()

        self.rnn_cell = nn.RNNCell(input_size, hidden_size)

        self.batch_first = batch_first
        self.hidden_size = hidden_size

    def _initialize_hidden(self, batch_size):
        return torch.zeros((batch_size, self.hidden_size))

    def forward(self, x_in, initial_hidden=None):
        """ Прямой проход ElmanRNN
        Аргументы:
            x_in (torch.Tensor): тензор входных данных
                Если self.batch_first = true: x_in.shape =
                    (batch_size, seq_size, feat_size)
                В противном случае: x_in.shape =
                    (seq_size, batch_size, feat_size)
            initial_hidden (torch.Tensor): начальное скрытое состояние для RNN
        Возвращает:
            hiddens (torch.Tensor): выходные векторы RNN на каждом из шагов
                Если self.batch_first = true:
                    hiddens.shape = (batch_size, seq_size, hidden_size)
                В противном случае: hiddens.shape =
                    (seq_size, batch_size, hidden_size)
        """
        if self.batch_first:
            batch_size, seq_size, feat_size = x_in.size()
            x_in = x_in.permute(1, 0, 2)
        else:
            seq_size, batch_size, feat_size = x_in.size()

        hiddens = []

        if initial_hidden is None:
            initial_hidden = self._initialize_hidden(batch_size)