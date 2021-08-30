print("Hi, welcome to the PythonMaker \nMade by 272!!!")

try:
    f3 = open("Output.txt", "x")
    print("Made output.txt, this is where your code will be sent to when you are done.")
except:
    input("It would appear that Output.txt has already been made, if so please make sure to save the code from it and then press enter! ")
    f3 = open("Output.txt", "w")
f3.close()

f1 = open("Output.txt", "a")

input272 = 0
varList = {}
def variable272():
    varName = str(input("Hi what would you like this variable to be called? "))
    varValue = input("What would you like the value to be? ")
    varValueType = int(input("What type is this value?\n1 • Integer\n2 • String\n3 • Float\n4 • Boolean "))
    if varValueType == 1:
        varValue = int(varValue)
        varList[varName] = (varValue)
    elif varValueType == 2:
        varValue = str(varValue)
        varList[varName] = (varValue)
    elif varValueType == 3:
        varValue = float(varValue)
        varList[varName] = (varValue)
    elif varValueType == 4:
        varValue = bool(varValue)
        varList[varName] = (varValue)
    else: 
        print("It would appear you typed something incorrect! :/")
        return
    
    f1.write(f'{varName} = {varValueType}({varValue})\n')
    
    
    
    

def print272():
    printStatement = ""
    printintPut = int(input("What kind of print are you doing?\n1 • String \n2 • String + Variable \n3 • Number Equations "))
    if printintPut == 1:
        printString = input("Enter your string ")
        printStatement = printString
    elif printintPut == 2:
        printString = str(input("Enter your string first (Don't worry if you want your variable to be in between your string) "))
        print(f"Here is a list of the current variables and their values! \n\n{varList}")
        printVariable = input("Now enter your variable(Case Sensitive)! ")
        printStringVar = int(input("Where do you want your variable in relation to your string?\n1 • At the start \n2 • At the end \n3 • Choose what place "))
        if printStringVar == 1:
            printStatement = printVariable, printString
        elif printStringVar == 2:
            printStatement = printString, printVariable
        elif printStringVar == 3:
            posPrintVar = int(input("At what point in the string would you like the variable "))
            startPrint = (printString[:posPrintVar])
            finishPrint = (printString[posPrintVar:])
            printStatement = f"{startPrint} {printVariable} {finishPrint}"
    elif printintPut == 3:
        printVal1 = int(input("What type is the first value?\n1 • Variable\n2 • Integer\n3 • Float "))
        if printVal1 == 1:
            print(f"Here is a list of the current variables and their values! \n\n{varList}")
            varForVal1 = str(input("Which variable would you like to use (Case Sensitive)? "))
            printVal123 = varList.get(varForVal1)
        elif printVal1 == 2:
            printVal123 = int(input("Hi enter your integer! "))
        elif printVal1 == 3:
            printVal123 = float(input("Hi enter your float please!" ))
        else: 
            print("It would appear you typed something incorrect! :/")
            return
        printOperator = int(input("What operator are you using?\n1 • +\n2 • - \n3 • /\n4 • * "))
        

        printVal2 = int(input("What type is the second value?\n1 • Variable\n2 • Integer\n3 • Float "))
        if printVal2 == 1:
            print(f"Here is a list of the current variables and their values! \n\n{varList}")
            varForVal2 = str(input("Which variable would you like to use (Case Sensitive)? "))
            printVal1232 = varList.get(varForVal2)
        elif printVal2 == 2:
            printVal1232 = int(input("Hi enter your integer! "))
        elif printVal2 == 3:
            printVal1232 = float(input("Hi enter your float please!" ))
        else: 
            print("It would appear you typed something incorrect! :/")
            return
        if printOperator == 1:
            printStatement = (f"{printVal123} + {printVal1232}")
        elif printOperator == 2:
            printStatement = (f"{printVal123} - {printVal1232}")
        elif printOperator == 3:
            printStatement = (f"{printVal123} / {printVal1232}")
        elif printOperator == 4:
            printStatement = (f"{printVal123} * {printVal1232}")
        else: 
            print("It would appear you typed something incorrect! :/")
            return
    
    else: 
        print("It would appear you typed something incorrect! :/")
        return
    
    
    f1.write(f'Print("{printStatement}")\n')
    
    
    
    


while input272 != 99:
    input272 = int(input("Hi enter the number that correlates to the command you want to do! \n1 • Print \n2 • Set Variables\n99 • Quit! "))
    if input272 == 1:
        print272()
    elif input272 == 2:
        variable272()
    elif input272 == 99:
        f1.close()
        break
    else:
        print("It would appear you typed something incorrect! :/")
        continue