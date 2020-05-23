from Errors import *


def PRINT(line):
    lst1 = line.split()
    printed = ""

    for w in range(1, len(lst1)):

        word = lst1[w]
        end = int(len(word))
        if word in Variables and word[0] != "\"":  # This checks if it is a variable and if the variable exists
            printed += Variables[word]
        else:
            for c in range(end):
                if w == 1 and c == 0 or w == len(lst1) - 1 and c == end - 1:
                    pass
                else:
                    printed += word[c]
            printed += " "

    print(printed)

    # I Still have to work on all the condition cases in the while. A more effective way should be used in order to
    # satisfy more compound conditions. The use of dictionaries should be explored


def WHILE(file, CurFlags, counter, variables, CurLine):
    # Defining the condition
    Lst2 = CurLine.split()
    if Lst2[1] in variables:
        toc1 = variables[Lst2[1]]
    elif type(Lst2[1]) == float or type(Lst2[1]) == int:
        toc1 = variables[Lst2[1]]
    op1 = Lst2[2]
    if Lst2[3] in variables:
        toc2 = variables[Lst2[3]]
    elif type(Lst2[3]) == float or type(Lst2[3]) == int:
        toc2 = variables[Lst2[3]]
    # Listing comparison scenarios for the Conditions
    if op1 == "=":
        CurFlags[counter] = toc1 == toc2
    elif op1 == ">":
        CurFlags[counter] = toc1 > toc2
    elif op1 == "<":
        CurFlags[counter] = toc1 < toc2
    elif op1 == "<=":
        CurFlags[counter] = toc1 <= toc2
    elif op1 == ">=":
        CurFlags[counter] = toc1 >= toc2

    else:
        print("There is an invalid operand")

    while CurLine[0:8] != "ENDWHILE" and CurFlags:
        if CurLine[0:5] == "PRINT":
            PRINT(CurLine)

        elif CurLine[0:5] == "WHILE":
            WHILE(file, CurFlags, counter, variables, CurLine)

        elif CurLine[0:6] == "REPEAT":
            pass

        elif CurLine[0:5] == "INPUT":
            variables[CurLine[6:len(CurLine) - 1]] = input()

        elif CurLine[0:3] == "FOR":
            FOR(CurLine)

        elif CurLine[0:2] == "IF":
            IF(CurLine, variables, CurFlags)

        # Assignment statement
        else:
            pass  # This part should carry out an assignment statement

        CurLine = file.readline()
        Lst2 = CurLine.split()
        if Lst2[1] in variables:
            toc1 = variables[Lst2[1]]
        elif type(Lst2[1]) == float or type(Lst2[1]) == int:
            toc1 = variables[Lst2[1]]
        op1 = Lst2[2]
        if Lst2[3] in variables:
            toc2 = variables[Lst2[3]]
        elif type(Lst2[3]) == float or type(Lst2[3]) == int:
            toc2 = variables[Lst2[3]]
        # Listing comparison scenarios for the Conditions
        if op1 == "=":
            CurFlags[counter] = toc1 == toc2
        elif op1 == ">":
            CurFlags[counter] = toc1 > toc2
        elif op1 == "<":
            CurFlags[counter] = toc1 < toc2
        elif op1 == "<=":
            CurFlags[counter] = toc1 <= toc2
        elif op1 == ">=":
            CurFlags[counter] = toc1 >= toc2


def IF(CurLine, variables, flags):
    """

    :rtype: object
    """
    Lst2 = CurLine.split()
    if Lst2[1] in variables:
        toc1 = variables[Lst2[1]]
    elif type(Lst2[1]) == float or type(Lst2[1]) == int:
        toc1 = variables[Lst2[1]]
    op1 = Lst2[2]
    if Lst2[3] in variables:
        toc2 = variables[Lst2[3]]
    elif type(Lst2[3]) == float or type(Lst2[3]) == int:
        toc2 = variables[Lst2[3]]
    # Listing comparison scenarios for the
    if op1 == "=":
        flags.append(toc1 == toc2)
    elif op1 == ">":
        flags.append(toc1 > toc2)
    elif op1 == "<":
        flags.append(toc1 < toc2)
    elif op1 == "<=":
        flags.append(toc1 <= toc2)
    elif op1 == ">=":
        flags.append(toc1 >= toc2)
    else:
        OpInvalid.isprint()


def FOR(CurLine, file):
    Lst = CurLine.split()
    LCV = Lst[1]
    Start = int(Lst[3])
    End = int(Lst[5])
    for i in range(Start, End):
        if CurLine[0:5] == "PRINT":
            PRINT(CurLine)

        elif CurLine[0:5] == "WHILE":
            WHILE(file, Flags, no, Variables, CurLine)

        elif CurLine[0:6] == "REPEAT":
            REPEAT()  # Haven't added repeat

        elif CurLine[0:5] == "INPUT":
            Variables[CurLine[6:len(CurLine) - 1]] = input()

        elif CurLine[0:3] == "FOR":
            FOR(CurLine)

        elif CurLine[0:2] == "IF":
            IF(CurLine, Variables, Flags)

        # Assignment statement
        else:
            pass  # This part should carry out an assignment statement

        CurLine = file.readline()
        Lst = CurLine.split()


def assignment():
    pass


def REPEAT():
    pass
