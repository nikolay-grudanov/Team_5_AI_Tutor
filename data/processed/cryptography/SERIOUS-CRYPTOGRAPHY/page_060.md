---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.29
tokens: 7569
characters: 1906
timestamp: 2025-12-24T09:11:21.043257
finish_reason: stop
---

Функция CryptGenRandom() в Windows

В Windows унаследованный интерфейс к системному PRNG, работающий в пространстве пользователя, дает функция СгуртGenRandom() из криптографического (API). В современных версиях Windows функция СгуртGenRandom() заменена функцией ВсгуртGenRandom(), входящей в состав Cryptography API: Next Generation (CNG). В Windows PRNG получает энтропию от драйвера ядра cng.sys (раньше ksecdd.sys), основанного на идеях Fortuna. Как обычно в Windows, процесс получения случайных битов сложен.

В листинге 2.5 показан типичный вызов СгуртGenRandom() из программы на C++ со всеми необходимыми проверками.

Листинг 2.5. Использование интерфейса СгуртGenRandom() к PRNG в Windows

int random_bytes(unsigned char *out, size_t outlen)
{
    static HCRYPTPROV handle = 0; /* освобождается только по завершении */
    /* программы */
    if(!handle) {
        if(!CryptAcquireContext(&handle, 0, 0, PROV_RSA_FULL,
            CRYPT_VERIFYCONTEXT | CRYPT_SILENT)) {
            return -1;
        }
    }
    while(outlen > 0) {
        const DWORD len = outlen > 1048576UL ? 1048576UL : outlen;
        if(!CryptGenRandom(handle, len, out)) {
            return -2;
        }
        out += len;
        outlen -= len;
    }
    return 0;
}

Обратите внимание, что в листинге 2.5 перед обращением к самому PRNG необходимо объявить поставщик служб шифрования (HCYPRT-PROV), а затем получить криптографический контекст с помощью функции СгуртAcquireContext(). Поэтому количество мест, где возможна ошибка, увеличивается. Например, в окончательной версии программы шифрования TrueСгурт не проверялось, завершается ли ошибкой вызов СгуртAcquireContext(), и в результате случайность без ведома пользователя могла оказаться неоптимальной. По счастью, новый интерфейс ВСгуртGenRandom() гораздо проще, в нем не требуется явно открывать описатель (по крайней мере, его легче использовать без описателя).