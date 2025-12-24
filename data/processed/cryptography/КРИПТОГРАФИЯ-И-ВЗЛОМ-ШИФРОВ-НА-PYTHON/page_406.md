---
source_image: page_406.png
page_number: 406
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.38
tokens: 7897
characters: 2415
timestamp: 2025-12-24T08:56:40.747902
finish_reason: stop
---

Например, чтобы зашифровать сообщение “IF YOU WANT TO SURVIVE OUT HERE, YOU’VE GOT TO KNOW WHERE YOUR TOWEL IS”, мы удаляем из него пробелы и знаки препинания, получая в результате сообщение длиной 55 букв. Для применения одноразового шифроблокнота необходимо получить ключ, длина которого тоже составляет 55 букв. Выбрав в качестве примера ключ KCQYZHEPXAUTIQEKEKXEMORETZHZTRWWQDYLBTTVEJMEDBSANYBPXQIK, мы получим шифротекст “SHOMTDECQTILCHZSSIXGHYIKDFNNMACEWRZLGHRAQQVHZGUERPLBBQC” (рис. 21.1).

<table>
  <tr>
    <th>Открытый текст</th>
    <td>IFYOUWANTTOSURVIVEOUTHEREYOUVEGOTTOKNOWWHEREYOURTOWELIS</td>
  </tr>
  <tr>
    <th>Ключ</th>
    <td>KCQYZHEPXAUTIQEKEKXEMORETZHZTRWWQDYLBTTVEJMEDBSANYBPXQIK</td>
  </tr>
  <tr>
    <th>Шифротекст</th>
    <td>SHOMTDECQTILCHZSSIXGHYIKDFNNMACEWRZLGHRAQQVHZGUERPLBBQC</td>
  </tr>
</table>

Рис. 21.1. Шифрование сообщения с помощью одноразового шифроблокнота

А теперь представьте, что криптоаналитик завладел шифротектом (“SHOMTDEC...”). Как взломать такой шифр? Полный перебор ключей методом грубой силы не сработает, так как это чересчур много даже для компьютера. Количество ключей будет равно 26 в степени, равной числу букв в сообщении. Если длина сообщения — 55 букв, как в нашем примере, то общее число возможных ключей составит \(26^{55}\), или 666 091 878 431 395 624 153 823 182 526 730 590 376 250 379 528 249 805 353 030 484 209 594 192 101 376.

Но, даже располагая компьютером, достаточно мощным для того, чтобы испытать все ключи, криптоаналитик все равно не сможет взломать одноразовый шифроблокнот, поскольку для любого шифротекста все возможные варианты открытых текстов одинаково вероятны.

Шифротекст “SHOMTDEC...” может оказаться результатом шифрования совершенно иного сообщения с тем же количеством букв, например текста “THE MYTH OF OSIRIS WAS OF IMPORTANCE IN ANCIENTEGYPTIAN RELIGION”, зашифрованного с помощью ключа ZAKAVKXOLFQDLZHWSQJBZMTWMMNAKWURWEXDCUYWKSGORGHNNEDVTCP (рис. 21.2).

<table>
  <tr>
    <th>Открытый текст</th>
    <td>THEMYTHOFOSIRISWASOFIMPORTANCEINANCIENTEGYPTIANRELIGION</td>
  </tr>
  <tr>
    <th>Ключ</th>
    <td>ZAKAVKXOLFQDLZHWSQJBZMTWMMNAKWURWEXDCUYWKSGORGHNNEDVTCP</td>
  </tr>
  <tr>
    <th>Шифротекст</th>
    <td>SHOMTDECQTILCHZSSIXGHYIKDFNNMACEWRZLGHRAQQVHZGUERPLBBQC</td>
  </tr>
</table>

Рис. 21.2. Шифрование другого сообщения с использованием другого ключа, приводящее к точно такому же шифротексту