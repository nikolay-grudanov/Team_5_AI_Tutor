---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.33
tokens: 7355
characters: 1051
timestamp: 2025-12-24T09:17:18.589898
finish_reason: stop
---

ментов, включая ANSI X9.42, RFC 2631 и RFC 5114, IEEE 1363 и NIST SP 800-56A. Они обеспечивают интероперабельность и содержат рекомендации о параметрах группы.

Если вы хотите узнать больше о передовых протоколах DH (в частности, MQV и родственных ему HMQV и OAKE) и их аспектах безопасности (например, атаках на разделение неизвестного ключа и атаках на представление группы), прочитайте статью Hugo Krawczyk «HMQV: A High-Performance Secure Diffie–Hellman Protocol» 2005 года (https://eprint.iacr.org/2005/176/) и статью Andrew C. Yao and Yunlei Zhao «A New Family of Implicitly Authenticated Diffie–Hellman Protocols» 2011 года (https://eprint.iacr.org/2011/035/). Обратите внимание, что в этих статьях операции Диффи–Хеллмана записываются не так, как в этой главе. Например, разделяемый секрет представлен в виде xP, а не g^x. Вообще, умножение заменено сложением, а возведение в степень — умножением. Причина в том, что эти протоколы обычно определяются не над группами целых чисел, а над эллиптическими кривыми, о которых пойдет речь в главе 12.