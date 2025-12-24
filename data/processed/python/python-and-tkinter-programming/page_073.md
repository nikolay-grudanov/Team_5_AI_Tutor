---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.21
tokens: 8548
characters: 2611
timestamp: 2025-12-24T00:33:37.509210
finish_reason: stop
---

• weight   A string that identifies the nominal blackness of the font, according to the foundry’s judgment (for example, medium, bold, etc.).
• slant   A code string that indicates the overall posture of the typeface design used in the font—one of roman (R), italic (I) or oblique (O).
• pointSize   An unsigned integer-string typographic metric in device-independent units which gives the body size for which the font was designed.
• encoding   A registered name that identifies the coded character set as defined by the specified registry.

An example of an X font descriptor might be:

'-*-verdana-medium-r-*-*-*-*-*-*-*-*-*-*'

This describes an 8-point Verdana font, medium weight and roman (upright). Although the descriptor is somewhat ugly, most programmers get used to the format quickly. With X-servers, not all fonts scale smoothly if a specific pointsize is unavailable in a font; unfortunately it is a trial-and-error process to get exactly the right combination of font and size for optimal screen appearance.

4.2.3 Colors

Tkinter allows you to use the color names defined by the X-server. These names are quite florid, and do not always fully describe the color: LavenderBlush1, LemonChiffon, LightSalmon, MediumOrchid3 and OldLace are just a few. Common names such as red, yellow, blue and black may also be used. The names and the corresponding RGB values are maintained in a Tk include file, so the names may be used portably on any Tkinter platform.*

It is often easier to precisely define colors using color strings:

#RGB      for 4-bit values (16 levels for each color)
#RRGGBB   for 8-bit values (256 levels for each color)
#RRRRGGGGBBBB   for 16-bit values (65526 levels for each color)

Here is an example of how one might set up part of a color definition table for an application (incomplete code):

# These are the color schemes for xxx and yyy front panels
#    Panel    LED off    ON    Active    Warning
COLORS = [('#545454','#656565','LawnGreen', 'ForestGreen','DarkOrange',\
#    Alarm    Display    Inside    Chrome    InsideP    Chassis
    '#ff342f','#747474','#343434','#efefef','#444444','#a0a0a0',\
#    DkChassis LtChassis VDkChassis VLtChassis Bronze
    '#767600','#848400','#6c6c00','#909000','#7e5b41'),
etc.

* X window color names are present in the standard X11 distribution but are not specified by the X11 Protocol or Xlib. It is permissible for X-server vendors to change the names or alter their interpretation. In rare cases you may find an implementation that will display different colors with Tkinter and X Window applications using the same color name.