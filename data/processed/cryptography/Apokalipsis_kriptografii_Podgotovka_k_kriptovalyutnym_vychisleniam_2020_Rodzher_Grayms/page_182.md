---
source_image: page_182.png
page_number: 182
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.29
tokens: 8085
characters: 2712
timestamp: 2025-12-24T09:06:00.357837
finish_reason: stop
---

Таблица 6.2. Криптографические типы второго тура конкурса NIST

<table>
  <tr>
    <th>Асимметричные шифры / KEM</th>
    <th>Тип</th>
    <th>Подписи</th>
    <th>Тип</th>
  </tr>
  <tr>
    <td>CRYSTAL-Kyber</td>
    <td>Lattice</td>
    <td>CRYSTALS-Dilithium</td>
    <td>Lattice</td>
  </tr>
  <tr>
    <td>FrodoKEM</td>
    <td>Lattice</td>
    <td>FALCON</td>
    <td>Lattice</td>
  </tr>
  <tr>
    <td>LAC</td>
    <td>Lattice</td>
    <td>qTESLA</td>
    <td>Lattice</td>
  </tr>
  <tr>
    <td>NewHope</td>
    <td>Lattice</td>
    <td>SPHINCS+</td>
    <td>Hash</td>
  </tr>
  <tr>
    <td>Three Bears</td>
    <td>Lattice</td>
    <td>GeMSS</td>
    <td>Multivariate</td>
  </tr>
  <tr>
    <td>NTRU</td>
    <td>Lattice</td>
    <td>LUOV</td>
    <td>Multivariate</td>
  </tr>
  <tr>
    <td>NTRU Prime</td>
    <td>Lattice</td>
    <td>MQDSS</td>
    <td>Multivariate</td>
  </tr>
  <tr>
    <td>SABER</td>
    <td>Lattice</td>
    <td>Rainbow</td>
    <td>Multivariate</td>
  </tr>
  <tr>
    <td>Classic McEliece</td>
    <td>Code</td>
    <td>Picnic</td>
    <td>Zero-knowledge proof</td>
  </tr>
  <tr>
    <td>NTS-KEM</td>
    <td>Code</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>BIKE</td>
    <td>Code</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>HQC</td>
    <td>Code</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>LEDAcrypt</td>
    <td>Code</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ROLLO</td>
    <td>Code</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>RQC</td>
    <td>Code</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>SIKE</td>
    <td>Isogeny</td>
    <td></td>
    <td></td>
  </tr>
</table>

Примечание. Lattice – на основе решетки. Code – на основе кода. Isogeny – изогенная. Hash – на основе хеша. Multivariate – многомерная. Zero-knowledge proof – с использованием доказательства нулевого знания.

Квантовоустойчивые асимметричные шифры

Квантовоустойчивые шифры – это криптографические шифры, которые не слишком восприимчивы к квантовым вычислениям с использованием квантовых алгоритмов и, в частности, алгоритма Шора (или любого квантового алгоритма, который может очень быстро вычислять уравнения с простыми числами). Они не используют квантовые свойства, чтобы защититься от атак. Существуют десятки квантовоустойчивых шифров, хотя один или несколько из 17 кандидатов конкурса NIST второго тура асимметричного шифрования, вероятно, станут одним из возможных федеральных стандартов NIST. Асимметричные кандидаты с инфраструктурой PKE и инкапсуляцией KEM второго тура NIST следующие (в алфавитном порядке):

■ BIKE;
■ Classic McEliece;
■ CRYSTALS-Kyber;
■ FrodoKEM;
■ HQC;
■ LAC;
■ LEDAcrypt;
■ NewHope;
■ NTRU;