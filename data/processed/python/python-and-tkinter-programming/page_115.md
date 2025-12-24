---
source_image: page_115.png
page_number: 115
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.20
tokens: 8187
characters: 1330
timestamp: 2025-12-24T00:34:27.589622
finish_reason: stop
---

You have already seen one example of the ImageEditor in use (figure 5.17). The real advantage of the grid geometry manager becomes apparent when you run the application with another image with a different aspect. Figure 5.20 shows this well; the grid adjusts perfectly to the image. Creating a similar effect using the Packer would require greater effort.

![ImageEditor—scales for image size](https://i.imgur.com/3Q5z5QG.png)

Figure 5.19 ImageEditor—scales for image size

5.4 Placer

![A simple scrapbook tool](https://i.imgur.com/3Q5z5QG.png)

Figure 5.20 A simple scrapbook tool

The Placer geometry manager is the simplest of the available managers in Tkinter. It is considered difficult to use by some programmers, because it allows precise positioning of widgets within, or relative to, a window. You will find quite a few examples of its use in this book so I could take advantage of this precision. Look ahead to figure 9.5 on page 213 to see an example of a GUI that would be fairly difficult to implement using pack or grid. Because we will see so many examples, I am only going to present two simple examples here.

Let’s start by creating the simple scrapbook window shown in figure 5.21. Its function is to display some images, which are scaled to fit the window. The images are selected by clicking on the numbered