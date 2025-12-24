---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.81
tokens: 7532
characters: 1744
timestamp: 2025-12-24T08:50:08.368545
finish_reason: stop
---

13. message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
14.
15. # Преобразование строки в список для перемешивания
16. message = list(message)
17. random.shuffle(message)
18. message = ''.join(message) # обратное преобразование в строку
19.
20. print('Test #%s: "%s..."' % (i + 1, message[:50]))
21.
22. # Проверяем все возможные ключи для каждого сообщения
23. for key in range(1, int(len(message)/2)):
24.     encrypted =
25.         transpositionEncrypt.encryptMessage(key, message)
26.     decrypted =
27.         transpositionDecrypt.decryptMessage(key, encrypted)
28. # Если дешифрованный текст не совпадает с оригинальным,
29. # вывести сообщение об ошибке и завершиться
30. if message != decrypted:
31.     print('Mismatch with key %s and message %s.' %
32.         (key, message))
33.     print('Decrypted as: ' + decrypted)
34.     sys.exit()
35.
36.
37. # Если файл transpositionTest.py выполняется как программа
38. # (а не импортируется как модуль), вызвать функцию main()
39. if __name__ == '__main__':
40.     main()

Пример выполнения программы Transposition Test

Выполнив программу transpositionTest.py, вы должны получить следующие результаты.

Test #1: "JEQLDFKJZWALCOYACUPLTRRMLWHOBXQNEAWSLGWAGQQRSRIUIQ..."
Test #2: "SWRCLUCRDOMLWZKOMAGVOTXUVVEPIOJMSBEQRQOFRGCCKENINV..."
Test #3: "BIZBPZUIWDUFXAPJTHCMDWEGHYOWKWWWSJYKDQVSFWCJNCOZZA..."
Test #4: "JEWBCEXVZAILLCHDZJCUTXASSZZRKRPMYGTGHBXQPQBEBVCODM..."
--опущено--
Test #17: "KPKHHLPUWPSSIOULGKVEFHZOKBFHXUKVSEOWOENOZSNIDELAWR..."
Test #18: "OYLFXXZENDFGSXTEAHGHPBNORCFEPBMITILSSJRGDVMNSOMURV..."
Test #19: "SOCLYBRVDPLNVJKAFDGHCQMXIOPEJSXEAAXNWCCYAGZGLZGZH... "
Test #20: "JXJGRBCKZXPUIEXOJUNZEYYSEAEGVOJWIRTSSGPUWPNZUBQND... "
Transposition cipher test passed.