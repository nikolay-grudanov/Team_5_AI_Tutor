---
source_image: page_252.png
page_number: 252
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.62
tokens: 8266
characters: 1525
timestamp: 2025-12-24T00:38:19.739681
finish_reason: stop
---

matchlist = self.primary_lookup[tag]
if not matchlist: return None
gotIndex = None
gotOpenLine = FALSE
for hasr, rfmt, un, sec in matchlist:
    if hasr and (string.find(val, 'L') >= 0):
        if rfmt == string.strip(val):
            gotIndex = sec
            gotOpenLine = TRUE
    else:
        decimal = string.find(val, '.')
        if decimal > 0:
            if rfmt == `decimal`:
                gotIndex = sec
        else:
            if not rfmt: # No decimals
                gotIndex = sec
    if gotIndex:
        if not string.strip(units) == string.strip(un):
            gotIndex = None
    if gotIndex:
        break
return (gotIndex, gotOpenLine)

def updateDisplay(self, result):
    self.canvas.delete('display')
    tag   = result[:2]
    val   = result[3:9]
    units = result [9:13]
    # display the hold value
    redraw = FALSE
    try:
        hold = string.atof(self.holdVal)
        nval = string.atof(val)
        if hold <= 0.0:
            if nval < 0.0:
                if nval < hold:
                    self.holdVal = val
                    redraw = TRUE
            else:
                hold = 0.0
        if hold >= 0.0 and not redraw:
            if nval >= 0.0:
                if nval > hold:
                    self.holdVal = val
                    redraw = TRUE
            else:
                self.holdVal = '0.0'
                redraw = TRUE
    except ValueError:
        self.holdVal = '0.0'
        redraw = TRUE

    if redraw:
        self.canvas.delete('holdval')