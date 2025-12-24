---
source_image: page_533.png
page_number: 533
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.81
tokens: 11718
characters: 1660
timestamp: 2025-12-24T01:59:30.284317
finish_reason: stop
---

Пример: три способа загрузки из веба

'MX PH VN ET EG DE IR TR CD FR').split() ②

BASE_URL = 'http://flupy.org/data/flags' ③

DEST_DIR = 'downloads/' ④

def save_flag(img, filename): ⑤
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc): ⑥
    url = '{}/{}{}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content

def show(text): ⑦
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list): ⑧
    for cc in sorted(cc_list): ⑨
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')
    return len(cc_list)

def main(download_many): 10
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))

if __name__ == '__main__':
    main(download_many) ⑪

① Импортируем библиотеку requests; она не входит в состав стандартной библиотеки, поэтому, по принятому соглашению, импортируется после стандартных модулей os, time и sys, а предложение импорта отделяется пустой строкой.
② Список кодов стран (по стандарту ISO 3166) с наибольшим населением, отсортированный в порядке убывания населения.
③ Сайт, откуда загружаются изображения флагов².
④ Локальный каталог, в котором сохраняются изображения.
⑤ Просто копируем img (последовательность байтов) в файл с именем filename в каталоге DEST_DIR.

² Оригиналы изображений взяты из мировой книги фактов ЦРУ (http://1.usa.gov/1JlsmHJ), открытого сайта правительства США. Я скопировал их на свой сайт во избежание непреднамеренной DoS-атаки на сайт CIA.gov.