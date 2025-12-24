---
source_image: page_041.png
page_number: 41
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.24
tokens: 7884
characters: 2729
timestamp: 2025-12-24T02:22:27.529326
finish_reason: stop
---

Процесс разбиения текста на токены называется токенизацией (tokenization). Например, во фразе на языке эсперанто “Maria frapis la verda sorĉistino.”1 содержится шесть токенов. Токенизация может оказаться намного сложнее обычного разбиения текста по символам, не являющимся алфавитно-цифровыми, как показано на рис. 2.2. Для таких агглютинативных языков, как турецкий, разбиения по пробелам и знакам препинания может оказаться недостаточно и могут понадобиться специализированные методики. Как вы увидите в главах 4 и 6, в некоторых видах нейронных сетей можно полностью обойти проблемы с токенизацией за счет представления текста в виде потока байтов; для агглютинативных языков это очень важно.

<table>
  <tr>
    <th>Turkish</th>
    <th>English</th>
  </tr>
  <tr>
    <td>kork(-mak)</td>
    <td>(to) fear</td>
  </tr>
  <tr>
    <td>korku</td>
    <td>fear</td>
  </tr>
  <tr>
    <td>korkusuz</td>
    <td>fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaş (-mak)</td>
    <td>(to) become fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaşmış</td>
    <td>One who has become fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştır(-mak)</td>
    <td>(to) make one fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştırıl(-mak)</td>
    <td>(to) be made fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştırılmış</td>
    <td>One who has been made fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştırılabil(-mek)</td>
    <td>(to) be able to be made fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştırılabilecek</td>
    <td>One who will be able to be made fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştırabileceklerimiz</td>
    <td>Ones who we can make fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştırabileceklerimizden</td>
    <td>From the ones who we can make fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştırabileceklerimizdenmiş</td>
    <td>I gather that one is one of those we can make fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştırabileceklerimizdenmişçesine</td>
    <td>As if that one is one of those we can make fearless</td>
  </tr>
  <tr>
    <td>korkusuzlaştırabileceklerimizdenmişçesineyken</td>
    <td>when it seems like that one is one of those we can make fearless</td>
  </tr>
</table>

Рис. 2.2. Сложность токенизации в таких языках, как турецкий, быстро растет

1 На английском эта фраза звучит как Mary slapped the green witch («Мэри шлепнула зеленую ведьму»). Мы будем постоянно использовать это предложение в качестве примера в данной главе. Не подумайте, что мы пропагандируем насилие, этот пример — наш реверанс в сторону самого известного современного учебника по искусственному интеллекту Рассела и Норвига (Russell, Norvig, 2016), в котором он также постоянно используется в качестве примера.