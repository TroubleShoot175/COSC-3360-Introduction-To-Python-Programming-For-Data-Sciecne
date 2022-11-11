''' Developing Title Library'''

from typing import Union

def strToTitle(stringToTitle: str, show: bool = False, amountOfChar: Union[str, tuple[str, int]] = 'f', spaces: bool = True, charForBar: str = "="):
    '''
    WARNING: This is only used for buildnig section TerminalTitleBuilder for clearer console print outs.
    
    Parameters
    ==========
    stringToTitle : string
        String to put in the center of the title.

    show : boolean, default=False, optional
        When False, builds a string and returns the built string to be printed.
        When True, builds teh string and then prints the built string.

    amountOfChar : str OR iterable, default="f" (Is the length of the string passed by default), optional
        Defines the number of characters to insert before or after the `stringToTitle`.

    spaces : boolean, default=True, optional
        Adds spaces before and after the `stringToTitle`.

    charForBar : string, default="=", optional
        Allows the operator to change the type of character used for the bars around the 

    Returns
    =======
    When 'show' is False, the built string will be returned.
    When 'show' is True, nothing will be returned.
    When 'amountOfChar' is not tuple or string, 0 will be returned.

    Prints
    ======
    The built string.

    Usage
    =====
    print(strToTitle("String You Want In Title"))
    
    AOR

    print(strToTitle("String You Want In Title", False, 'f'))
    >>> ======================= String You Want In Title =======================

    AOR

    print(strToTitle("String You Want In Title", False, 'h'))
    >>> =========== String You Want In Title ===========

    AOR

    print(strToTitle("String You Want In Title", False, ("c", #))) # = any integer (This case 10)
    >>> ========== String You Want In Title ==========

    AOR

    print(strToTitle("String You Want In Title", False, 'h', False))
    >>> ===========String You Want In Title===========

    AOR

    print(strToTitle("String You Want In Title", False, 'h', True, '@'))
    >>> @@@@@@@@@@@@ String You Want In Title @@@@@@@@@@@
    '''
    
    if amountOfChar == "f":
        numOfChar = len(stringToTitle)
    elif amountOfChar == "h":
        numOfChar = int(len(stringToTitle) / 2)
    elif amountOfChar[0] == "c":
        numOfChar = amountOfChar[1]
    else:
        return 0


    titleBar = ""
    for x in range(0, numOfChar):
        titleBar += charForBar

    if spaces == True:
        stringToTitle = " " + stringToTitle + " "

    builtString = titleBar + stringToTitle + titleBar

    if show == False:
        return builtString
    else:
        print(builtString)
