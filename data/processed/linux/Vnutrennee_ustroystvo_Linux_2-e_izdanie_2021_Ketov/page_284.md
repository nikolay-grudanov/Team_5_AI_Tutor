---
source_image: page_284.png
page_number: 284
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.09
tokens: 7565
characters: 1855
timestamp: 2025-12-24T04:40:14.522625
finish_reason: stop
---

Листинг 6.36. Анализатор пакетов wireshark

lumpy@ubuntu:~$ tshark -i wlp2s0 -V -O http,data-text-lines -Y http port 80
Capturing on wlp2s0

lumpy@ubuntu:~$ curl http://ipinfo.io/city
Saint Petersburg

Frame 4: 131 bytes on wire (1048 bits), 131 bytes captured (1048 bits) on interface 0
Ethernet II, Src: PcsCompu_a9:78:36 (08:00:27:a9:78:36), Dst: RealtekU_12:35:02 (52:54:00:12:35:02)
Internet Protocol Version 4, Src: 10.0.2.15, Dst: 216.239.36.21
Transmission Control Protocol, Src Port: 38534, Dst Port: 80, Seq: 1, Ack: 1, Len: 77
Hypertext Transfer Protocol
    GET /city HTTP/1.1\r\n
        [Expert Info (Chat/Sequence): GET /city HTTP/1.1\r\n]
            [GET /city HTTP/1.1\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Request Method: GET
        Request URI: /city
        Request Version: HTTP/1.1
        Host: ipinfo.io\r\n
        User-Agent: curl/7.65.3\r\n
        Accept: */*\r\n
        \r\n
        [Full request URI: http://ipinfo.io/city]
        [HTTP request 1/1]

Frame 6: 441 bytes on wire (3528 bits), 441 bytes captured (3528 bits) on interface 0
Ethernet II, Src: RealtekU_12:35:02 (52:54:00:12:35:02), Dst: PcsCompu_a9:78:36 (08:00:27:a9:78:36)
Internet Protocol Version 4, Src: 216.239.36.21, Dst: 10.0.2.15
Transmission Control Protocol, Src Port: 80, Dst Port: 38534, Seq: 1, Ack: 78, Len: 387
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        [Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]
            [HTTP/1.1 200 OK\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Response Version: HTTP/1.1
        Status Code: 200
        [Status Code Description: OK]
        Response Phrase: OK
        Date: Sat, 23 Nov 2019 23:27:18 GMT\r\n
        Content-Type: text/html; charset=utf-8\r\n
        Content-Length: 7\r\n
        [Content length: 7]