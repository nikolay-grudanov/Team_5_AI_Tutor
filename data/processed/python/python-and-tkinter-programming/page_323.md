---
source_image: page_323.png
page_number: 323
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.00
tokens: 8164
characters: 1394
timestamp: 2025-12-24T00:40:17.671991
finish_reason: stop
---

The presentation for the strip chart is intended to be similar to an oscilloscope or some other piece of equipment. Normally reverse-video is not the best medium for presenting data; this may be one of the exceptions.

The example code implements a threshold setting which allows the user to set values which trigger an alarm or warning when values are above or below the selected threshold. Take a look at figure 11.10 which shows how thresholds can be set on the data. This data comes from my home airport (Providence, in Warwick, Rhode Island) and it shows data just before a thunderstorm started.

![Figure 11.10 Setting thresholds on data values](https://i.imgur.com/3Q5z5QG.png)

If you look at figure 11.11 you can observe how the cloud base suddenly dropped below 5000 feet and triggered the threshold alarm.

If you do use this example please do not set the update frequency to a high rate. The data on the National Oceanic and Atmospheric Administration (NOAA) website is important for many pilots—leave the bandwidth for them!

11.5 **Summary**

Drawing graphs may not be necessary for many applications, but the ability to generate attractive illustrations from various data sources may be useful in some cases. While there are several general-purpose plotting systems available to generate graphs from arbitrary data, there is something satisfying about creating the code yourself.