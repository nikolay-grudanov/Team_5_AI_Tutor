---
source_image: page_276.png
page_number: 276
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.43
tokens: 6409
characters: 1734
timestamp: 2025-12-24T10:08:24.571597
finish_reason: stop
---

На рис. 7.30 можно уже наблюдать деминифицированную версию кода нашей функции итератора. Эта версия уже менее уродлива, но имена переменных все еще не соответствуют нашему исходному коду, а номера строк отличаются от номеров строк в исходном файле. Вот тут-то нам и помогут карты кода! Прежде всего, нужно указать Closure Compiler, что нужно создать карту кода (все в одной строке):

% java -jar compiler.jar --js iterator.js --js_output_file it-comp.js --create_source_map ./it-min.js.map --source_map_format=V3

В результате мы получим файл с картой источника, it-min.js.map, содержащий гигантский JSON-объект:

{
"version":3,
"file":"it-comp.js",
"lineCount":1,
"mappings":"AAAAA,QAASA,YAAW,CAACC,CAAD,CAAUC,CAAV,CAAmBC,CAAAnB,CAA2B,CAE3C,IAAAF,EAAUA,CAAVA,EAAqB,CAAkB,CACAC,EAAUA,CAAVA,EAAqB,CADrB,CAEAC,EAASA,CAATA,EAAmB,GAFnB,CAIIC,EAAUF,CAJd,CAKMG,EAAMA,QAAQ,EAAG,CACfD,CAAA,EAAWH,CACX,OAAQG,EAAA,CAAUD,CAA,CAAoBG,GAApB,CAA0BF,CAFnB,CAMvBC,EAAAE,YAAA,CAAkB,gBAAIB,CAAqCL,CAAkC,CAA+C,SAA/C,CAA2DC,CAA3D,CAAoE,MAApE,CAA6EF,CAE7E,OAAOI,EAfoC;",
"sources":["iterator.js"],
"names":["getIterator","countBy","startAt","upTill","current","ret","NaN","displayName"]
}

Суть этого объекта — свойство mappings, которое является Base64 VLQ-закодированной строкой. При желании, в Интернете вы найдете много информации по этому кодированию.

Последнее действие заключается в том, чтобы связать созданную карту кода с JavaScript-кодом, поданным браузеру. Для этого нужно указать отладчику, где найти соответствующую карту:

function getIterator(a,b,c){var a=all1,b=b||0,c=c||100,d=b,e=function(){d+=a;return d>c?NaN:d};
e.displayName="Iterator from "+b+" until "+c+" by "+a;return e;
//@ sourceMappingURL=file:///Users/trostler/it-min.js.map