---
source_image: page_181.png
page_number: 181
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.47
tokens: 7364
characters: 1559
timestamp: 2025-12-24T08:50:25.151354
finish_reason: stop
---

39. totalTime = round(time.time() - startTime, 2)
40. print('%sion time: %s seconds' % (myMode.title(), totalTime))
41.
42. # Записать транслированное сообщение в выходной файл
43. outputFileObj = open(outputFilename, 'w')
44. outputFileObj.write(translated)
45. outputFileObj.close()
46.
47. print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
48. print('%sed file is %s.' % (myMode.title(), outputFilename))
49.
50.
51. # Если файл transpositionCipherFile.py выполняется как программа
52. # (а не импортируется как модуль), вызвать функцию main()
53. if __name__ == '__main__':
54.     main()

Пример выполнения программы Transposition File Cipher

Выполнив программу transpositionFileCipher.py, вы должны получить следующие результаты.

Encrypting...
Encryption time: 1.21 seconds
Done encrypting frankenstein.txt (441034 characters).
Encrypted file is frankenstein.encrypted.txt.

Новый файл frankenstein.encrypted.txt создается в той же папке, что и файл transpositionFileCipher.py. Если вы откроете этот файл с помощью редактора IDLE, то увидите зашифрованное содержимое файла frankenstein.py. Оно должно выглядеть примерно так.

PtFiyedleo a arnvmt eneeGLchongnes Mmuyedlsu0#uiSHTGA r sy,n t ys s nuaoGeL sc7s,
--опущено--

Располагая зашифрованным текстом, вы сможете переслать его тому, кто его расшифрует. Для этого у получателя сообщения тоже должна быть программа transpositionFileCipher.py.

Чтобы дешифровать текст, внесите следующие изменения в исходный код (выделены полужирным шрифтом) и вновь запустите программу.