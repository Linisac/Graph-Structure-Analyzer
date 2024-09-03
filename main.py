#! /usr/bin/env python3
#from numpy import *

import math as math
from functools import total_ordering

class graph:
    def __init__(self, initAdjMat = None, initLabelSet = None):
        if initAdjMat is None:
            self.adjMat = []
        else:
            self.adjMat = initAdjMat    
        if initLabelSet is None:
            self.labelSet = {}
        else:
            self.labelSet = initLabelSet
        self.order = math.floor(math.sqrt(len(self.adjMat)))
    def adj(self, i, j):
        return self.adjMat[i * self.order + j]
    def size(self):
        return int(pow(len(self.adjMat), 1 / 2))
    def __repr__(self):
        return (repr(self.adjMat) + repr(self.labelSet))
    def __str__(self):
        return ("Adjacency: \n" + str(self.adjMat) + "\nLabel Set:\n" + str(self.labelSet))

g = graph([2, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 1, 1, 2], {3, 5})
h = graph([2, 1, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 1, 2], {3, 5})
i = graph([2, 1, 1, 1, 0, 0, 1, 2, 1, 0, 0, 0, 1, 1, 2, 0, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2], {3, 5})
j = graph([2, 1, 1, 1, 0, 0, 1, 2, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2], {3, 5})
k = graph([2, 1, 1, 1, 1, 0, 1, 2, 1, 1, 0, 0, 1, 1, 2, 0, 0, 0, 1, 1, 0, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2], {3, 5})
@total_ordering
class multisetEntry:
    def __init__(self, input_atp=[]):
        self.atp = input_atp
        self.sift = []
    def add(self, color):
        self.sift.append(color)
    def _is_valid_operand(self, other):
        return (hasattr(other, "atp") and hasattr(other, "sift"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return ((self.atp, self.sift) == (other.atp, other.sift))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return ((self.atp, self.sift) < (other.atp, other.sift))
    def __repr__(self):
        return ("(" + repr(self.atp) + "; " + repr(self.sift) + ")")
    def __str__(self):
        return ("(" + str(self.atp) + "; " + str(self.sift) + ")")
    
@total_ordering
class multiset:
    def __init__(self):
        self.entriesAndCounts = []
    def add(self, entry):
        length = len(self.entriesAndCounts)
        if length == 0:
            self.entriesAndCounts.append([entry, 1])
        else:
            position = 0
            while(position < length):
                if entry == self.entriesAndCounts[position][0]:
                    break
                else:
                    position = position + 1
            if position == length:
                self.entriesAndCounts.append([entry, 1])
            else:
                self.entriesAndCounts[position][1] = self.entriesAndCounts[position][1] + 1
    def sort(self):
        self.entriesAndCounts.sort()
    def _is_valid_operand(self, other):
        return (hasattr(other, "entriesAndCounts"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return (self.entriesAndCounts == other.entriesAndCounts)
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return (self.entriesAndCounts < other.entriesAndCounts)
    def __repr__(self):
        length = len(self.entriesAndCounts)
        if length == 0:
            return "Empty"
        else:
            message = ""
            for i in range(length):
                message = message + "Color " + repr(i) + ": " + repr(self.entriesAndCounts[i][0]) + "\nOccurrence(s): " + repr(self.entriesAndCounts[i][1]) + "\n"
            return message
    def __str__(self):
        length = len(self.entriesAndCounts)
        if length == 0:
            return "Empty"
        else:
            message = ""
            for i in range(length):
                message = message + "Color " + str(i) + ": " + str(self.entriesAndCounts[i][0]) + "\nOccurrence(s): " + str(self.entriesAndCounts[i][1]) + "\n"
            return message
        
@total_ordering
class color:
    def __init__(self, fst, snd, level):
        self.fst = fst
        self.snd = snd
        self.level = level
    def _is_valid_operand(self, other):
        return (hasattr(other, "fst") and hasattr(other, "snd") and hasattr(other, "level"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return ((self.fst, self.snd, self.level) == (other.fst, other.snd, other.level))
    def __lt__(self, other):
        if not (self._is_valid_operand(other) and self.level == other.level):
            return NotImplemented
        else:
            return ((self.fst < other.fst) or (self.fst == other.fst and self.snd < other.snd))
    def __repr__(self):
        return ("FIRST" + repr(self.level) + ": " + repr(self.fst) + ", SECOND" + repr(self.level) + ": " + repr(self.snd))
    def __str__(self):
        return ("FIRST" + str(self.level) + ": " + str(self.fst) + ", SECOND" + str(self.level) + ": " + str(self.snd))

def atp(graph, tuple):
    mat = list()
    for i in range(0, len(tuple)):
        for j in range(0, len(tuple)):
            mat.append(graph.adj(tuple[i], tuple[j]))
    return mat
    
def tupleToNumber(tuple, base):
    length = len(tuple)
    sum = 0
    for i in range(0, length):
        sum = sum * base + tuple[i]
    return sum

def numberToTuple(num, base, length):
    if num == 0:
        return [0] * length
    else:
        tuple = list()
        for i in range(0, length):
            tuple.append((num % base))
            num = num // base
        tuple.reverse()
        return tuple


def wl(graph, dimen):
    #initial coloring, round 0
    initialColoring = {}
    for i in range((graph.order) ** dimen):
        initialColoring[i] = atp(graph, numberToTuple(i, graph.order, dimen))
    #coloring of round 1
    level = 1
    coloring = {}
    for i in range((graph.order ** dimen)):
        tuple = numberToTuple(i, graph.order, dimen)
        sndElement = multiset()
        for v in range(graph.order):
            tupleFirst = tuple.copy()
            tupleFirst.append(v)
            entry = multisetEntry(atp(graph, tupleFirst))
            for j in range(len(tuple)):
                tupleMinor = tuple.copy()
                tupleMinor[j] = v
                entry.add(initialColoring[tupleToNumber(tupleMinor, graph.order)])
            sndElement.add(entry)
        sndElement.sort()
        coloring[i] = color(initialColoring[i], sndElement, level)
    #iterative coloring until stable
    while(True):
        level = level + 1
        setOfColors = []
        for i in range((graph.order ** dimen)):
            if coloring[i] in setOfColors:
                continue
            else:
                setOfColors.append(coloring[i])
        totalNumOfColors = len(setOfColors)
        #compute new coloring
        newColoring = {}
        for i in range((graph.order ** dimen)):
            tuple = numberToTuple(i, graph.order, dimen)
            sndElement = multiset()
            for v in range(graph.order):
                tupleFirst = tuple.copy()
                tupleFirst.append(v)
                entry = multisetEntry(atp(graph, tupleFirst))
                for j in range(len(tuple)):
                    tupleMinor = tuple.copy()
                    tupleMinor[j] = v
                    entry.add(coloring[tupleToNumber(tupleMinor, graph.order)])
                sndElement.add(entry)
            sndElement.sort()
            newColoring[i] = color(coloring[i], sndElement, level)
        setOfNewColors = []
        for i in range((graph.order ** dimen)):
            if newColoring[i] in setOfNewColors:
                continue
            else:
                setOfNewColors.append(newColoring[i])
        totalNumOfNewColors = len(setOfNewColors)
        #decide stability
        if totalNumOfNewColors == totalNumOfColors: #stable
            return (level - 1, coloring, newColoring)
        else: #not yet stable
            coloring = newColoring

def coloring(graph, dimen):
    return wl(graph, dimen)[1]

def indent(ch, times):
    result = ""
    for i in range(times):
        result = result + ch
    return result

class clog:
    def __init__(self, form, operands):
        self.form = form
        self.operands = operands
    def _is_valid_operand(self, other):
        return (hasattr(other, "form") and hasattr(other, "operands"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return ((self.form, self.operands) == (other.form, other.operands))
    def toString(self, level=0):
            if self.form == "eq":
                return (indent('  ', level) + "x" + str(self.operands[0]) + " = x" + str(self.operands[1]))
            elif self.form == "adj":
                return (indent('  ', level) + "E(x" + str(self.operands[0]) + ", x" + str(self.operands[1]) + ")")
            elif self.form == "neg":
                return (indent('  ', level) + "not(\n" + self.operands[0].toString(level + 1) + "\n" + indent('  ', level) + ")")
            elif self.form == "cnj": #conjunction
                message = indent('  ', level)
                for i in range(len(self.operands)):
                    if i == 0:
                        message = message + "(\n" + self.operands[0].toString(level + 1) + "\n" + indent('  ', level) + ")"
                    else:
                        message = message + "\n" + indent('  ', level) + "and\n" + indent('  ', level) + "(\n" + self.operands[i].toString(level + 1) + "\n" + indent('  ', level) + ")"
                return message
            elif self.form == "dsj": #disjunction
                message = indent('  ', level)
                for i in range(len(self.operands)):
                    if i == 0:
                        message = message + "(\n" + self.operands[0].toString(level + 1) + "\n" + indent('  ', level) + ")"
                    else:
                        message = message + "\n" + indent('  ', level) + "or\n" + indent('  ', level) + "(\n" + self.operands[i].toString(level + 1) + "\n" + indent('  ', level) + ")"
                return message
            elif self.form == "exq":
                return indent('  ', level) + "exist(s)=" + str(self.operands[0]) + " x" + str(self.operands[1]) + "(\n" + self.operands[2].toString(level + 1) + "\n" + indent('  ', level) + ")"
            elif self.form == "unq":
                return indent('  ', level) + "for all x" + str(self.operands[0]) + "(\n" + self.operands[1].toString(level + 1) + "\n" + indent('  ', level) + ")"
            else:
                return "TRUE"
    def __repr__(self):
        return self.toString()
    def __str__(self):
        if self.form == "eq":
            return ("x" + str(self.operands[0]) + " = x" + str(self.operands[1]))
        elif self.form == "adj":
            return ("E(x" + str(self.operands[0]) + ", x" + str(self.operands[1]) + ")")
        elif self.form == "neg":
            return ("not(" + str(self.operands[0]) + ")")
        elif self.form == "cnj": #conjunction
            message = ""
            for i in range(len(self.operands)):
                if i == 0:
                    message = "(" + str(self.operands[0]) + ")"
                else:
                    message = message + " and " + "(" + str(self.operands[i]) + ")"
            return message
        elif self.form == "dsj": #disjunction
            message = ""
            for i in range(len(self.operands)):
                if i == 0:
                    message = "(" + str(self.operands[0]) + ")"
                else:
                    message = message + " or " + "(" + str(self.operands[i]) + ")"
            return message
        elif self.form == "exq":
            return "exist(s)=" + str(self.operands[0]) + " x" + str(self.operands[1]) + " (" + str(self.operands[2]) + ")"
        elif self.form == "unq":
            return "for all x" + str(self.operands[0]) + " (" + str(self.operands[1]) + ")"
        else:
            return "TRUE"   

def atpToFormula(adj, varList):
    dimen = int(pow(len(adj), 1 / 2))
    if dimen == 1:
        if (adj[0] == 2):
            return clog("eq", [varList[0], varList[0]])
        elif (adj[0] == 1):
            return clog("adj", [varList[0], varList[0]])
        elif (adj[0] == 0):
            return clog("neg", [clog("adj", [varList[0], varList[0]])])
    else:
        formulas = []
        for i in range(dimen):
            for j in range(i, dimen):
                if (adj[tupleToNumber([i, j], dimen)] == 2):
                    formulas.append(clog("eq", [varList[i], varList[j]]))
                elif (adj[tupleToNumber([i, j], dimen)] == 1):
                    formulas.append(clog("adj", [varList[i], varList[j]]))
                elif (adj[tupleToNumber([i, j], dimen)] == 0):
                    formulas.append(clog("neg", [clog("adj", [varList[i], varList[j]])]))
        return clog("cnj", formulas)

def colorToFormula(clr, varList=None):
    mset = clr.snd.entriesAndCounts
    dimen = int(pow(len(mset[0][0].atp), 1 / 2)) - 1
    if varList is None:
        varList = list(range(0, dimen + 1))
    if clr.level == 1: #base case
        fstConjunct = atpToFormula(clr.fst, varList)
        if len(mset) == 1:
            entry = mset[0][0]
            count = mset[0][1]
            formulas = [atpToFormula(entry.atp, varList)]
            for i in range(len(entry.sift)):
                newVarList = varList.copy()
                swap = newVarList[-1]
                newVarList[-1] = newVarList[-1 - (i + 1)]
                newVarList[-1 - (i + 1)] = swap
                formulas.append(atpToFormula(entry.sift[i], newVarList))
            sndConjunct = clog("exq", [count, varList[-1], clog("cnj", formulas)])
            thrConjunct = clog("unq", [varList[-1], clog("cnj", formulas)])
            return clog("cnj", [fstConjunct, sndConjunct, thrConjunct])
        else: #len(mset) > 1
            sndGrpOfFormulas = []
            thrGrpOfFormulas = []
            for entryAndCount in mset:
                entry = entryAndCount[0]
                count = entryAndCount[1]
                formulas = [atpToFormula(entry.atp, varList)]
                for i in range(len(entry.sift)):
                    newVarList = varList.copy()
                    swap = newVarList[-1]
                    newVarList[-1] = newVarList[-1 - (i + 1)]
                    newVarList[-1 - (i + 1)] = swap
                    formulas.append(atpToFormula(entry.sift[i], newVarList))
                sndGrpOfFormulas.append(clog("exq", [count, varList[-1], clog("cnj", formulas)]))
                thrGrpOfFormulas.append(clog("cnj", formulas))
            sndConjunct = clog("cnj", sndGrpOfFormulas)
            thrConjunct = clog("unq", [varList[-1], clog("dsj", thrGrpOfFormulas)])
            return clog("cnj", [fstConjunct, sndConjunct, thrConjunct])
    else: #recursive case, clr.level > 1
        fstConjunct = colorToFormula(clr.fst, varList)
        if len(mset) == 1:
            entry = mset[0][0]
            count = mset[0][1]
            formulas = [atpToFormula(entry.atp, varList)]
            for i in range(len(entry.sift)):
                newVarList = varList.copy()
                swap = newVarList[-1]
                newVarList[-1] = newVarList[-1 - (i + 1)]
                newVarList[-1 - (i + 1)] = swap
                formulas.append(colorToFormula(entry.sift[i], newVarList))
            sndConjunct = clog("exq", [count, varList[-1], clog("cnj", formulas)])
            thrConjunct = clog("unq", [varList[-1], clog("cnj", formulas)])
            return clog("cnj", [fstConjunct, sndConjunct, thrConjunct])
        else: #len(mset) > 1
            sndGrpOfFormulas = []
            thrGrpOfFormulas = []
            for entryAndCount in mset:
                entry = entryAndCount[0]
                count = entryAndCount[1]
                formulas = [atpToFormula(entry.atp, varList)]
                for i in range(len(entry.sift)):
                    newVarList = varList.copy()
                    swap = newVarList[-1]
                    newVarList[-1] = newVarList[-1 - (i + 1)]
                    newVarList[-1 - (i + 1)] = swap
                    formulas.append(colorToFormula(entry.sift[i], newVarList))
                sndGrpOfFormulas.append(clog("exq", [count, varList[-1], clog("cnj", formulas)]))
                thrGrpOfFormulas.append(clog("cnj", formulas))
            sndConjunct = clog("cnj", sndGrpOfFormulas)
            thrConjunct = clog("unq", [varList[-1], clog("dsj", thrGrpOfFormulas)])
            return clog("cnj", [fstConjunct, sndConjunct, thrConjunct])

def clogType(graph, tuple, dimen, coloring=None):
    graphSize = graph.size()
    lengthOfTuple = len(tuple)
    if coloring is None:
        coloring = wl(graph, dimen - 1)[2]
    if lengthOfTuple == dimen - 1:
        return colorToFormula(coloring[tupleToNumber(tuple, graphSize)])
    else:
        formulasAndCounts = []
        for i in range(graphSize):
            extendedTuple = tuple.copy()
            extendedTuple.append(i)
            formula = colorToFormula(coloring[tupleToNumber(extendedTuple, graphSize)])
            length = len(formulasAndCounts)
            position = 0
            while(position < length):
                if formula == formulasAndCounts[position][0]:
                    break
                else:
                    position = position + 1
            if position == length:
                formulasAndCounts.append([formula, 1])
            else:
                formulasAndCounts[position][1] = formulasAndCounts[position][1] + 1
        totalNumOfFormulas = len(formulasAndCounts)
        quantifiedFormulas = []
        for i in range(totalNumOfFormulas):
            quantifiedFormulas.append(clog("exq", [formulasAndCounts[i][1], lengthOfTuple, formulasAndCounts[i][0]]))
        return clog("cnj", quantifiedFormulas)
            
            