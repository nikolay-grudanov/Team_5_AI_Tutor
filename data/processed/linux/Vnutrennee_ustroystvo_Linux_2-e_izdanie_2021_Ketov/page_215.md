---
source_image: page_215.png
page_number: 215
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 59.00
tokens: 8237
characters: 2818
timestamp: 2025-12-24T04:38:34.103231
finish_reason: stop
---

В менее тривиальных случаях, как в примере 1 из листинга 5.32, попытка выполнения команды find(1) с вполне валидными аргументами приводит к неожиданным и странным результатам. В режиме трассировки команд интерпретатора становится очевидно, что шаблонное выражение *.gz, предназначавшееся самой команде поиска файлов, было подставлено интерпретатором до запуска команды, что привело ее в недоумение. Для правильной передачи шаблонных выражений самим командам их следует экранировать, как в примере 2.

Листинг 5.32. Экранирование шаблонных выражений

1 bender@ubuntu:~$ find . -name *.gz
find: paths must precede expression: 'plan9.iso.gz'
find: possible unquoted pattern after predicate '-name'?
bender@ubuntu:~$ set -x
bender@ubuntu:~$ find . -name *.gz ③
+ find . -name dvd.iso.gz plan9.iso.gz
①↑ ②↑ ?↑
find: paths ① must precede expression ②: 'plan9.iso.gz'
find: possible unquoted ③ pattern after predicate '-name'?

2 bender@ubuntu:~$ find . -name "*.gz"
+ find . -name '*.gz'
./dvd.iso.gz
./plan9.iso.gz

Аналогично, в примере 1 из листинга 5.33 при попытке скачивания с Web-сервера ресурса со сложным W:[URL] при помощи команды wget(1) командный интерпретатор постарался разбить команду на список заданий, встретив метасимвол &, формирующий асинхронные задания (см. разд. 4.8.1). Для правильной передачи строк, содержащих метасимволы, их следует экранировать, как в примере 2.

Листинг 5.33. Экранирование символов списка команд &

bender@ubuntu:~$ youtube-dl -g https://www.youtube.com/watch?v=n1F_MfLRLX0
https://r4---sn-n3toxu-axqe.googlevideo.com/videoplayback?expire=1574532639&ei=vyHZXfo3kp3JBFwBqzg&ip=93.100.207.82&id=o-ABldbr46QqdVsKX_53HJb4sbFnPU60Ki_oStnK0vfARv&itag=136&aitag=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-n3toxu-axqe%2Csn-axq7sn7s&ms=au%2Crdu&mv=m&mvi=3&pl=23&nh=%2CIgpwcjAyLnxLZDAzKgkxMjcuMC4wLjE&initcwndbps=1630000&mime=video%2Fmp4&glr=yes&clen=380099033&dur=5496.290&lmt=1540876699100611&mt=1574510962&fvip=4&keepalive=yes&fexp=23842630&beids=9466585&c=WEB&txp=5432432&sparms=expire%2Cet%2Cip%2Cld%2Caitag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ALgxI2wwRgIhAIDBEEOHhkBBZZoFPqTEUrbzgQQ-7BR0dfzBSl9Tws2AiEAmF6e8aCTtR2L2YcBZRIGACeUnoVuB5cPlSo-l6iJHGUX3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cwi%2Cpl%2Cnh%2Cinitcwndbps&lsig=AHylm14wRQIhAPjk5c57desGzTSVx4QPsoTAsg6wtyZShvGeCmwojtnJAIaA8fkeGc76lPA-USegzGJCzc4qvvlUMF763x1u5yXSvXQ%30%3D&ratebypass=yes

1 bender@ubuntu:~$ wget https://r4---sn-n3toxu-axqe.googlevideo.com/videoplayback?expire=1574532639&ei=vyHZXfo3kp3JBFwBqzg&ip=93.100.207.82&id=o-ABldbr46QqdVsKX_53HJb4sbFnPU60Ki_oStnK0vfARv&itag=136&aitag=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-n3toxu-axqe%2Csn-axq7sn7s&ms=au%2Crdu&mv=m&mvi=3&pl=