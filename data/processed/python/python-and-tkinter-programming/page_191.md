---
source_image: page_191.png
page_number: 191
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.50
tokens: 8766
characters: 2742
timestamp: 2025-12-24T00:37:14.287013
finish_reason: stop
---

NONBLANK = 1    # Field cannot be blank

dataDict  = {
    'crewmembers': ('crewmembers', 0.11, 0.45, 0.05, [
        ('Employee #', 'employee_no', 9, XX, 'valid_blank', NONBLANK),
        ('PIN', 'pin', 4, XX, '', BLANKOK),
        ('Category', 'type', 1, UC, 'valid_category', NONBLANK),
        ('SSN #', 'ssn', 9, XX, 'valid_ssn', BLANKOK),
        ('First Name', 'firstname', 12, XX, 'valid_blank', NONBLANK),
        ('Middle Name', 'middlename', 10, XX, '', BLANKOK),
        ('Last Name', 'lastname', 20, XX, 'valid_blank', NONBLANK),
        ('Status', 'status', 1, UC, '', BLANKOK),
        ('New Hire', 'newhire', 1, UC, 'valid_y_n_blank', BLANKOK),
        ('Seniority Date', 'senioritydate', 8, XX, 'valid_blank', NONBLANK),
        ('Seniority', 'seniority', 5, XX, 'valid_blank', NONBLANK),
        ('Base', 'base', 3, UC, 'valid_base', NONBLANK),
        ('Language 1', 'lang1', 2, UC, 'valid_lang', BLANKOK),
        ('Language 2', 'lang2', 2, UC, 'valid_lang', BLANKOK),
        ('Language 3', 'lang3', 2, UC, 'valid_lang', BLANKOK),
        ('Language 4', 'lang4', 2, UC, 'valid_lang', BLANKOK),
        ('Language 5', 'lang5', 2, UC, 'valid_lang', BLANKOK),
        ('Language 6', 'lang6', 2, UC, 'valid_lang', BLANKOK)],
        'Crew Members', [0]),
    'crewqualifications': ('crewqualification',0.25,0.45,0.075, [
        ('Employee #', 'employee_no', 9, XX, '', BLANKOK),
        ('Equipment', 'equipment', 3, UC, '', BLANKOK),
        ('Eqpt. Code', 'equipmentcode', 1, UC, '', BLANKOK),
        ('Position', 'position', 2, UC, '', BLANKOK),
        ('Pos. Code', 'positioncode', 2, UC, '', BLANKOK),
        ('Reserve', 'reserve', 1, UC, 'valid_r_blank', BLANKOK),
        ('Date of Hire', 'hiredate', 8, UC, '', BLANKOK),
        ('End Date', 'enddate', 8, UC, '', BLANKOK),
        ('Base Code', 'basecode', 1, UC, '', BLANKOK),
        ('Manager', 'manager', 1, UC, 'valid_y_n_blank', BLANKOK)],
        'Crew Qualifications', [0]) }

Code comments

① We define several constants to characterize the behavior of entry fields, controlling case-changing, for example:

LC   = 1      # Lowercase Key
UC   = 2      # Uppercase Key
XX   = 3      # As Is
...

② The first section of each entry in the dictionary defines the key, database table and layout data to customize the position of the first line, label/field position and the line spacing respectively.

'crewmembers': ('crewmembers', 0.11, 0.45, 0.05, [

③ Each entry in the dictionary defines the label, database key, field length, entry processing, validation and whether the field may be left blank.

('Employee #', 'employee_no', 9, XX, 'valid_blank', NONBLANK),
('PIN', 'pin', 4, XX, '', BLANKOK),
('Category', 'type', 1, UC, 'valid_category', NONBLANK),