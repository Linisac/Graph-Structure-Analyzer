#! /usr/bin/env python3
import fileinput
import sys

##################
# Wei-lin Wu
#TO DO: Exception handling
##################


# used to store a parsed TL expressions which are
# constant numbers, constant strings, variable names, and binary expressions
class Expr :
    def __init__(self, op1, operator, op2 = None):
        self.op1 = op1
        self.operator = operator
        self.op2 = op2

    def __str__(self):
        if self.op2 == None:
            return "(" + self.operator + " " + str(self.op1) + ")"
        else:
            return "(" + str(self.op1) + " " + self.operator + " " + str(self.op2) + ")"

    # evaluate this expression given the environment of the symTable
    def eval(self, symTable):
        if self.operator == "var":
            if self.op1 in symTable.keys():
                return ("normal", symTable[self.op1])
            else:
                return ("undefined", self.op1)
        elif self.operator == "num":
            return ("normal", self.op1)
        elif self.operator == "str":
            return ("normal", self.op1)
        elif self.operator == "+":
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            else:
                return ("normal", value1 + value2)
        elif self.operator == "-":
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            else:
                return ("normal", value1 - value2)
        elif self.operator == "*":
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            else:
                return ("normal", value1 * value2)
        elif self.operator == "/":
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            elif value2 == 0:
                return ("division by 0", 0)
            else:
                return ("normal", value1 / value2)
        elif self.operator == "<":
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            elif value1 < value2:
                return ("normal", 1)
            else:
                return ("normal", 0)
        elif self.operator == ">":
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            elif value1 > value2:
                return ("normal", 1)
            else:
                return ("normal", 0)
        elif self.operator == "<=":
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            elif value1 <= value2:
                return ("normal", 1)
            else:
                return ("normal", 0)
        elif self.operator == ">=":
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            elif value1 >= value2:
                return ("normal", 1)
            else:
                return ("normal", 0)
        elif self.operator == "==":
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            elif value1 == value2:
                return ("normal", 1)
            else:
                return ("normal", 0)
        else: # that is, self.operator == "!="
            (message1, value1) = self.op1.eval(symTable)
            (message2, value2) = self.op2.eval(symTable)
            if message1 == "undefined":
                return ("undefined", value1)
            elif message2 == "undefined":
                return ("undefined", value2)
            elif value1 != value2:
                return ("normal", 1)
            else:
                return ("normal", 0)

# used to store a parsed TL statement
class Stmt :
    def __init__(self, keyword, exprs):
        self.keyword = keyword
        self.exprs = exprs

    def __str__(self):
        others = ""
        for exp in self.exprs:
            others = others + " " + str(exp)
        return self.keyword + others

    # perform/execute this statement given the environment of the symTable
    def perform(self, symTable, currLine):
        if self.keyword == "let":
            expr = self.exprs[1]
            (message, value) = expr.eval(symTable)
            if message == "undefined":
                print("Undefined variable " + value + " at line " + str(currLine) + ".")
                return ("halt", symTable)
            elif message == "division by 0":
                print("Division by 0 on line " + str(currLine) + "\n")
                return ("halt", symTable)
            else: # that is, message == "normal"
                variable = self.exprs[0]
                symTable.update({variable : value})
                return (currLine + 1, symTable)
        elif self.keyword == "if":
            expr = self.exprs[0]
            (message, value) = expr.eval(symTable)
            if message == "undefined":
                print("Undefined variable " + value + " at line " + str(currLine) + ".")
                return ("halt", symTable)
            elif message == "division by 0":
                print("Division by 0 on line " + str(currLine) + "\n")
                return ("halt", symTable)
            elif value > 0: # and message == "normal"
                label = self.exprs[1]
                if label in symTable.keys(): # label appears in the symbol table
                    targetLine = symTable[label]
                    return (targetLine, symTable)
                else: # label does not appear in the symbol table
                    print("Illegal goto label at line " + str(currLine))
                    return ("halt", symTable)
            else: # that is, message == "normal" and value == 0
                return (currLine + 1, symTable)
        elif self.keyword == "print":
            displayString = ""
            for expr in self.exprs:
                (message, value) = expr.eval(symTable)
                if message == "undefined":
                    print("Undefined variable " + value + " at line " + str(currLine) + ".")
                    return ("halt", symTable)
                elif message == "division by 0":
                    print("Division by 0 on line " + str(currLine) + "\n")
                    return ("halt", symTable)
                else: # that is, message == "normal"
                    displayString = displayString + " " + str(value)
            print(displayString)
            return (currLine + 1, symTable)
        else: # that is, self.keyword == "input"
            variable = self.exprs[0]
            value = input("Enter value for a variable: ")
            if value.isnumeric() or ((value[0] == '+' or value[0] == '-') and value[1 : ].isnumeric()): # that is, if valid value for number
                value = float(value) # type cast from string to floating-point value
                symTable.update({variable : value})
                return (currLine + 1, symTable)
            else: # that is, invalid value for number
                print("Illegal or missing input")
                return ("halt", symTable)

