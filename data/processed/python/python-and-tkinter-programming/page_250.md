---
source_image: page_250.png
page_number: 250
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.76
tokens: 8324
characters: 1515
timestamp: 2025-12-24T00:38:19.861233
finish_reason: stop
---

```python
anchor = CENTER,
tags=tag)

def buildRule(self):
    self.canvas.create_line(75,150, 213,150,
        width=1,fill="#333377")
    self.Xincr = 140.0/40.0
    self.X = x = 75
    self.X1 = 213
    y = 150
    lbli = 0

    for i in range(40):
        lbl = ''
        if i in [0,9,19,29,39]:
            h = 6
            lbl = `lbli`
            lbli = lbli + 5
        elif i in [5,14,24,34]:
            h = 4
        else:
            h = 2
        self.canvas.create_line(x,y, x,y-h,
            width=1,fill="#333377")

        if lbl:
            self.canvas.create_text(x, y-5, text=lbl,
                font=("Arial", 6),
                fill="#333377",
                anchor = S),
            x = x + self.Xincr

    def startAnimation(self):
        self.animX = self.X
        self.action = TRUE
        self.root.after(30, self.animate)
```

**Code comments**

1. The test version of our code does not initialize the serial interface:

```python
def __init__(self):
    # Open up the serial port
    pass
```

2. The poll method retrieves a random entry from the TESTDATA list, simulating a poll of the meter:

```python
def poll(self):
    import random
    choice = random.choice(range(0, len(TESTDATA)-1))
    return TESTDATA[choice]
```

3. This section of code illustrates how to arrange for an operation to occur as a background task. The methods buildSymbols and buildScanner are set up to run as callbacks after a few milliseconds.

```python
self.root.after(5, self.buildSymbols)
```