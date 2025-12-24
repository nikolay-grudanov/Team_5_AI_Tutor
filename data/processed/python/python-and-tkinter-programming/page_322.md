---
source_image: page_322.png
page_number: 322
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.00
tokens: 8316
characters: 2096
timestamp: 2025-12-24T00:40:25.657171
finish_reason: stop
---

the data is made available or polled at some time interval, and then they reset the chart when the maximum space has been filled.

Strip charts are an ideal medium for displaying performance data; data from sensors, such as temperature, speed, or humidity; data from more abstract measurements (such as the average number of items purchased per hour by each customer in a grocery store); and other types of data. They also can be used as a means of setting thresholds and triggering alarms when those thresholds have been reached.

The final example implements a weather monitoring system utilizing METAR* data. This encoded data may be obtained via FTP from the National Weather Service in the United States and from similar authorities around the globe. We are not going to enter a long tutorial about how to decode METARs, since that would require a chapter of its own. For this example, I am not even going to present the source code (there is really too much to use the space on the printed page). The source code is available online and it may be examined to determine how a simple FTP poll may be made to gather data continuously.

Take a look at figure 11.9 which shows the results of collecting the data from Tampa Bay, Florida (station KTPA), for about nine hours, starting at about 8:00 a.m. EST. The graphs depict temperature, humidity, altimeter (atmospheric pressure), visibility, wind speed, wind direction, clouds over 10,000 feet and clouds under 25,000 feet.

![Figure 11.9 Strip chart display with polled meteorological data](https://i.imgur.com/3Q5z5QG.png)

Figure 11.9 Strip chart display with polled meteorological data

* If you are a weather buff or a private pilot, you will be familiar with the automated, encoded weather observations that are posted at many reporting stations, including major airports, around the world. Updated on an hourly basis (more frequently if there are rapid changes in conditions), they contain details of wind direction and speed, temperature, dewpoints, atmospheric pressure, cloud cover and other data important to aviation in particular.