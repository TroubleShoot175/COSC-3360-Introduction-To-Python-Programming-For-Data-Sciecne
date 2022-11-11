''' Developing Title Library'''

def sectionTitle(stringToTitle, show=False, spaces=True, amountOfChar=0, charForBar="="):
    '''
    WARNING: This is only used for buildnig TerminalTitleBuilder for clearer console print-outs.
    Do not use within print statements for formating. 
    
    Parameters
    ==========
    stringToTitle : string
        String to put in the center of the title.
    show : boolean, default=False, optional
        When False, builds a string and returns the built string to be printed.
        When True, builds teh string and then prints the built string.
    spaces : boolean, default=True, optional
        Adds spaces before and after the `stringToTitle`.
    amountOfChar : integer, default=0 (Is the length of the string passed by default), optional
        Defines the number of characters to insert before or after the `stringToTitle`.
    charForBar : string, default="=", optional

    Returns
    =======
    String with the passed information added to the passed string.

    Prints
    ======
    String with the passed information added to the passed string.
    '''
    if amountOfChar == 0:
        amountOfChar = len(stringToTitle)

    titleBar = ""
    for x in range(0, amountOfChar):
        titleBar += charForBar

    if spaces == True:
        stringToTitle = " " + stringToTitle + " "

    builtString = titleBar + stringToTitle + titleBar

    if show == False:
        return builtString
    else:
        print(builtString)

print(sectionTitle("Test", spaces=0, amountOfChar=10, charForBar='-'))