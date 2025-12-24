---
source_image: page_049.png
page_number: 49
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 64.89
tokens: 8867
characters: 2693
timestamp: 2025-12-24T00:33:18.687479
finish_reason: stop
---

calc2.py (continued)

def buildCalculator(self):
    FUN = 1                # A Function
    KEY = 0                # A Key
    KC1 = 'gray30'         # Dark Keys
    KC2 = 'gray50'         # Light Keys
    KC3 = 'steelblue1'     # Light Blue Key
    KC4 = 'steelblue'      # Dark Blue Key
    keys = [
        [('2nd',   '',   '',   KC3, FUN, 'second'),   # Row 1
         ('Mode',  'Quit',  '',  KC1, FUN, 'mode'),
         ('Del',   'Ins',   '',  KC1, FUN, 'delete'),
         ('Alpha','Lock',   '',  KC2, FUN, 'alpha'),
         ('Stat',  'List',   '',  KC1, FUN, 'stat')],
        [('Math',  'Test',  'A',  KC1, FUN, 'math'),   # Row 2
         ('Mtrx',  'Angle','B',  KC1, FUN, 'matrix'),
         ('Prgm',  'Draw',  'C',  KC1, FUN, 'program'),
         ('Vars',  'YVars',' ',  KC1, FUN, 'vars'),
         ('Clr',   '',     '',   KC1, FUN, 'clear')],
        [('X-1',   'Abs',   'D',  KC1, FUN, 'X1'),      # Row 3
         ('Sin',   'Sin-1','E',  KC1, FUN, 'sin'),
         ('Cos',   'Cos-1','F',  KC1, FUN, 'cos'),
         ('Tan',   'Tan-1','G',  KC1, FUN, 'tan'),
         ('^',     'PI',    'H',  KC1, FUN, 'up')],
        [('X2',    'Root',  'I',  KC1, FUN, 'X2'),       # Row 4
         (',',     'EE',    'J',  KC1, KEY, ',' ),
         ('(',     '{',     'K',  KC1, KEY, '(' ),
         (')',     '}',     'L',  KC1, KEY, ')' ),
         ('/',     'M',     'M',  KC4, KEY, '/')],
        [('Log',   '10x',   'N',  KC1, FUN, 'log'),      # Row 5
         ('7',     'Un-1',  'O',  KC2, KEY, '7'),
         ('8',     'Vn-1',  'P',  KC2, KEY, '8'),
         ('9',     'n',     'Q',  KC2, KEY, '9'),
         ('X',     '[',     'R',  KC4, KEY, '*')],
        [('Ln',    'ex',    'S',  KC1, FUN, 'ln'),       # Row 6
         ('4',     'L4',    'T',  KC2, KEY, '4'),
         ('5',     'L5',    'U',  KC2, KEY, '5'),
         ('6',     'L6',    'V',  KC2, KEY, '6'),
         ('-',     ']',     'W',  KC4, KEY, '-')],
        [('STO',   'RCL',   'X',  KC1, FUN, 'store'),    # Row 7
         ('1',     'L1',    'Y',  KC2, KEY, '1'),
         ('2',     'L2',    'Z',  KC2, KEY, '2'),
         ('3',     'L3',    '',   KC2, KEY, '3'),
         ('+',     'MEM',   '"',  KC4, KEY, '+')],
        [('Off',   '',      '',   KC1, FUN, 'off'),      # Row 8
         ('0',     '',      '',   KC2, KEY, '0'),
         (':',     ':',     '',   KC2, KEY, ':'),
         ('(-)',   'ANS',   '?',  KC2, FUN, 'neg'),
         ('Enter','Entry','','',  KC4, FUN, 'enter')]]
    self.display = Pmw.ScrolledText(self, hscrollmode='dynamic',
                                    vscrollmode='dynamic', hull_relief='sunken',
                                    hull_background='gray40', hull_borderwidth=10,