---
source_image: page_587.png
page_number: 587
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.02
tokens: 8572
characters: 3292
timestamp: 2025-12-24T00:48:41.248177
finish_reason: stop
---

• maxstrict If true, then maximum checking is strictly enforced. Otherwise, the entry input may be more than max, but it will be displayed using the errorbackground color. The default is true.

If the dictionary contains a stringtovalue field, it overrides the normal stringtovalue function for the validator. The stringtovalue function is described below.
Other fields in the dictionary (apart from the core fields mentioned above) are passed on to the validator and stringtovalue functions as keyword arguments.
If validate is not a dictionary, then it is equivalent to specifying it as a dictionary with a single validator field. For example, validate = 'real' is equivalent to validate = {'validator': 'real'} and it specifies real numbers without any minimum or maximum limits and using “.” as the decimal point character.
The standard validators accepted in the validator field are these:
• numeric An integer greater than or equal to 0. Digits only. No sign.
• hexadecimal Hex number (with optional leading 0x), as accepted by string.atol(text, 16).
• real A number, with or without a decimal point and optional exponent (e or E), as accepted by string.atof(). This validator accepts a separator argument, which specifies the character used to represent the decimal point. The default separator is “.”.
• alphabetic Consisting of the letters a-z and A-Z. In this case, min and max specify limits on the length of the text.
• alphanumeric Consisting of the letters a-z, A-Z and the numbers 0-9. In this case, min and max specify limits on the length of the text.
• time Hours, minutes and seconds, in the format HH:MM:SS, as accepted by Pmw.timestringtoseconds(). This validator accepts a separator argument, which specifies the character used to separate the three fields. The default separator is “:”. The time may be negative.
• date Day, month and year, as accepted by Pmw.datestringtojdn(). This validator accepts a separator argument, which specifies the character used to separate the three fields. The default is “:”. This validator also accepts a format argument, which is passed to Pmw.datestringtojdn() to specify the desired ordering of the fields. The default is ymd.

If validator is a function, then it will be called whenever the contents of the entry may have changed due to user action or by a call to setentry(). The function is called with at least one argument, the first one being the new text as modified by the user or setentry(). The other arguments are keyword arguments made up of the non-core fields of the validate dictionary.
The validator function should return Pmw.OK, Pmw.ERROR or Pmw.PARTIAL as described above. It should not perform minimum and maximum checking. This is done after the call, if it returns Pmw.OK.
The stringtovalue field in the dictionary may be specified as the name of one of the standard validators, the name of a validator supplied by the extravalidators option, a function or None.
The stringtovalue function is used to convert the entry input into a value which can then be compared with any minimum or maximum values specified for the validator. If the min or max fields are specified as strings, they are converted using the stringtovalue function. The stringtovalue function is called with the same arguments as the validator