class Prog :
    def __init__(self, symTable, listOfStmts):
        self.symtable = symTable
        self.stmts = listOfStmts
    
    def execute(self):
        statements = self.stmts
        symTable = self.symtable
        totalNumOfStatements = len(statements)
        currLineNumber = 0
        while currLineNumber < totalNumOfStatements:
            currStatement = statements[currLineNumber]
            (currLineNumber, symTable) = currStatement.perform(symTable, currLineNumber)
            if (currLineNumber == "halt"):
                break

         
def isLabel(str):
    if str.endswith(':'):
        str = str[ : -1]
        if str.isalnum():
            return True
    else:
        return False


def isString(str):
    return (str.startswith('"') and str.endswith('"'))


def parseNonStringExpr(tokens):
    numOfTokens = len(tokens)
    if numOfTokens == 1: # expression is a variable or constant number
        expr = tokens[0]
        if expr[0].isalpha(): # expression is a variable
            return ("normal", Expr(expr, "var"))
        elif expr.isnumeric() or ((expr[0] == '+' or expr[0] == '-') and expr[1 : ].isnumeric):
            return ("normal", Expr(float(expr), "num"))
        else:
            return ("error", 0)
    elif numOfTokens == 3: # expression involves a binary operator
        op1 = tokens[0]
        op  = tokens[1]
        op2 = tokens[2]
        if op == "+" or op == "-" or op == "*" or op == "/" or op == "<" or op == ">" or op == "<=" or op == ">=" or op == "==" or op == "!=":
            op1 = parseNonStringExpr([op1])
            if op1[0] == "normal":
                op2 = parseNonStringExpr([op2])
                if op2[0] == "normal":
                    op1 = op1[1]
                    op2 = op2[1]
                    return ("normal", Expr(op1, op, op2))
                else:
                    return ("error", 0)
            else:
                return ("error", 0)
        else:
            return ("error", 0)
    else:
        return ("error", 0)

        
#########################################################
# below is the main action            


filepath = input("Enter the file name of a TL program: ")
with open(filepath) as fp:
    listOfStatements = []
    symTable = {}
    line = fp.readline()
    lineNumber = 0
    successfulParsing = True
    
    # parsing
    while line:
        tokens = line.split()
        lineIsLabeled = False
        label = ""
        
        if isLabel(tokens[0]):
            lineIsLabeled = True
            label = tokens[0]
            symTable.update({label : lineNumber})
            tokens = tokens[1 : ]
        
        if tokens[0] == "let":
            variable = tokens[1]
            expr = parseNonStringExpr(tokens[3 : ])
            if expr[0] == "normal":
                expr = expr[1]
                listOfStatements.append(Stmt("let", [variable, expr]))
            else:
                print("Syntax error at line " + str(lineNumber))
                successfulParsing = False
                break
        elif tokens[0] == "if":
            lastToken = tokens[-1]
            label = lastToken + str(":")
            if not isLabel(label):
                print("Syntax error at line " + str(lineNumber))
                successfulParsing = False
                break
            expr = parseNonStringExpr(tokens[1 : -2])
            if expr[0] == "normal":
                expr = expr[1]
                listOfStatements.append(Stmt("if", [expr, label]))
            else:
                print("Syntax error at line " + str(lineNumber))
                successfulParsing = False
                break
        elif tokens[0] == "print":
            if lineIsLabeled:
                lengthOfLabel = len(label)
                line = line[lengthOfLabel : ]
                line = line.strip()
            
            exprFragments = line.split(", ")
            exprFragments[0] = exprFragments[0].strip()
            exprFragments[0] = exprFragments[0][5 : ] # "print" has length 5
            exprFragments[0] = exprFragments[0].strip()
            
            exprs = []
            for fragment in exprFragments:
                fragment = fragment.strip()
                if isString(fragment):
                    fragment = fragment.strip('"')
                    exprs.append(Expr(fragment, "str"))
                else:
                    tokens = fragment.split()
                    expr = parseNonStringExpr(tokens)
                    if expr[0] == "normal":
                        exprs.append(expr[1])
                    else:
                        print("Syntax error at line " + str(lineNumber))
                        successfulParsing = False
                        break
            
            if successfulParsing == False:
                break
            else:   
                listOfStatements.append(Stmt("print", exprs))
        elif tokens[0] == "input":
            variable = tokens[1]
            listOfStatements.append(Stmt("input", [variable]))
            
        
        line = fp.readline()
        lineNumber += 1
    
    # evaluation of the program
    if successfulParsing == True:
        program = Prog(symTable, listOfStatements)
        program.execute()