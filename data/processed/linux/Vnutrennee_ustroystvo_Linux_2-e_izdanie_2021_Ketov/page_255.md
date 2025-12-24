---
source_image: page_255.png
page_number: 255
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 66.39
tokens: 8807
characters: 2923
timestamp: 2025-12-24T04:39:50.778448
finish_reason: stop
---

Таблица маршрутизации ядра протокола IP

<table>
  <tr>
    <th>Destination</th>
    <th>Gateway</th>
    <th>Genmask</th>
    <th>Flags Metric Ref Use Iface</th>
  </tr>
  <tr>
    <td>0.0.0.0 ①</td>
    <td>10.0.0.1 ②</td>
    <td>0.0.0.0</td>
    <td>UG 0 0 0 eno1</td>
  </tr>
  <tr>
    <td>10.0.0.0</td>
    <td>0.0.0.0</td>
    <td>255.0.0.0</td>
    <td>U 0 0 0 eno1</td>
  </tr>
  <tr>
    <td>169.254.0.0</td>
    <td>0.0.0.0</td>
    <td>255.255.0.0</td>
    <td>U 1000 0 0 eno1</td>
  </tr>
  <tr>
    <td>172.16.0.0</td>
    <td>0.0.0.0</td>
    <td>255.255.0.0</td>
    <td>U 0 0 0 eno1</td>
  </tr>
</table>

lumpy@ubuntu:~$ ip route show
default ① via 10.0.0.1 ② dev eno1 proto static
10.0.0.0/8 dev eno1 proto kernel scope link src 10.0.0.1
172.16.0.0/16 dev eno1 proto kernel scope link src 172.16.0.1
169.254.0.0/16 dev eno1 scope link metric 1000

③ lumpy@ubuntu:~$ traceroute -m 50 bad.horse
traceroute to bad.horse (162.252.205.157), 30 hops max, 60 byte packets
  1  10.0.0.1 (10.0.0.1)  1.025 ms  1.080 ms  1.236 ms
  22  bad.horse (162.252.205.130)  191.988 ms  191.997 ms  178.848 ms
  23  bad.horse (162.252.205.131)  190.805 ms  195.160 ms  194.807 ms
  24  bad.horse (162.252.205.132)  199.199 ms  187.907 ms  201.063 ms
  25  bad.horse (162.252.205.133)  209.814 ms  203.633 ms  199.866 ms
  26  he.rides.across.the.nation (162.252.205.134)  209.300 ms  204.059 ms  211.089 ms
  27  the.thoroughbred.of.sin (162.252.205.135)  211.454 ms  208.207 ms  212.280 ms
  28  he.got.the.application (162.252.205.136)  208.660 ms  222.452 ms  210.522 ms
  29  that.you.just.sent.in (162.252.205.137)  215.037 ms  223.553 ms  223.043 ms
  30  it.needs.evaluation (162.252.205.138)  229.889 ms  231.036 ms  234.139 ms
  31  so.let.the.games.begin (162.252.205.139)  226.369 ms  230.170 ms  223.952 ms
  32  a.heinous.crime (162.252.205.140)  232.431 ms  231.814 ms  240.990 ms
  33  a.show.of.force (162.252.205.141)  241.706 ms  233.070 ms  272.973 ms
  34  a.murder.would.be.nice.of.course (162.252.205.142)  264.821 ms  239.704 ms  247.930 ms
  35  bad.horse (162.252.205.143)  250.081 ms  244.279 ms  254.147 ms
  36  bad.horse (162.252.205.144)  247.903 ms  258.675 ms  257.366 ms
  37  bad.horse (162.252.205.145)  261.103 ms  253.861 ms  261.307 ms
  38  he-s.bad (162.252.205.146)  267.135 ms  266.860 ms  258.031 ms
  39  the.evil.league.of.evil (162.252.205.147)  262.974 ms  262.773 ms  275.656 ms
  40  is.watching.so.beware (162.252.205.148)  278.567 ms  276.382 ms  277.577 ms
  41  the.grade.that.you.receive (162.252.205.149)  276.158 ms  283.299 ms  284.268 ms
  42  will.be.your.last.we.swear (162.252.205.150)  286.575 ms  286.470 ms  278.213 ms
  43  so.make.the.bad.horse.gleeful (162.252.205.151)  283.040 ms  292.280 ms  290.042 ms
  44  or.he-ll.make.you.his.mare (162.252.205.152)  300.872 ms  299.806 ms  289.688 ms
  45  o_o (162.252.205.153)  294.548 ms  295.458 ms  295.030 ms