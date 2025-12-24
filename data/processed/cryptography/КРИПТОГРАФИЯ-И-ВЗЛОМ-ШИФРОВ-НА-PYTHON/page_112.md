---
source_image: page_112.png
page_number: 112
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.13
tokens: 7592
characters: 1528
timestamp: 2025-12-24T08:48:52.791310
finish_reason: stop
---

19. translatedIndex = symbolIndex - key
20.
21. # Обработка "заворачивания"
22. if translatedIndex < 0:
23.     translatedIndex = translatedIndex + len(SYMBOLS)
24.
25. # Присоединить дешифрованный символ
26. translated = translated + SYMBOLS[translatedIndex]
27.
28. else:
29.     # Присоединить символ без шифрования/дешифрования
30.     translated = translated + symbol
31.
32. # Отобразить каждый возможный вариант расшифровки
33. print('Key #%s: %s' % (key, translated))

Обратите внимание на то, что значительная часть программы совпадает с исходной программой шифрования на основе шифра Цезаря. Это объясняется тем, что программа взлома шифра Цезаря использует те же действия для дешифрования сообщений.

Пример выполнения программы Caesar Hacker

Выполнив программу взлома шифра Цезаря, вы должны получить приведенный ниже результат. Программа взламывает зашифрованный текст guv6Jv6Jz!J6rp5r7Jzr66ntrM, поочередно используя все 66 возможных значений ключей.

Key #0: guv6Jv6Jz!J6rp5r7Jzr66ntrM
Key #1: ftu5Iu5Iy I5qo4q6Iyq55msqL
Key #2: est4Ht4Hx0H4pn3p5Hxp44lrpK
Key #3: drs3Gs3Gw9G3om2o4Gwo33kqoJ
Key #4: cqr2Fr2Fv8F2nl1n3Fvn22jpnI
--пропущено--
Key #11: Vjku?ku?ol?ugetgv?oguucigB
Key #12: Uijt!jt!nz!tfdsfu!nfttbhfA
Key #13: This is my secret message.
Key #14: Sghr0hr0lx0rdbqds0ldrrZfd?
Key #15: Rfgq9gq9kw9qcapcr9kcqqYec!
--пропущено--
Key #61: lz1 01 O5CO wu0w!O5w sywR
Key #62: kyz0Nz0N4BN0vt9v N4v00rxvQ
Key #63: jxy9My9M3AM9us8u0M3u99qwup
Key #64: iwx8Lx8L2.L8tr7t9L2t88pvtO
Key #65: hvw7Kw7K1?K7sq6s8K1s77ousN