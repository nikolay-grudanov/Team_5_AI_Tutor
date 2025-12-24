---
source_image: page_158.png
page_number: 158
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.01
tokens: 7607
characters: 1632
timestamp: 2025-12-24T09:14:19.424597
finish_reason: stop
---

Сам по себе стандарт FIPS 202 весьма длинный и читается с трудом, но можно найти реализации с открытым исходным кодом, которые работают довольно быстро, — понять алгоритм, глядя на код, проще, чем читая спецификации. Например, реализация tiny_sha3 (https://github.com/mjosaarinen/tiny_sha3/), распространяемая по лицензии MIT и написанная Маркку-Юхани О. Саариненом, содержит объяснение базового алгоритма Кессак в виде 19 строк кода на C, частично воспроизведенных в листинге 6.9.

Листинг 6.9. Реализация tiny_sha3

static void sha3_keccakf(uint64_t st[25], int rounds)
{
    (⊕)
    for (r = 0; r < rounds; r++) {
        // Theta
        for (i = 0; i < 5; i++)
            bc[i] = st[i] ^ st[i + 5] ^ st[i + 10] ^ st[i + 15] ^ st[i + 20];

        for (i = 0; i < 5; i++) {
            t = bc[(i + 4) % 5] ^ ROTL64(bc[(i + 1) % 5], 1);
            for (j = 0; j < 25; j += 5)
                st[j + i] ^= t;
        }

        // Rho Pi
        t = st[1];
        for (i = 0; i < 24; i++) {
            j = keccakf_piln[i];
            bc[0] = st[j];
            st[j] = ROTL64(t, keccakf_rotc[i]);
            t = bc[0];
        }

        // Chi
        for (j = 0; j < 25; j += 5) {
            for (i = 0; i < 5; i++)
                bc[i] = st[j + i];
            for (i = 0; i < 5; i++)
                st[j + i] ^= (~bc[(i + 1) % 5]) & bc[(i + 2) % 5];
        }

        // Iota
        st[0] ^= keccakf_rndc[r];
    }
    (⊕)
}

Программа tiny_sha3 реализует перестановку P алгоритма Кессак, обратимое преобразование 1600-битового состояния, рассчитываемого как массив двадцати пяти 64-битовых слов. Видно, что в цикле