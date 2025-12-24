---
source_image: page_163.png
page_number: 163
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.00
tokens: 7531
characters: 1702
timestamp: 2025-12-24T09:14:29.012094
finish_reason: stop
---

Для дополнительного чтения

Если вы хотите больше узнать о функциях хеширования, почитайте классические работы 1980-х и 1990-х годов, например Ralph Merkle «One Way Hash Functions and DES» и Ivan Dåmgerd «A Design Principle for Hash Functions». Кроме того, познакомьтесь с первым полным исследованием хеширования на основе блочных шифров: Preneel, Govaerts, and Vandewalle «Hash Functions Based on Block Ciphers: A Synthetic Approach».

Дополнительные сведения о поиске коллизий имеются в статье van Oorschot and Wiener «Parallel Collision Search with Cryptanalytic Applications», вышедшей в 1997 году. Чтобы больше узнать о теоретических основах стойкости к коллизиям и восстановлении прообраза, а также об атаках удлинением сообщения, поищите в сети по ключевому слову indifferentiability (неразличимость).

Более поздние исследования по хеш-функциям см. в архивах конкурса на звание SHA-3, где имеются описания всех поданных на конкурс алгоритмов и их взлома. Много ссылок можно найти на сайте SHA-3 Zoo по адресу http://ehash.iaik.tugraz.at/wiki/The_SHA-3_Zoo и на странице NIST http://csrc.nist.gov/groups/ST/hash/sha-3/.

Дополнительные сведения о победителе конкурса на звание SHA-3, Кессак, и функциях губки см. на официальных страницах авторов Кессак http://keccak.noekeon.org/ и http://sponge.noekeon.org/.

И наконец, поинтересуйтесь следующими двумя примерами эксплуатации слабых хеш-функций:

• компьютерный червь Flame, эксплуатируя коллизию в MD5, создавал поддельный сертификат и притворялся легитимной программой;
• в игровой консоли Xbox для построения хеш-функции использовался слабый блочный шифр ТЕА. Это было использовано для взлома консоли и выполнения на ней произвольного кода.