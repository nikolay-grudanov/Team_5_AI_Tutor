---
source_image: page_226.png
page_number: 226
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 78.27
tokens: 12982
characters: 4709
timestamp: 2025-12-24T05:42:25.870201
finish_reason: stop
---

функциональных символов, входящих в А (множество всех таких термов называют иногда эрбрановским универсумом формулы А).

Если А содержит ∀, то ее эрбрановские развертки — это, по определению, эрбрановские развертки формулы Ф(А).

Заметим, что в случае, когда А — предваренная формула, не все эрбрановские дизъюнкции формулы А (согласно определению на стр. 413—414) являются, согласно нашему определению, ее эрбрановскими развертками. Однако их можно превратить в эрбрановские развертки, добавив недостающие дизъюнктивные члены.

Следующее утверждение — это теорема Эрбрана для произвольных формул.

Теорема 3. Формула А выводима в исчислении предикатов тогда и только тогда, когда некоторая ее эрбрановская развертка выводима (или, что то же самое, общезначима) в исчислении высказываний.

Доказательство. В силу теоремы 2 и определения эрбрановской развертки можно считать, что А не содержит кванторов всеобщности.

(a) Пусть дано доказательство формулы А в G4. Можно считать, что в него входят лишь термы из эрбрановского универсума формулы А (иначе можно было бы заменить термы, начинаяющиеся с лишних функциональных символов, на новую переменную). Запишем полный список этих термов в виде t₁, ..., tₖ. Заменив теперь во всем доказательстве все формулы ∃αBα на B(t₁) V ... VB(tₖ), получим фигуру, которая заканчивается эрбрановской разверткой формулы А и в которой переходы происходят либо по правилам исчисления высказываний, либо по правилу

\[
\frac{\Gamma \rightarrow \Delta, B(t_i)}{\Gamma \rightarrow \Delta, B(t_1) V ... VB(t_k)},
\]

которое достраивается до (серии) → V с помощью утончений.

(b) Если R — произвольная эрбрановская развертка формулы А, то (в рассматриваемом нами случае, когда А не содержит ¬, ∀ и все отрицания находятся перед атомарными формулами), R → A выводимо в исчислении предикатов. Это можно легко доказать, например, индукцией по построению А, используя импликации

((B₁ ⊃ B) & (C₁ ⊃ C)) ⊃ (B₁ & C₁ ⊃ B & C),
((B₁ ⊃ B) & (C₁ ⊃ C)) ⊃ (B₁ VC₁ ⊃ B VC),
(B(t₁) V ... VB(tₖ)) ⊃ ∃αB(α).

R и R ⊃ A дают А.

СПИСОК ЛИТЕРАТУРЫ ¹)

Аддисон (Addison J. W.)
1960. The theory of hierarchies, Logic, methodology and philosophy of science, Proceedings of the 1960 International Congress (Stanford, Aug. 24 — Sept. 2), ed. by Nagel, Suppes and Tarski, Stanford, Calif. (Stanford Univ. Press) 1962, 26—37. [Русский перевод: Теория иерархий, в сб. «Математическая логика и ее применения», М., 1967, 23—36.]

Аддисон, Генкин, Тарский (Addison J. W., Henkin L. Tarski A.)
1965. (редакторы). The theory of models, Proceedings of 1963 the International Symposium at Berkeley, Amsterdam (North-Holland Pub. Co.)

Акерман (Ackermann W.)
1924—5. Begründung des «tertium non datur» mittels der Hilbertschen Theorie der Widerspruchsfreiheit, Math. Ann, 93,1—36.
1940. Zur Widerspruchsfreiheit der Zahlentheorie, Ibid., 117, 162—194.

Амброс, Лазерович (Ambrose A., Lazerowitz M.)
1948. Fundamentals of symbolic logic, New York (Rinehart).

Бар-Хиллел, Перлес, Шамир (Bar-Hillel Y., Perles M., Shamir E.)
1961. On formal properties of simple phase structure grammars, Zeitschrift für Phonetik, Sprachwissenschaft und Kommunikationsforschung, 14, 143—172.

Бахман (Bachmann H.)
1955. Transfinite Zahlen, Ergebnisse der Mathematik und ihrer Grenzgebiete, n. s., no. 1, Berlin, Göttingen and Heidelberg (Springer-Velag).

Бенакерраф, Путнам (Benacerraf P., Putnam H.)
1964. (редакторы) Philosophy of mathematics, selected readings, Englewood Cliffs, N. J., (Prentice-Hall).

Бернайс (Bernays P.)
1937—1954. A system of axiomatic set theory — Parts I—VII, The journal of symbolic logic, 2 (1937), 65—77, 6 (1941), 1—17, 7 (1942), 65—89, 133—145, 8 (1943), 89—106, 13 (1948), 65—79, 19 (1954), 81—96.

Бернайс, Френкель (Bernays P., Fraenkel A. A.)
1958. Axiomatic set theory [монография Бернайса с историческим введением Френкеля], Amsterdam (North-Holland Pub. Co.).

Бернстайн, Робинсон (Bernstein A. R., Robinson A.).
1966. Solution of an invariant subspace problem of K. T. Smith and P. R. Halmos, Pacific journ. of math., 16, 421—431.

Бет (Beth E. W.)
1951. A topological proof of the theorem of Löwenheim-Skolem-Gödel, Koninklijke Nederlandse Akademie van Wetenhappen (Amsterdam), Proceedings, ser. A, 54 (или Indagationes mathematicae, 13), 436—444.
1953. On Padoa's method in the theory of definition, Ibid, 56 (or 15), 330—339.
1955. Semantic entailment and formal derivability, Mededelingen der Koninklijke Nederlandse Akademie van Wetenschappen (Amsterdam), Afd. letterkunde, n. s., 18, no. 13, 309—342.
1959. The foundations of mathematics, Amsterdam (North-Holland Pub. Co.).

¹) ° возле даты указывает, что соответствующая работа добавлена в список литературы при переводе.— Прим. перее.