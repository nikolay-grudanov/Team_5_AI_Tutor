---
source_image: page_344.png
page_number: 344
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.98
tokens: 7473
characters: 2643
timestamp: 2025-12-24T08:54:30.799825
finish_reason: stop
---

В цикле for мы проходим по всем символам строки message, преобразованным в верхний регистр. Текущий символ записывается в переменную letter. В строке 13 мы проверяем, содержится ли символ в строке LETTERS, поскольку счетчики небуквенных символов нас не интересуют. Если буква встречается в строке LETTERS, в строке 14 инкрементируется значение letterCount[letter].

По завершении цикла for функция getLetterCount() возвращает словарь letterCount, содержащий счетчики появлений каждой буквы в строке message.

В этой главе мы будем использовать следующую строку (https://en.wikipedia.org/wiki/Alan_Turing).

""""Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist. He was highly influential in the development of computer science, providing a formalisation of the concepts of "algorithm" and "computation" with the Turing machine. Turing is widely considered to be the father of computer science and artificial intelligence. During World War II, Turing worked for the Government Code and Cypher School (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8, the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German ciphers, including the method of the bombe, an electromechanical machine that could find settings for the Enigma machine. After the war he worked at the National Physical Laboratory, where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers and became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical reactions such as the Belousov-Zhabotinsky reaction, which were first observed in the 1960s. Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way he was treated." As of May 2012 a private member's bill was before the House of Lords which would grant Turing a statutory pardon if enacted.""""