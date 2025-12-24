---
source_image: page_004.png
page_number: 4
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.72
tokens: 3653
characters: 2224
timestamp: 2025-12-23T22:41:21.699424
finish_reason: stop
---

Класс \( B_2 \):
\[
F(x) \sim a|x|^{-\Delta}, \quad f(x) \sim a\Delta|x|^{-\Delta-1} \text{ при } x \to -\infty, \ a, \Delta > 0,
\]
\[
d_{n,t} = -(a n^{1-\alpha}/t)^{1/\Delta}, \quad c_{n,t} = a^{1/\Delta}/(\Delta t^{(2+\Delta)/(2\Delta)} n^{-(1-\alpha)/\Delta+\alpha/2}).
\]

Класс \( B_3 \):
\[
F(x) \sim a(x-z_F)^{\Delta}, \quad f(x) \sim a\Delta(x-z_F)^{\Delta-1} \text{ при } x \to z_F, \ -\infty < z_F < \infty, \ a, \Delta > 0,
\]
\[
d_{n,t} = z_F + (a n^{1-\alpha}/t)^{-1/\Delta}, \quad c_{n,t} = 1/(\Delta a^{1/\Delta} t^{(\Delta-2)/(2\Delta)} n^{(1-\alpha)/\Delta+\alpha/2}).
\]

При \( n \to \infty \) для всех трех классов \( B_1, B_2 \) и \( B_3 \) предельным распределением статистики \( (X_{[t n^{\alpha}] - d_{n,t}}^{(n)})/c_{n,t} \) является стандартное нормальное распределение. Для классов \( B_1 \) и \( B_3 \) условие (3) выполняется, а для класса \( B_2 \) это условие справедливо только при \( 2/(2+\Delta) \leq \alpha < 1 \). Следовательно, для класса \( B_2 \) теорема верна лишь при указанном ограничении на параметр \( \alpha \).

СПИСОК ЛИТЕРАТУРЫ

1. Смирнов Н.В. Предельные законы распределения для членов вариационного ряда // Тр. МИАН им. В.А. Стеклова. 1949. 25. С. 5–59.
2. Смирнов Н.В. О сходимости к нормальному закону распределений членов вариационного ряда // Известия АН УзССР. 1966. 3. С. 24–32.
3. Чибисов Д.М. О предельных распределениях для членов вариационного ряда // Теория вероятн. и примен. 1964. 9. № 1. С. 159–163.
4. Wu C. The types of limit distributions for some terms of variational series // Sci. Sinica. 1966. 15. P. 749–762.
5. Mosteller F. On some useful “inefficient” statistics // Ann. Math. Statist. 1946. 17. P. 377–408.
6. Cooil B. Limiting multivariate distributions of intermediate order statistics // Ann. Probab. 1985. 13. N 2. P. 469–477.
7. Watts V., Rootsen H., Leadbetter M. On limiting distributions of intermediate order statistics from stationary sequences // Ann. Probab. 1982. 10. P. 653–662.
8. Пагурова В.И. О предельном распределении порядковых статистик в выборке случайного объема // Вестн. Моск. ун-та. Сер. 15. Вычисл. матем. и киберн. 2016. № 4. С. 16–19.
9. Дэйвид Г. Порядковые статистики. М.: Наука, 1979.

Поступила в редакцию 13.02.17