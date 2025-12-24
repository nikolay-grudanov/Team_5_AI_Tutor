---
source_image: page_135.png
page_number: 135
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.65
tokens: 7218
characters: 1300
timestamp: 2025-12-24T02:37:23.985415
finish_reason: stop
---

for fin in self.files:
    logging.debug('catting {0}'.format(fin))
    for count, line in enumerate(fin, 1):
        if self.show_numbers:
            fout.write(fmt.format(
                count, line))
        else:
            fout.write(line)

def main(args):
    """
    Логика выполнения cat с аргументами
    """
    parser = argparse.ArgumentParser(
        description='Concatenate FILE(s), or '
        'standard input, to standard output')
    parser.add_argument('--version',
        action='version', version=__version__)
    parser.add_argument('-n', '--number',
        action='store_true',
        help='number all output lines')
    parser.add_argument('files', nargs='*',
        type=argparse.FileType('r'),
        default=[sys.stdin], metavar='FILE')
    parser.add_argument('--run-tests',
        action='store_true',
        help='run module tests')
    args = parser.parse_args(args)

    if args.run_tests:
        import doctest
        doctest.testmod()
    else:
        cat = Catter(args.files, args.number)
        cat.run(sys.stdout)
        logging.debug('done catting')

    if __name__ == '__main__':
        main(sys.argv[1:])

Если вам не хочется вводить весь этот код вручную, загрузите его копию из интернета¹.

¹ https://github.com/mattharrison/IllustratedPy3/