---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.08
tokens: 7623
characters: 1942
timestamp: 2025-12-24T08:50:27.306942
finish_reason: stop
---

В строках 39 и 40 проверяется, содержит ли специальная переменная __name__ значение '__main__', и если это так, то вызывается функция main().

Тестирование программы-тестера

Мы написали программу, которая тестирует функции шифрования и дешифрования перестановочного шифра, но как узнать, что она работает правильно? Что, если в программе-тестере имеются логические ошибки и она лишь сообщает нам, что функции шифрования/дешифрования работают, хотя на самом деле это не так?

Мы можем протестировать саму программу-тестер, намеренно введя ошибки в функции шифрования/дешифрования. Тогда, если программа-тестер не обнаружит проблему, мы будем знать, что она работает не так, как ожидается.

Чтобы внести в программу логическую ошибку, откройте файл transpositionEncrypt.py и добавьте + 1 в строке 36.

transpositionEncrypt.py

<table>
  <tr>
    <th>35.</th>
    <td># Увеличить значение currentIndex</td>
  </tr>
  <tr>
    <th>36.</th>
    <td>currentIndex += key + 1</td>
  </tr>
</table>

Теперь, если запустить программу-тестер, она должна вывести следующее сообщение об ошибке.

Test #1: "JEQLDFKJZWALCOYACUPLTRRMLWHOBXQNEAWSLGWAGQQSRSIUUIQ..."
Mismatch with key 1 and message
JEQLDFKJZWALCOYACUPLTRRMLWHOBXQNEAWSLGWAGQQSRSIUUIQTRGJHDVCZECRESZJARAVIPFOBWZXXTBFOFHVSIGBWBIBBHGUWHEUUDYONTZVKNVVTTYZPDDMIDKBHTYJAHBNDVJUZDCEMFMLUXEONCZXWAWGXZSFTMJNLJOKKIJXLWAPCQNYCIQOFTEAUHRJODKLGRIZSJBXQPBMQPPFGMVUZHKFWPGNMRYXROMSCEEXLUSCFHNELYPYKCNYTOUQGBFSRDDMVIGXNYPHVPQISTATKVKM.
Decrypted as:
JQDKZACYCPTRLHBQEWLWGQRIITGHVZCEZAAIFBZXBOHSGWBHKWEUYNTVNVYPDIKHYABDJZCMMUENZWWXSTJLOKJLACNCQFEUROKGISBQBQPGVZKWGMYRMCELSFNLPKNTUGFRDVGNPVQSAKK

После того как мы намеренно ввели ошибку, программа споткнулась на первом же сообщении, как и ожидалось!

Резюме

Приобретенные к этому времени навыки программирования пригодятся вам не только для того, чтобы писать программы шифрования и дешифрования. Теперь вы умеете тестировать программы и можете убедиться в