---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.90
tokens: 5683
characters: 1668
timestamp: 2025-12-24T07:39:40.969796
finish_reason: stop
---

7. Примеры

Программа sts.chisquare, выполняющая расчет согласно критерию \( \chi^2 \), не выполняет проверку условия \( np_i \geq 5 \). Нужно самим проверить и внести соответствующие поправки.

Получив массив expected_frequencies, распечатываем его содержимое:

expected_frequencies
array([ 2.86897824e-02,  4.36982303e-01,  2.99511125e+00,
        1.21651729e+01,  3.24259666e+01,  5.92667037e+01,
        7.52256801e+01,  6.54733661e+01,  3.73966356e+01,
       1.26577529e+01,  1.92793865e+00])

Имеем: \( np_1 = 12,65775, np_2 = 0,043698, np_3 = 2,995111, np_4 = 12,16517, np_{10} = 12,65775, np_{11} = 1,92794 \). Требуемое неравенство не выполняется для первых трех элементов массива, объединяем их с четвертым; и для предпоследнего элемента, объединяем его с последним.

expected_frequencies_new = expected_frequencies[3:10]
# в новом массиве ожидаемых частот отсутствуют
# первые две и последний элементы старого массива
expected_frequencies_new[0] = np.sum(expected_frequencies[0:4])
# первым элементом нового массива является
# сумма первых четырех элементов старого массива
expected_frequencies_new[6] = np.sum(expected_frequencies[9:11])
# последним элементом нового массива является
# сумма двух последних элементов старого массива

Такие же действия совершаем с массивом observed_frequencies:
observed_frequencies_new = observed_frequencies[3:10]
observed_frequencies_new[0] = np.sum(observed_frequencies[0:4])
observed_frequencies_new[6] = np.sum(observed_frequencies[9:11])
Вызываем функцию st.chisquare:
chisq, p = sts.chisquare(f_obs = observed_frequencies_new, f_exp = expected_frequencies_new, ddof=1)
print('chi2 = ', chisq)
print('p-value =', p)