---
source_image: page_383.png
page_number: 383
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 99.44
tokens: 9794
characters: 4464
timestamp: 2025-12-24T00:43:22.217124
finish_reason: stop
---

When the application exits from start, the profiler prints a report on all the functions and execution times. Let’s take a look at one of the earlier examples in the book. In “Speed drawing” on page 271, we developed a fractal program. This is highly compute-bound, but we can probably make some improvements. To profile the code, we just add the additional profiler statements:

if __name__ == '__main__':
    def start():
        fractal = Fractal()
        fractal.root.after(10, fractal.createImage())
        fractal.run()

import profile
profile.run('start()')

When you exit the application, a screenful of statistics fly by—you will have to redirect the output to read it! Part of the output is shown here:

655511 function calls (655491 primitive calls) in 419.062 CPU seconds
Ordered by: standard name

<table>
  <tr>
    <th>ncalls</th>
    <th>tottime</th>
    <th>percall</th>
    <th>cumtime</th>
    <th>percall</th>
    <th>filename:lineno(function)</th>
  </tr>
  <tr>
    <td>2</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.003</td>
    <td>0.002</td>
    <td>&lt;string&gt;:1(after)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.001</td>
    <td>0.001</td>
    <td>&lt;string&gt;:1(after_cancel)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.002</td>
    <td>0.002</td>
    <td>&lt;string&gt;:1(after_idle)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.001</td>
    <td>0.001</td>
    <td>&lt;string&gt;:1(bind)</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.003</td>
    <td>0.002</td>
    <td>&lt;string&gt;:1(bind_class)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>&lt;string&gt;:1(focus_set)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>20.476</td>
    <td>20.476</td>
    <td>&lt;string&gt;:1(mainloop)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.001</td>
    <td>0.001</td>
    <td>&lt;string&gt;:1(overridedirect)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>ImageDraw.py:24(__init__)</td>
  </tr>
  <tr>
    <td>214194</td>
    <td>22.624</td>
    <td>0.000</td>
    <td>22.624</td>
    <td>0.000</td>
    <td><b>ImageDraw.py:34(setink)</b></td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>ImageDraw.py:39(setfill)</td>
  </tr>
  <tr>
    <td>214194</td>
    <td>20.578</td>
    <td>0.000</td>
    <td>20.578</td>
    <td>0.000</td>
    <td><b>ImageDraw.py:51(point)</b></td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.152</td>
    <td>0.152</td>
    <td>0.152</td>
    <td>0.152</td>
    <td>ImageFile.py:194(_save)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.465</td>
    <td>0.465</td>
    <td>p_fractal.py:55(initData)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>287.474</td>
    <td>287.474</td>
    <td>394.599</td>
    <td>394.599</td>
    <td><b>p_fractal.py:65(createImage)</b></td>
  </tr>
  <tr>
    <td>1</td>
    <td>0.135</td>
    <td>0.135</td>
    <td>0.135</td>
    <td>0.135</td>
    <td>p_fractal.py:8(getpalette)</td>
  </tr>
  <tr>
    <td>214194</td>
    <td>49.528</td>
    <td>0.000</td>
    <td>92.730</td>
    <td>0.000</td>
    <td><b>p_fractal.py:96(pixel)</b></td>
  </tr>
  <tr>
    <td>0</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>0.000</td>
    <td>profile:0(profiler)</td>
  </tr>
</table>

You can see three routines that are called over 200,000 times each, and notice that almost all the time is spent in createImage (which is not surprising). However, there is really too much output in a default run to be very useful.

Fortunately, the profiler can also be run in a mode where the statistics are collected in a file which may be analyzed at your leisure. You also have considerable control over the output format. To illustrate this, we need to make a small modification. In this case we will print the entries for the 20 top cumulative times:

import profile
profile.run('start()', 'profile_results')

import pstats
p = pstats.Stats('profile_results')
p.sort_stats('cumulative').print_stats(20)

Now, when we run p_fractal.py again, we get the following output when the application exits: