---
source_image: page_126.png
page_number: 126
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.04
tokens: 8211
characters: 1437
timestamp: 2025-12-24T00:34:41.172577
finish_reason: stop
---

Code comments

1 eventDict defines all of the event types that Tkinter (strictly Tk) recognizes. Not all of the event masks defined by X are directly available to Tkinter applications, so you will see that the enumerated event type values are sparse.

'12': 'Expose', '15': 'Visibility', '17': 'Destroy',

The dictionary is also used to look up the event-type name when the event is detected.

2 reportEvent is our event handler. It is responsible for formatting data about the event. The event type is retrieved from eventDict; if an unrecognized event occurs, we will type it as Unknown.

def reportEvent(event):
    rpt = '\n\n%s' % (80*'=')
    rpt = '%s\nEvent: type=%s (%s)' % (rpt, event.type,
        eventDict.get(event.type, 'Unknown'))

3 Not all events supply focus and send_event attributes, so we handle AttributeErrors appropriately.

4 Finally, we bind each of the events to the reportEvent callback for the Frame and Entry widgets:

for event in eventDict.values():
    frame.bind('<%s>' % event, reportEvent)
    text.bind('<%s>' % event, reportEvent)

Figure 6.1 shows the result of running Example_6_2.py. The displayed events show the effect of typing SHIFT-M. You can see the KeyPress for the SHIFT key, and the KeyPress for the M key, followed by the corresponding KeyRelease events.

![Screenshot of an event monitor window showing event types and details](./images/event_monitor.png)

Figure 6.1 An event monitor