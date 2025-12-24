---
source_image: page_360.png
page_number: 360
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.75
tokens: 11693
characters: 1659
timestamp: 2025-12-24T01:51:15.009870
finish_reason: stop
---

_abc_registry, и связывает каждый класс с именем ConcreteTombola, используемым в doctest-скриптах.

Успешный прогон тестового скрипта выглядит следующим образом:

$ python3 tombola_runner.py
BingoCage 23 tests, 0 failed - OK
LotteryBlower 23 tests, 0 failed - OK
TumblingDrum 23 tests, 0 failed - OK
TomboList 23 tests, 0 failed - OK

Сам тестовый скрипт приведен в примере 11.15, а doctest-скрипты — в примере 11.16.

Пример 11.15. tombola_runner.py: исполнитель тестов для подклассов Tombola

import doctest

from tombola import Tombola

# модули, подлежащие тестированию
import bingo, lotto, tombolist, drum

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'

def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()  # Метод __subclasses__() возвращает список непосредственных потомков, находящихся в памяти. Именно поэтому мы сначала импортировали под-
    virtual_subclasses = list(Tombola._abc_registry)

    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)

def test(cls, verbose=False):
    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))

if __name__ == '__main__':
    import sys
    main(sys.argv)

1 Импортируем модули, содержащие настоящие и виртуальные подклассы Tombola, для тестирования.
2 Метод __subclasses__() возвращает список непосредственных потомков, находящихся в памяти. Именно поэтому мы сначала импортировали под-