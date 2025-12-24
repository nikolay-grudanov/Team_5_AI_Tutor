---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 77.81
tokens: 8668
characters: 3593
timestamp: 2025-12-24T00:57:25.772974
finish_reason: stop
---

In[17]: for (method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))

Astrometry                shape=(2, 6)
Eclipse Timing Variations  shape=(9, 6)
Imaging                    shape=(38, 6)
Microlensing               shape=(23, 6)
Orbital Brightness Modulation  shape=(3, 6)
Pulsar Timing              shape=(5, 6)
Pulsation Timing Variations shape=(1, 6)
Radial Velocity            shape=(553, 6)
Transit                    shape=(397, 6)
Transit Timing Variations   shape=(4, 6)

Это может пригодиться для выполнения некоторых вещей вручную, хотя обычно быстрее воспользоваться встроенной функциональностью apply.

Методы диспетчеризации. Благодаря определенной магии классов языка Python все методы, не реализованные явным образом объектом GroupBy, будут передаваться далее и выполняться для групп, вне зависимости от того, являются ли они объектами Series или DataFrame. Например, можно использовать метод describe() объекта DataFrame для вычисления набора сводных показателей, описывающих каждую группу в данных:

In[18]: planets.groupby('method')['year'].describe().unstack()

Out[18]:

<table>
  <tr>
    <th> </th>
    <th>count</th>
    <th>mean</th>
    <th>std</th>
    <th>min</th>
    <th>25%</th>
    <th>50%</th>
    <th>75%</th>
    <th>max</th>
  </tr>
  <tr>
    <th>method</th>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Astrometry</td>
    <td>2.0</td>
    <td>2011.500000</td>
    <td>2.121320</td>
    <td>2010.0</td>
    <td>2010.75</td>
    <td>2011.5</td>
    <td>2012.25</td>
    <td>2013.0</td>
  </tr>
  <tr>
    <td>Eclipse Timing Variations</td>
    <td>9.0</td>
    <td>2010.000000</td>
    <td>1.414214</td>
    <td>2008.0</td>
    <td>2009.00</td>
    <td>2010.0</td>
    <td>2011.00</td>
    <td>2012.0</td>
  </tr>
  <tr>
    <td>Imaging</td>
    <td>38.0</td>
    <td>2009.131579</td>
    <td>2.781901</td>
    <td>2004.0</td>
    <td>2008.00</td>
    <td>2009.0</td>
    <td>2011.00</td>
    <td>2013.0</td>
  </tr>
  <tr>
    <td>Microlensing</td>
    <td>23.0</td>
    <td>2009.782609</td>
    <td>2.859697</td>
    <td>2004.0</td>
    <td>2008.00</td>
    <td>2009.0</td>
    <td>2011.00</td>
    <td>2013.0</td>
  </tr>
  <tr>
    <td>Orbital Brightness Modulation</td>
    <td>3.0</td>
    <td>2011.666667</td>
    <td>1.154701</td>
    <td>2011.0</td>
    <td>2011.00</td>
    <td>2011.0</td>
    <td>2012.0</td>
    <td>2013.0</td>
  </tr>
  <tr>
    <td>Pulsar Timing</td>
    <td>5.0</td>
    <td>1998.400000</td>
    <td>8.384510</td>
    <td>1992.0</td>
    <td>1992.00</td>
    <td>1994.0</td>
    <td>2003.00</td>
    <td>2011.0</td>
  </tr>
  <tr>
    <td>Pulsation Timing Variations</td>
    <td>1.0</td>
    <td>2007.000000</td>
    <td>NaN</td>
    <td>2007.0</td>
    <td>2007.00</td>
    <td>2007.0</td>
    <td>2007.00</td>
    <td>2007.0</td>
  </tr>
  <tr>
    <td>Radial Velocity</td>
    <td>553.0</td>
    <td>2007.518987</td>
    <td>4.249052</td>
    <td>1989.0</td>
    <td>2005.00</td>
    <td>2009.0</td>
    <td>2011.00</td>
    <td>2013.0</td>
  </tr>
  <tr>
    <td>Transit</td>
    <td>397.0</td>
    <td>2011.236776</td>
    <td>2.077867</td>
    <td>2002.0</td>
    <td>2010.00</td>
    <td>2012.0</td>
    <td>2013.00</td>
    <td>2014.0</td>
  </tr>
  <tr>
    <td>Transit Timing Variations</td>
    <td>4.0</td>
    <td>2012.500000</td>
    <td>1.290994</td>
    <td>2011.0</td>
    <td>2011.75</td>
    <td>2012.5</td>
    <td>2013.25</td>
    <td>2014.0</td>
  </tr>
</table>