---
source_image: page_269.png
page_number: 269
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.92
tokens: 7628
characters: 2219
timestamp: 2025-12-24T08:52:51.849840
finish_reason: stop
---

немся к нашему исходному коду и рассмотрим, как с помощью инструкции continue пропустить определенные участки кода в зависимости от выбранного ключа.

Использование инструкции continue для пропуска кода

В строке 35 программы с помощью функции gcd() из модуля cryptomath проверяется, являются ли ключ A и размер символьного набора взаимно простыми числами.

<table>
  <tr><th>35.</th><td>if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) !=1:</td></tr>
  <tr><th>36.</th><td>continue</td></tr>
</table>

Вспомните, что два числа называются взаимно простыми, если их наибольший общий делитель (НОД) равен 1. Если ключ A и размер символьного набора не являются взаимно простыми числами, то условие в строке 35 оказывается равно True, и тогда выполняется инструкция continue в строке 36. Это заставляет программу вернуться в начало цикла и перейти к следующей итерации. В результате программа пропускает вызов функции decryptMessage() в строке 38, так как ключ не является допустимым, и продолжает проверять другие ключи, пока не встретится подходящий.

Как только программа находит подходящий ключ, сообщение дешифруется путем вызова функции decryptMessage() с этим ключом в строке 38.

<table>
  <tr><th>38.</th><td>decryptedText = affineCipher.decryptMessage(key, message)</td></tr>
  <tr><th>39.</th><td>if not SILENT_MODE:</td></tr>
  <tr><th>40.</th><td>print('Tried Key %s... (%s)' % (key, decryptedText[:40]))</td></tr>
</table>

Если константа SILENT_MODE задана равной False, то информация о проверяемом ключе выводится на экран, в противном случае вызов функции print() в строке 40 пропускается.

В строке 42 вызывается функция isEnglish() из модуля detectEnglish, чтобы проверить, содержит ли дешифрованное сообщение осмысленный текст на английском языке.

<table>
  <tr><th>42.</th><td>if detectEnglish.isEnglish(decryptedText):</td></tr>
  <tr><th>43.</th><td># Подтвердить, что найден правильный ключ</td></tr>
  <tr><th>44.</th><td>print()</td></tr>
  <tr><th>45.</th><td>print('Possible encryption hack:')</td></tr>
  <tr><th>46.</th><td>print('Key: %s' % (key))</td></tr>
  <tr><th>47.</th><td>print('Decrypted message: ' + decryptedText[:200])</td></tr>
  <tr><th>48.</th><td>print()</td></tr>
</table>