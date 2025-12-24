---
source_image: page_339.png
page_number: 339
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.75
tokens: 7803
characters: 2018
timestamp: 2025-12-24T08:39:53.072046
finish_reason: stop
---

B8C0D19BB7E17E5CEC6D69D487C0AC3FEDA7E796
B8C0D19BB7E17E5CEC6D69D487C0AC3FEDA7E796
uid                Kalle Rosenbaum <kalle@example.com>
sub    rsa2048 2018-04-27 [E] [expires: 2020-04-26]

Теперь у нас есть свой ключ, который можно использовать для подписания доверенных ключей. Давайте подпишем ключ команды Bitcoin Core:

$ gpg --sign-key 01EA5486DE18A882D4C2684590C8019E36C2E964
pub   rsa4096/90C8019E36C2E964
      created: 2015-06-24 expires: 2019-02-14 usage: SC
      trust: unknown validity: unknown
[ unknown] (1). Wladimir J. van der Laan (Bitcoin Core binary release signing key) <laanwj@gmail.com>
pub   rsa4096/90C8019E36C2E964
      created: 2015-06-24 expires: 2019-02-14 usage: SC
      trust: unknown validity: unknown
Primary key fingerprint: 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964
      Wladimir J. van der Laan (Bitcoin Core binary release signing key) <laanwj@gmail.com>
This key is due to expire on 2019-02-14.
Are you sure that you want to sign this key with your key "Kalle Rosenbaum <kalle@example.com>" (8DC7D3846BA6AB5E)

Really sign? (y/N)

Нажмем клавишу y. Далее будет предложено ввести пароль личного ключа. Введем его и нажмем Enter. Теперь ключ Bitcoin Core будет считаться доверенным. Это упростит процесс обновления узла в будущем.

Посмотрим на вновь подписанный ключ:

$ gpg --list-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
pub   rsa4096 2015-06-24 [SC] [expires: 2019-02-14]
      01EA5486DE18A882D4C2684590C8019E36C2E964
uid        [ full ] Wladimir J. van der Laan (Bitcoin Core binary release signing key) <laanwj@gmail.com>

Найдите слово full в квадратных скобках. Оно означает, что gpg, как и вы, теперь полностью доверяет этому ключу.

Проверка подписи

Настал момент проверить подпись файла SHA256SUMS.asc:

$ gpg --verify SHA256SUMS.asc
gpg: Signature made Wed 03 Oct 2018 10:53:25 AM CEST
gpg:           using RSA key 90C8019E36C2E964
gpg: Good signature from "Wladimir J. van der Laan (Bitcoin Core binary release signing key) <laanwj@gmail.com>" [full]