---
source_image: page_725.png
page_number: 725
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 57.78
tokens: 11734
characters: 2260
timestamp: 2025-12-24T02:08:26.261830
finish_reason: stop
---

Глава 17: примеры HTTP-клиентов из серии flags2

elif all_cc:
    with open(COUNTRY_CODES_FILE) as fp:
        text = fp.read()
        codes.update(text.split())
else:
    for cc in {c.upper() for c in cc_args}:
        if len(cc) == 1 and cc in A_Z:
            codes.update(cc+c for c in A_Z)
        elif len(cc) == 2 and all(c in A_Z for c in cc):
            codes.add(cc)
    else:
        msg = 'each CC argument must be A to Z or AA to ZZ.'
        raise ValueError('*** Usage error: '+msg)
return sorted(codes)[:limit]

def process_args(default_concur_req):
    server_options = ', '.join(sorted(SERVERS))
    parser = argparse.ArgumentParser(
        description='Download flags for country codes. '
        'Default: top 20 countries by population.')
    parser.add_argument('cc', metavar='CC', nargs='*',
        help='country code or 1st letter (eg. B for BA...BZ)')
    parser.add_argument('-a', '--all', action='store_true',
        help='get all available flags (AD to ZW)')
    parser.add_argument('-e', '--every', action='store_true',
        help='get flags for every possible code (AA...ZZ)')
    parser.add_argument('-l', '--limit', metavar='N', type=int,
        help='limit to N first codes', default=sys.maxsize)
    parser.add_argument('-m', '--max_req', metavar='CONCURRENT', type=int,
        default=default_concur_req,
        help='maximum concurrent requests (default={})'.
        format(default_concur_req))
    parser.add_argument('-s', '--server', metavar='LABEL',
        default=DEFAULT_SERVER,
        help='Server to hit; one of {} (default={})'.
        format(server_options, DEFAULT_SERVER))
    parser.add_argument('-v', '--verbose', action='store_true',
        help='output detailed progress info')
    args = parser.parse_args()
    if args.max_req < 1:
        print('*** Usage error: --max_req CONCURRENT must be >= 1')
        parser.print_usage()
        sys.exit(1)
    if args.limit < 1:
        print('*** Usage error: --limit N must be >= 1')
        parser.print_usage()
        sys.exit(1)
    args.server = args.server.upper()
    if args.server not in SERVERS:
        print('*** Usage error: --server LABEL must be one of',
            server_options)
        parser.print_usage()
        sys.exit(1)