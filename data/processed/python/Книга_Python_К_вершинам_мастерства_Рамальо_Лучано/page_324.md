---
source_image: page_324.png
page_number: 324
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.87
tokens: 11609
characters: 1546
timestamp: 2025-12-24T01:49:21.466543
finish_reason: stop
---

return bool(abs(self))

def __len__(self):
    return len(self._components)

def __getitem__(self, index):
    cls = type(self)
    if isinstance(index, slice):
        return cls(self._components[index])
    elif isinstance(index, numbers.Integral):
        return self._components[index]
    else:
        msg = '{.__name__} indices must be integers'
        raise TypeError(msg.format(cls))

shortcut_names = 'xyzt'

def __getattr__(self, name):
    cls = type(self)
    if len(name) == 1:
        pos = cls.shortcut_names.find(name)
        if 0 <= pos < len(self._components):
            return self._components[pos]
    msg = '{.__name__!r} object has no attribute {!r}'
    raise AttributeError(msg.format(cls, name))

def angle(self, n): ②
    r = math.sqrt(sum(x * x for x in self[n:]))
    a = math.atan2(r, self[n-1])
    if (n == len(self) - 1) and (self[-1] < 0):
        return math.pi * 2 - a
    else:
        return a

def angles(self): ③
    return (self.angle(n) for n in range(1, len(self)))

def __format__(self, fmt_spec=''): ④
    if fmt_spec.endswith('h'): # hyperspherical coordinates
        fmt_spec = fmt_spec[:-1]
        coords = itertools.chain([abs(self)], self.angles())
        outer_fmt = '<{}>' ⑤
    else:
        coords = self
        outer_fmt = '({})' ⑥
    components = (format(c, fmt_spec) for c in coords) ⑦
    return outer_fmt.format(', '.join(components)) ⑧

@classmethod
def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(memv)