---
source_image: page_314.png
page_number: 314
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.00
tokens: 8263
characters: 1587
timestamp: 2025-12-24T00:40:06.013469
finish_reason: stop
---

3 The bargraph simply draws a rectangle for the visual.
4 Defining the data is similar to the method for lines. Note that I have omitted the first data point so that it does not overlay the y-axis:
    line1a = GraphBars(data[1:], color='blue', fillstyle='gray25', anchor=0.0)

11.2.2 Pie charts

As Emeril Lagasse* would say, “Let’s kick it up a notch!” Bargraphs were easy to add, and adding pie charts is not much harder. Pie charts seem to have found a niche in management reports, since they convey certain types of information very well. As you will see in figure 11.6, I have added some small details to add a little extra punch. The first is to scale the pie chart if it is drawn in combination with another graph—this prevents the pie chart from getting in the way of the axes (I do not recommend trying to combine pie charts and bar graphs, however). Secondly, if the height and width of the pie chart are unequal, I add a little decoration to give a three-dimensional effect.

There is a problem with Tk release 8.0/8.1. A stipple is ignored for arc items, if present, when running under Windows; the figure was captured under UNIX. Here are the changes to create pie charts:

![Pie charts example](https://i.imgur.com/3Q5z5QG.png)

Figure 11.6 Adding pie charts to the graph widget

* Emeril Lagasse is a popular chef/proprietor of restaurants in New Orleans and Las Vegas in the USA. He is the exuberant host of a regular cable-television cooking show. The audience join Emeril loudly in shouting “Bam! Let’s kick it up a notch!” as he adds his own Essence to his creations.