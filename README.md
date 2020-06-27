# rebar_waste_reducer
This program helps reduce waste of rebars in construction site by comparing rebars in model with rebars in leftovers database
# Requirements
Text files must be copied form Tekla Structures inquire window or have the same structure.
Leftovers database must be in csv format and have structure as in added csv example.
# How to use
1. Setup default file path in main module (file path where text files of elements and csv files of leftovers are being used).
2. In main module, set text file of the element to be checked.
3. in main module, set leftovers csv file to be checked.
4. Run program.
Program returns rebars that are created in the element and are available in leftovers stock.
# Limitations
Current version only compares length of rebars, and only return rebars which are in stock and have exactly the same lenght.
