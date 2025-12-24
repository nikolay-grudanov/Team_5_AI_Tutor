---
source_image: page_229.png
page_number: 229
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.17
tokens: 6182
characters: 1408
timestamp: 2025-12-24T10:07:15.893003
finish_reason: stop
---

var reporting = require('nodeload/lib/reporting')
    , report = reporting.REPORT_MANAGER.getReport('System Usage')
    , memChart = report.getChart('Memory Usage')
    , cpuChart = report.getChart('CPU Usage')
    , loop = require('nodeload/lib/loop')
    , fs = require('fs')
;

Можно видеть, что здесь я определил один отчет ('System Usage') с двумя графиками: 'Memory Usage' (использование памяти) и 'CPU Usage' (использование процессора). Функция getMemory использует файловую систему Linux /proc для получения информации об использовании памяти:

function getMemory() {
    var memData = getProc('meminfo', /\s*kb/i);
    memChart.put({
        'Free Memory': memData['MemFree']
        , 'Free Swap': memData['SwapFree']
    });
    report.summary['Total Memory'] = memData['MemTotal'];
    report.summary['Total Swap'] = memData['SwapTotal'];
}

Конечно, мы можем извлечь любые значения, которые нам нужны. Функция getProc() не показана, она просто берет файл в файловой системе /proc и объектизирует его.

Функция getCPU в целом аналогична функции getMemory, приведенной выше:

function getCPU() {
    var meminfo = fs.readFileSync('/proc/loadavg', 'utf8')
        , vals = meminfo.split(/\s+/)
        , cpuInfo = getProc('cpuinfo')
    ;
    cpuChart.put({
        '1 Min': vals[0]
        , '5 Min': vals[1]
        , '15 Min': vals[2]
    });
    report.summary['CPU'] = cpuInfo['model name'];
}