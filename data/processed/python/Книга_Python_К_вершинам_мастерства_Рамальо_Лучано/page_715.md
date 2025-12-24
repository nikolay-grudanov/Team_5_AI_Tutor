---
source_image: page_715.png
page_number: 715
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.59
tokens: 11800
characters: 2288
timestamp: 2025-12-24T02:07:53.724399
finish_reason: stop
---

Глава 14: скрипт преобразования базы данных isis2json.py

help='output individual records as separate JSON dictionaries, one'
    ' per line for bulk insert to MongoDB via mongoimport utility')
parser.add_argument(
    '-t', '--type', type=int, metavar='ISIS_JSON_TYPE', default=1,
    help='ISIS-JSON type, sets field structure: 1=string, 2=alist,'
        ' 3=dict (default=1)')
parser.add_argument(
    '-q', '--qty', type=int, default=DEFAULT_QTY,
    help='maximum quantity of records to read (default=ALL)')
parser.add_argument(
    '-s', '--skip', type=int, default=0,
    help='records to skip from start of .mst (default=0)')
parser.add_argument(
    '-i', '--id', type=int, metavar='TAG_NUMBER', default=0,
    help='generate an "_id" from the given unique TAG field number'
        ' for each record')
parser.add_argument(
    '-u', '--uuid', action='store_true',
    help='generate an "_id" with a random UUID for each record')
parser.add_argument(
    '-p', '--prefix', type=str, metavar='PREFIX', default='',
    help='concatenate prefix to every numeric field tag'
        ' (ex. 99 becomes "v99")')
parser.add_argument(
    '-n', '--mfn', action='store_true',
    help='generate an "_id" from the MFN of each record'
        ' (available only for .mst input)')
parser.add_argument(
    '-k', '--constant', type=str, metavar='TAG:VALUE', default='',
    help='Include a constant tag:value in every record (ex. -k type:AS)')

# TODO: реализовать следующий флаг для экспорта больших объемов
# данных в CouchDB
parser.add_argument(
    '-r', '--repeat', type=int, default=1,
    help='repeat operation, saving multiple JSON files'
        ' (default=1, use -r 0 to repeat until end of input)')

# разбираем командную строку
args = parser.parse_args()
if args.file_name.lower().endswith('.mst'):
    input_gen_func = iter_mst_records ⑤
else:
    if args.mfn:
        print('UNSUPPORTED: -n/--mfn option only available for .mst input.')
        raise SystemExit
    input_gen_func = iter_iso_records ⑥
input_gen = input_gen_func(args.file_name, args.type) ⑦
if args.couch:
    args.out.write('{ "docs" : ')
    write_json(input_gen, args.file_name, args.out, args.qty, ⑧
        args.skip, args.id, args.uuid, args.mongo, args.mfn,
        args.type, args.prefix, args.constant)