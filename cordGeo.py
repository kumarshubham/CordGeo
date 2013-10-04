__author__ = 'kumar'

import random
import math
from fractions import Fraction
from lib import MultiplyMinus, getAnsString, getSignedString, GetCoeffString, GetNewIfEqual, GetNewIfEqualInt
from generateFiles import generateCSV, generateSVG

set1 = [0, 180]
set2 = [30, 210]
set3 = [45, 225]
set4 = [60, 240]
set5 = [90, 270]
set6 = [120, 300]
set7 = [135, 315]
set8 = [150, 330]
angleSet = [set1, set2, set3, set4, set5, set6, set7, set8]


def cordinateGeo(startIndex=0, lastIndex=26):
    """

    :param startIndex:
    :param lastIndex:
    """
    Mtype = 1
    Mtype1 = 2
    ques = []
    for x in range(startIndex, lastIndex):
        temp = {}
        Qtype = x + 1
        temp1 = random.randint(0, 7)
        inclination = getInclination(temp=temp1)
        m = getSlope(inclination)
        if m[0] > 100 or m[1] == 0:
            m1 = "&infin;"
            slope = "&infin;"
        else:
            m1 = str(m[0]) + "/" + str(m[1])
            slope = m[0] / m[1]

        if Qtype == 2 or Qtype == 5 or Qtype == 8:
            points = getLinePoints(slope=slope)
            equation = getEqFromPoints(points)
            question = getQuestion(Qtype, m1, inclination, [points], equation)
            hints = getHints(Qtype, inclination, points)
            options = getOptions(Qtype, inclination, slope, [equation], set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
            i2 = getOppositeInclination(temp1)
            i3 = getInclination(GetNewIfEqualInt([temp1, temp1 + 4, temp1 - 4], 0))
            i4 = getInclination(GetNewIfEqualInt([temp1, temp1 + 4, temp1 - 4, 0], 4))
            m2 = getSlope(i2)
            m3 = getSlope(i3)
            m4 = getSlope(i4)
            iList = [inclination, i2, i3, i4]
            mList = [m, m2, m3, m4]
            for x in range(4):
                if mList[x][0] > 100 or mList[x][1] == 0:
                    slope = "&infin;"
                else:
                    slope = mList[x][0] / mList[x][1]
                points = getLinePoints(slope=slope)
                equation = getEqFromPoints(points)
                a = [getStringToDisplay(Qtype=Qtype, equation=equation, m=mList[x], i=iList[x])]
                generateSVG([equation], a, str(Qtype) + "_" + str(x), Qtype, [points])
        elif Qtype == 10 or Qtype == 11 or Qtype == 15:
            points = getRandomLinePoints()
            slope = getSlopeFromPoints(points)
            while slope == "&infin;":
                points = getRandomLinePoints()
                slope = getSlopeFromPoints(points)
            equation = getEqFromPoints(points)
            points1 = getLinePoints(slope=slope)
            equation1 = getEqFromPoints(points1)
            slope = round(slope, 2)
            question = getQuestion(Qtype, slope, inclination, [points, points1], equation1)
            hints = getHints(Qtype, inclination, points)
            options = getOptions(Qtype, inclination, slope, [equation, equation1], set=angleSet[temp1], points=[points, points1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
            a = [getStringToDisplay(Qtype=Qtype, equation=equation, m=m, i=inclination),
                 getStringToDisplay(Qtype=Qtype, equation=equation1, m=m, i=inclination)]
            generateSVG([equation, equation1], a, str(Qtype), Qtype, [points, points1])
        elif Qtype == 12 or Qtype == 13 or Qtype == 16:
            points = getRandomLinePoints()
            slope = getSlopeFromPoints(points)
            while slope == "&infin;" or slope == 0:
                points = getRandomLinePoints()
                slope = getSlopeFromPoints(points)
            equation = getEqFromPoints(points)
            points1 = getLinePoints(slope=-1 / slope)
            equation1 = getEqFromPoints(points1)
            slope = round(slope, 2)
            question = getQuestion(Qtype, slope, inclination, [points, points1], equation1)
            hints = getHints(Qtype, inclination, points)
            options = getOptions(Qtype, inclination, slope, [equation, equation1], set=angleSet[temp1], points=[points, points1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
            a = [getStringToDisplay(Qtype=Qtype, equation=equation, m=m, i=inclination),
                 getStringToDisplay(Qtype=Qtype, equation=equation1, m=m, i=inclination)]
            generateSVG([equation, equation1], a, str(Qtype), Qtype, [points, points1])
        elif Qtype == 14:
            points = getRandomLinePoints()
            slope = getSlopeFromPoints(points)
            while slope == "&infin;" or slope == 0:
                points = getRandomLinePoints()
                slope = getSlopeFromPoints(points)
            equation = getEqFromPoints(points)
            points1 = getCollinearPoints(equation)
            slope = round(slope, 2)
            question = getQuestion(Qtype, slope, inclination, [points, points1], equation)
            hints = getHints(Qtype, inclination, points)
            options = getOptions(Qtype, inclination, slope, [equation], set=angleSet[temp1], points=[points, points1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
            a = [getStringToDisplay(Qtype=Qtype, equation=equation, m=m, i=inclination),
                 getStringToDisplay(Qtype=Qtype, equation=equation1, m=m, i=inclination)]
            generateSVG([equation], a, str(Qtype), Qtype, [points, points1])
        elif Qtype == 17 or Qtype == 18:
            loop = True
            while loop:
                points1 = getRandomLinePoints()
                points2 = getRandomLinePoints()
                points3 = getRandomLinePoints()
                points4 = getRandomLinePoints()
                slope1 = getSlopeFromPoints(points1)
                slope2 = getSlopeFromPoints(points2)
                slope3 = getSlopeFromPoints(points3)
                slope4 = getSlopeFromPoints(points4)
                if slope1 != "&infin;" and slope2 != "&infin;" and slope3 != "&infin;" and slope4 != "&infin;" and \
                             slope1 != slope2 and slope1 != slope3 and slope1 != slope4 and slope1 != 0:
                    loop = False
            eq1 = getEqFromPoints(points1)
            eq2 = getEqFromPoints(points2)
            eq3 = getEqFromPoints(points3)
            eq4 = getEqFromPoints(points4)
            if Qtype == 18:
                slope1 = -1 / slope1
            points = getLinePoints(slope=slope1)
            equation = getEqFromPoints(points)
            eq = [eq1, eq2, eq3, eq4]
            slope = round(slope1, 2)
            question = getQuestion(Qtype, slope, inclination, [points, points1], equation)
            hints = getHints(Qtype, inclination, points)
            options = getOptions(Qtype, inclination, slope, [equation, equation1], set=angleSet[temp1], points=[points, points1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
            for x in range(4):
                eq0 = eq[x]
                a = [getStringToDisplay(Qtype=Qtype, equation=eq0, m=m, i=inclination)]
                generateSVG([eq0], a, str(Qtype) + "_" + str(x), Qtype)
        elif Qtype == 19:
            points1 = getRandomLinePoints()
            points2 = getRandomLinePoints()
            points3 = getRandomLinePoints()
            points4 = getRandomLinePoints()
            equation = getEqFromPoints(points1)
            loop = True
            while loop:
                p1 = getCollinearPoints(equation)
                if p1[0] != points1[0] and p1[0] != points1[1]:
                    loop = False
            p2 = getRandomLinePoints()
            p3 = getRandomLinePoints()
            p4 = getRandomLinePoints()
            points1.append(p1[0])
            points1.append(p1[1])
            points2.append(p2[0])
            points2.append(p2[1])
            points3.append(p3[0])
            points3.append(p3[1])
            points4.append(p4[0])
            points4.append(p4[1])
            question = getQuestion(Qtype)
            hints = getHints(Qtype)
            options = getOptions(Qtype, eq=[equation], points=[points1, points2, points3, points4], set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
        elif Qtype == 20 or Qtype == 21 or Qtype == 22 or Qtype == 23:
            eq = []
            if Qtype == 20:
                eq = [1, 0, random.randint(-12, 12)]
            elif Qtype == 21:
                eq = [0, 1, random.randint(-12, 12)]
            elif Qtype == 22:
                eq = [1, 0, 0]
            elif Qtype == 23:
                eq = [0, 1, 0]
            question = getQuestion(Qtype, e=eq)
            hints = getHints(Qtype)
            options = getOptions(Qtype, eq=eq, set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
        elif Qtype == 24 or Qtype == 25:
            points1 = getRandomLinePoints()
            y = points1[1]
            loop = True
            while loop:
                points2 = getRandomLinePoints()
                points3 = getRandomLinePoints()
                points4 = getRandomLinePoints()
                x1 = [points2[0], points2[2], points3[0], points3[2], points4[0], points4[2]]
                y1 = [points2[1], points2[3], points3[1], points3[3], points4[1], points4[3]]
                if 0 not in x1 and y not in y1:
                    loop = False
            eq1 = getEqFromPoints(points1)
            eq2 = getEqFromPoints(points2)
            eq3 = getEqFromPoints(points3)
            eq4 = getEqFromPoints(points4)
            eq = [eq1, eq2, eq3, eq4]
            question = getQuestion(Qtype, p=[points1])
            hints = getHints(Qtype)
            options = getOptions(Qtype, eq=eq, set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
        elif Qtype == 26:
            x = random.randint(-12, 12)
            y = random.randint(-12, 12)
            p = [x, y]
            question = getQuestion(Qtype, p=[p])
            hints = getHints(Qtype)
            options = getOptions(Qtype, points=[p], set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
        else:
            points = getLinePoints(slope=slope)
            equation = getEqFromPoints(points)
            question = getQuestion(Qtype, m1, inclination, [points], equation)
            hints = getHints(Qtype, inclination, points)
            options = getOptions(Qtype, inclination, slope, [equation], set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            # print o
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
            a = [getStringToDisplay(Qtype=Qtype, equation=equation, m=m, i=inclination)]
            generateSVG([equation], a, str(Qtype), Qtype, [points])

        temp['Q'] = question
        temp['hints'] = hints
        temp['details'] = feedback
        ques.append(temp)
        print "\n\n"
        print "NEW QUESTION...........................\n"
        print "Question: ", question
        print "Hints: ", hints
        print "Options: ", options
        print "OFmap: ", OFmap
        print "Details: ", feedback
    generateCSV(ques)


def getRandomLinePoints():
    x1 = random.randint(-12, 12)
    y1 = random.randint(-12, 12)
    x2 = random.randint(-12, 12)
    y2 = random.randint(-12, 12)
    return [x1, y1, x2, y2]


def getSlopeFromPoints(points):
    """

    :param points:
    :return:
    """
    x1 = points[0]
    y1 = points[1]
    x2 = points[2]
    y2 = points[3]

    if x2 != x1:
        m = (y2 - y1) * 1.0 / (x2 - x1)
        return m
    else:
        return "&infin;"


def getOppositeInclination(set):
    """

    :param set:
    :return:
    """
    if set == 0 or set == 1 or set == 2 or set == 3:
        return angleSet[set + 4][0]
    else:
        return angleSet[set - 4][0]


def getLinePoints(line=None, slope=0):
    """

    :param line:
    :param slope:
    """
    if not line: line = []
    y1, y2 = 20, 20
    if len(line) > 2:
        a = line[0]
        b = line[1]
        c = line[2]
    else:
        if slope == "&infin;":
            a = random.randint(-12, 12)
            b = 0
        else:
            a = -slope
            b = 1
        c = random.randint(-12, 12)
    x1, x2 = 0, 0
    while y1 > 12 or y1 < -12 or y2 > 12 or y2 < -12 or (x1 == x2 and y1 == y2):
        x1 = random.randint(-12, 12)
        x2 = random.randint(-12, 12)
        if b != 0:
            y1 = ((-a * x1) - c) * 1.0 / b
            y2 = ((-a * x2) - c) * 1.0 / b
        else:
            y1 = random.randint(-12, 12)
            y2 = random.randint(-12, 12)
            x1 = x2
    if x1 % 1 == 0:
        x1 = int(x1)
    # else:
    #     x1 = round(x1, 2)
    if y1 % 1 == 0:
        y1 = int(y1)
    # else:
    #     y1 = round(y1, 2)
    if x2 % 1 == 0:
        x2 = int(x2)
    # else:
    #     x2 = round(x2, 2)
    if y2 % 1 == 0:
        y2 = int(y2)
    # else:
    #     y2 = round(y2, 2)
    return [x1, y1, x2, y2]
    # return [x1, y1, x2, y2]


def getEqFromPoints(points):
    """

    :param points:
    :return:
    """
    x1 = points[0]
    y1 = points[1]
    x2 = points[2]
    y2 = points[3]
    a = y2 - y1
    b = x1 - x2
    c = y1 * (x2 - x1) + x1 * (y1 - y2)
    return [a, b, c]


def getInclination(temp=random.randint(0, 7)):
    """

    :rtype : object
    """
    temp1 = random.randint(0, 1)
    theta = angleSet[temp][temp1]
    # print theta
    return theta


def getSlope(theta):
    """

    :param theta:
    :return:
    """
    theta = math.radians(theta)
    slope = math.tan(theta)
    slopeRatio = Fraction(slope).limit_denominator(max_denominator=10)
    num = slopeRatio.numerator
    denom = slopeRatio.denominator
    if slopeRatio.numerator > 100:
        denom = 0
    return [num, denom]


def getQuestion(Qtype=0, m=0, i=0, p=0, e=0):
    """

    :param Qtype:
    :param m:
    :param i:
    :param p:
    :param e:
    :return:
    """
    if type(p) is list:
        if len(p) > 1:
            p1 = p[1]
        p = p[0]
    ques = ""
    if Qtype == 1 or Qtype == 3:
        ques = "Given an inclination of the line as " + str(i) + " degrees, find the slope of the line"
        ques += "<img>" + str(Qtype) + "</img>"
    elif Qtype == 2:
        ques = "Which of these figures represent a line with slope as " + str(m) + ": "
    elif Qtype == 4 or Qtype == 6:
        ques = "Given that a line passes through the points " + str((p[0], p[1])) + " and " + \
               str((p[2], p[3])) + ", find the slope of the line"
    elif Qtype == 5 or Qtype == 8:
        ques = "Which of the figures represents a slope of " + str(m)
    elif Qtype == 7 or Qtype == 9:
        ques = "Given a line denoted by the equation of a line " + getFormattedEq(e) + ", find the " \
               "slope of the line"
    elif Qtype == 10 or Qtype == 11:
        ques = "If " + str((p[0], 'K')) + " & " + str((p[2], p[3])) + " are parallel to the line passing through" \
               " the points " + str((p1[0], p1[1])) + " and " + str((p1[2], p1[3])) + " Find the value of K "
    elif Qtype == 12 or Qtype == 13:
        ques = "If the line passing through the points" + str((p[0], p[1])) + " & " + str((p[2], p[3])) + \
               " is perpendicular to the line passing through the points " + str((p1[0], p1[1])) + " and " + \
               str((p1[2], 'K')) + " Find the value of K "
    elif Qtype == 14:
        ques = "If " + str((p[0], p[1])) + ", " + str((p[2], 'K')) + " & " + str((p1[0], p1[1])) + " are collinear," \
               " find the value of K"
    elif Qtype == 15:
        ques = "If " + str((p[0], 'K')) + " & " + str((p[2], p[3])) + " are parallel to the line " +\
               getFormattedEq(e) + ", Find the value of K "
    elif Qtype == 16:
        ques = "If the line " + getFormattedEq(e) + " is perpendicular to the line passing through the points " +\
               str((p1[0], p1[1])) + " and " + str((p1[2], 'K')) + ", Find the value of K "
    elif Qtype == 17:
        ques = "Which of these lines is parallel to the line " + getFormattedEq(e)
    elif Qtype == 18:
        ques = "Which of these lines is perpendicular to the line " + getFormattedEq(e)
    elif Qtype == 19:
        ques = "Which of these three points are collinear ?"
    elif Qtype == 20 or Qtype == 21 or Qtype == 22 or Qtype == 23:
        ques = "The equation " + getFormattedEq(e) + " represents"
    elif Qtype == 24 or Qtype == 25:
        ques = "Of the given lines, the line which cuts the axis at " + str((p[0], p[1])) + " is"
    elif Qtype == 26:
        ques = "The point of intersection of lines x=" + str(p[0]) + " and y=" + str(p[1]) + " is"
    return ques


def getOptions(Qtype, i=0, m=0, eq=0, set=0, points=0):
    """

    :param Qtype:
    :param i:
    :param m:
    :param e:
    :param set:
    :return:
    """
    if type(eq) is list:
        if len(eq) > 1:
            e1 = eq[1]
        e = eq[0]
    options = []
    OFmap = []
    sign = random.randint(0, 1)
    index = angleSet.index(set)
    if (type(m) is float or type(m) is long) and m != 0:
        if 1/m > 100 or 1/m < -100:
            inverseM = random.randint(-10, 10)
        else:
            inverseM = 1/m
    if sign == 0:
        # print i
        t = math.sin(math.radians(i))
        if index == 7:
            index = 0
        f = angleSet[index + 1][0]
    else:
        t = math.cos(math.radians(i))
        if index == 0:
            index = 7
        f = angleSet[index - 1][0]
    f = math.tan(math.radians(f))
    if f > 100:
        f = random.randint(-10, 10)

    if Qtype == 1 or Qtype == 3:
        options.append(m)
        options.append(GetNewIfEqual([m], i))
        options.append(GetNewIfEqual([m, i], t))
        options.append(GetNewIfEqual([m, i, t], f))
        OFmap.append(m)
        OFmap.append(round(i, 2))
        OFmap.append(round(t, 2))
        OFmap.append(round(f, 2))
    elif Qtype == 2:
        options.append("<img>2_0</img>")
        options.append("<img>2_1</img>")
        options.append("<img>2_2</img>")
        options.append("<img>2_3</img>")
        OFmap = options
    elif Qtype == 4 or Qtype == 6:
        options.append(m)
        OFmap.append(m)
        if m == "&infin;":
            options.append("0")
            options.append("tan<sup>-1</sup>(90)")
            options.append("tan<sup>-1</sup>(" + str(0) + ")")
            OFmap = options
        else:
            if m == 0:
                options.append("&infin;")
                options.append("tan<sup>-1</sup>(" + str(m) + ")")
                options.append("tan<sup>-1</sup>(" + str(90) + ")")
                OFmap = options
            else:
                t1 = GetNewIfEqual([m], inverseM)
                options.append(t1)
                options.append("tan<sup>-1</sup>(" + str(m) + ")")
                options.append("tan<sup>-1</sup>(" + str(t1) + ")")
                OFmap = options
                OFmap[1] = round(inverseM, 2)
    elif Qtype == 5:
        options.append("Figure 1 : Line connecting coordinates (5,4) and (9,6)")
        options.append("Figure 1 : Line connecting coordinates (4,5) and (9,6)")
        options.append("Figure 1 : Wrong 1")
        options.append("Figure 1 : Wrong 2")
        OFmap = options
    elif Qtype == 7 or Qtype == 9:
        options.append(m)
        t1 = 0
        OFmap.append(m)
        if m == "&infin;":
            options.append("0")
            OFmap.append("0")
            if e[2] != 0:
                t1 = GetNewIfEqual([m, 0], -e[0] / e[2])
                options.append(str(t1))
                OFmap.append(round(-e[0] / e[2], 2))
            else:
                t1 = GetNewIfEqual([m, 0])
                options.append(t1)
                OFmap.append(-1)
            options.append(GetNewIfEqual([m, 0, t1]))
            OFmap.append(-1)
        else:
            if m == 0:
                options.append("&infin;")
                t1 = GetNewIfEqual([m, 0])
                options.append(t1)
                options.append(GetNewIfEqual([m, t1]))
                OFmap.append("&infin;")
                OFmap.append(-1)
                OFmap.append(-1)
            else:
                t1 = GetNewIfEqual([m], inverseM)
                options.append(t1)
                options.append(0)
                options.append(GetNewIfEqual([m, 1 / m, 0], -e[2] / e[1]))
                OFmap.append(round(inverseM, 2))
                OFmap.append(0)
                OFmap.append(round(-e[2] / e[1], 2))
    elif Qtype == 8:
        options.append("Figure 1 : Line with the equation x-2y+3=0")
        options.append("Figure 2 : Line with the equation 2x-y+3=0")
        options.append("Figure 3 : Line with the equation x+2y+3=0")
        options.append("Figure 4: Line Passing through any 2 points whose slope is neither the correct slope "
                       "i.e 1/2 nor reciprocal of the correct slope i.e.2")
        OFmap = options
    elif Qtype == 10 or Qtype == 11 or Qtype == 15:
        wrong = getWrongAnswers(Qtype=Qtype, points=points)
        options.append(points[0][1])
        options.append(wrong[0])
        options.append(wrong[1])
        options.append(wrong[2])
        OFmap = options
    elif Qtype == 12 or Qtype == 13 or Qtype == 16:
        wrong = getWrongAnswers(Qtype=Qtype, points=points)
        options.append(points[1][3])
        options.append(wrong[0])
        options.append(wrong[1])
        options.append(wrong[2])
        OFmap = options
    elif Qtype == 14:
        wrong = getWrongAnswers(Qtype=Qtype, points=points)
        options.append(points[0][3])
        options.append(wrong[0])
        options.append(wrong[1])
        options.append(wrong[2])
        OFmap = options
    elif Qtype == 17:
        options.append("<img>17_0</img>")
        options.append("<img>17_1</img>")
        options.append("<img>17_2</img>")
        options.append("<img>17_3</img>")
        OFmap = options
    elif Qtype == 18:
        options.append("<img>17_0</img>")
        options.append("<img>17_1</img>")
        options.append("<img>17_2</img>")
        options.append("<img>17_3</img>")
        OFmap = options
    elif Qtype == 19:
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]
        p4 = points[3]
        ans1 = str((p1[0], p1[1])) + ", " + str((p1[2], p1[3])) + "and " + str((p1[4], p1[5]))
        ans2 = str((p2[0], p2[1])) + ", " + str((p2[2], p2[3])) + "and " + str((p2[4], p2[5]))
        ans3 = str((p3[0], p3[1])) + ", " + str((p3[2], p3[3])) + "and " + str((p3[4], p3[5]))
        ans4 = str((p4[0], p4[1])) + ", " + str((p4[2], p4[3])) + "and " + str((p4[4], p4[5]))
        options.append(ans1)
        options.append(ans2)
        options.append(ans3)
        options.append(ans4)
        OFmap = options
    elif Qtype == 20 or Qtype == 21 or Qtype == 22 or Qtype == 23:
        op1 = "a line parallel to the Y axis"
        op2 = "a line parallel to the X axis"
        op3 = "the Y axis"
        op4 = "the X axis"
        op5 = "a line parallel to the Y axis but not the Y axis"
        op6 = "a line parallel to the X axis but not the X axis"
        if Qtype == 20:
            options.append(op1)
            options.append(op2)
            options.append(op3)
            options.append(op4)
        elif Qtype == 21:
            options.append(op2)
            options.append(op1)
            options.append(op3)
            options.append(op4)
        elif Qtype == 22:
            options.append(op3)
            options.append(op4)
            options.append(op5)
            options.append(op6)
        elif Qtype == 23:
            options.append(op4)
            options.append(op3)
            options.append(op6)
            options.append(op5)
        OFmap = options
    elif Qtype == 24 or Qtype == 25:
        # print eq
        options.append(getFormattedEq(eq[0]))
        options.append(getFormattedEq(eq[1]))
        options.append(getFormattedEq(eq[2]))
        options.append(getFormattedEq(eq[3]))
        OFmap = options
    elif Qtype == 26:
        p1 = points[0][0]
        p2 = points[0][1]
        loop = True
        while loop:
            p3 = random.randint(-12, 12)
            p4 = random.randint(-12, 12)
            if p3 != p1 and p3 != p2 and p3 != p4:
                loop = False
        options.append(str((p1, p2)))
        if p2 == p1:
            p2 = p1 + 1
        options.append(str((p2, p1)))
        options.append(str((p3, p4)))
        options.append(str((p4, p3)))
        OFmap = options
    return [options, OFmap]


def getOptionsNFeedback(Qtype, option, OFmap):
    """

    :param Qtype:
    :param option:
    :param OFmap:
    :return:
    """
    feedbackStr1 = "Your answer is correct! Let's try the next one"
    feedbackStr2 = "The selected answer is the value inclination and not slope. Value of slope = tan (inclination)"
    feedbackStr3 = "The value of slope is tan (inclination) and not sin (inclination) [or cos (inclination)]"
    feedbackStr4 = "You seem to have misinterpreted the inclination. The right answer is " + str(option[0])
    feedbackStr5 = "The value of inclination is such that the line falls in the first quadrant hence the value of " \
                   "slope i.e tan (inclination) cannot be negative"
    feedbackStr6 = "The line described is not of the type x = a and intersects the X axis as can be visibly seen. " \
                   "Hence your answer is incorrect"
    feedbackStr7 = "The line described is not of the type y = b and intersects the Y axis as can be visibly seen. " \
                   "Hence your answer is incorrect"
    feedbackStr8 = "You seem to have used an incorrect formula for calculating the slope which probably " \
                   "explains why the selected answer is the reciprocal of the slope. Let's try the next one"
    feedbackStr9 = "You have selected the answer for inclination  by computing tan<sup>-1</sup> (slope) which is the " \
                   "incorrect answer. Let's try the next one"
    feedbackStr10 = "Unfortunately the selected answer is incorrect. Let's try the next one"
    feedbackStr11 = "The selected option is reciprocal of the value of slope. Please check the formula for slope. "
    feedbackStr12 = "The selected option is parallel to X (or Y) Axis and hence incorrect. Let's try the next one"
    options = []
    feedback = []
    if Qtype == 1 or Qtype == 3:
        feedback = [feedbackStr1, feedbackStr2, feedbackStr3, feedbackStr4]
    elif Qtype == 2:
        feedback = [feedbackStr1, feedbackStr5, feedbackStr6, feedbackStr7]
        count = 0
    elif Qtype == 4 or Qtype == 6:
        feedback = [feedbackStr1, feedbackStr8, feedbackStr9, feedbackStr10]
    elif Qtype == 5:
        feedback = [feedbackStr1, feedbackStr11, feedbackStr12, feedbackStr10]
    elif Qtype == 7 or Qtype == 9:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 8:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 10 or Qtype == 11 or Qtype == 15:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 12 or Qtype == 13 or Qtype == 16:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 14:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 17:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 18:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 19:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 20 or Qtype == 21:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 22 or Qtype == 23:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 24 or Qtype == 25:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    elif Qtype == 26:
        feedback = [feedbackStr1, feedbackStr10, feedbackStr10, feedbackStr10]
    count = 0
    for x in option:
        if type(option[count]) is float:
            option[count] = round(option[count], 2)
        temp = {'option': option[count]}
        if count == 0:
            temp['correct'] = True
        else:
            temp['correct'] = False
        if option[count] == OFmap[count]:
            temp['feedback'] = feedback[count]
        else:
            temp['feedback'] = feedbackStr10
        options.append(temp)
        count += 1
    options = random.sample(options, 4)
    return options


def getHints(Qtype=0, i=0, p=None):
    """

    :param Qtype:
    :param i:
    :param p:
    :return:
    """
    if not p: p = [0, 1, 2, 3]   ## Just for initialization
    hintStr1 = "Identify the angle made between the line and the X axis. Check the figure and see if you can find " \
               "the angle"
    hintStr2 = "The value of slope of the line = tan (inclination in degrees or radians)"
    hintStr3 = "The inclination is " + str(i) + " degrees and hence the slope is tan(" + str(i) + ")"
    hintStr4 = "If the value of slope = 1 then the value of inclination should be either 45 degrees (or \/4c) or " \
               "225 degrees (or 5\/4c)"
    hintStr5 = "Identify the angle made between the line and the X axis."
    hintStr6 = "Use the equation for slope when given two points i.e. slope = (y2-y1) / (x2-x1)"
    hintStr7 = "Substitute appropriate values of x1,y1,x2 and y2 in the equation mentioned in the previous hint"
    hintStr8 = "Put x1 = " + str(p[0]) + ", y1 = " + str(p[1]) + ",  x2 = " + str(p[2]) + " " \
               "and y2 = " + str(p[3]) + " in the equation given in Hint 1 to get the answer for slope"
    hintStr9 = "Since the value of the slope is positive, the inclination angle should be either between 0 to 90 " \
               "degrees or 180 to 270 degrees"
    hintStr10 = "Since the value of the slope is negative, the inclination angle should be either between 90 to 180 " \
                "degrees or 270 to 360 degrees"
    hintStr11 = "Substitute appropriate values of x1,y1,x2 and y2 from each of the figures in the equation " \
                "mentioned in the previous hint to find slope"
    hint = []
    if Qtype == 1:
        hint.append(hintStr1)
        hint.append(hintStr2)
        hint.append(hintStr3)
    elif Qtype == 2:
        hint.append(hintStr1)
        hint.append(hintStr2)
        hint.append(hintStr4)
    elif Qtype == 3:
        hint.append(hintStr5)
        hint.append(hintStr2)
        hint.append(hintStr3)
    elif Qtype == 4 or Qtype == 6:
        hint.append(hintStr6)
        hint.append(hintStr7)
        hint.append(hintStr8)
    elif Qtype == 5:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 7 or Qtype == 9:
        hint.append(hintStr6)
        hint.append(hintStr7)
        hint.append(hintStr8)
    elif Qtype == 8:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 10 or Qtype == 11:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 12 or Qtype == 13:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 14:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 15:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 16:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 17:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 18:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 19:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 20 or Qtype == 21 or Qtype == 22 or Qtype == 23:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 24 or Qtype == 25:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 26:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    return hint


def getWrongAnswers(Qtype=0, points=None):
    if not points: points = []
    p1 = points[0]

    x1 = p1[0]
    y1 = p1[1]
    x2 = p1[2]
    y2 = p1[3]
    if len(points) > 1:
        if Qtype == 14:
            p2 = points[1]
            x3 = p2[0]
            y3 = p2[1]
        else:
            p2 = points[1]
            x3 = p2[0]
            y3 = p2[1]
            x4 = p2[2]
            y4 = p2[3]

    wrong = []
    if Qtype == 10 or Qtype == 11 or Qtype == 15:
        if y2 == 0:
            y2 = random.randint(1, 12)
        if x3 == x4:
            x4 = x3 + 1
        t1 = ((y4 - y3) / (x4 - x3)) * (x2 - x1) - y1
        t2 = GetNewIfEqualInt([t1])
        t3 = GetNewIfEqualInt([t1, t2])
        wrong.append(t1)
        wrong.append(t2)
        wrong.append(t3)

    if Qtype == 12 or Qtype == 13 or Qtype == 16:
        if y3 == 0:
            y3 = random.randint(1, 12)
        if x2 == x1:
            x2 = x1 + 1
        t1 = ((y2 - y1) / (x2 - x1)) * (x4 - x3) - y3
        t2 = GetNewIfEqualInt([t1])
        t3 = GetNewIfEqualInt([t1, t2])
        wrong.append(t1)
        wrong.append(t2)
        wrong.append(t3)

    if Qtype == 14:
        if y1 == 0:
            y1 = random.randint(1, 12)
        if x3 == x1:
            x3 = x1 + 1
        t1 = ((y3 - y1) / (x3 - x1)) * (x2 - x1) - y1
        t2 = GetNewIfEqualInt([t1])
        t3 = GetNewIfEqualInt([t1, t2])
        wrong.append(t1)
        wrong.append(t2)
        wrong.append(t3)

    return wrong


def getCollinearPoints(equation):
    a = equation[0]
    b = equation[1]
    c = equation[2]
    loop = True
    while loop:
        x = random.randint(-11, 11)
        if b != 0:
            y = ((-a * 1.0 * x) - c) / b
        else:
            x = -c * 1.0 / a
            y = random.randint(-11, 11)
        if 11 >= x >= -11 and 11 >= y >= -11:
            loop = False
    return [x, y]


def getFormattedEq(eq):
    """


    :rtype : object
    :param eq: 
    :return: 
    """
    temp = ""
    if eq[0] != 0:
        if eq[0] % 1 == 0:
            eq[0] = int(eq[0])
        else:
            eq[0] = round(eq[0], 2)
        temp += GetCoeffString(eq[0]) + "x"
    if eq[1] != 0:
        if eq[1] % 1 == 0:
            eq[1] = int(eq[1])
        else:
            eq[1] = round(eq[1], 2)
        if eq[0] == 0:
            temp += GetCoeffString(eq[1]) + "y"
        else:
            if eq[1] == 1:
                temp += "+y"
            elif eq[1] == -1:
                temp += "-y"
            else:
                temp += getSignedString(eq[1]) + "y"
    if eq[2] != 0:
        if eq[2] % 1 == 0:
            eq[2] = int(eq[2])
        else:
            eq[2] = round(eq[2], 2)
        temp += getSignedString(eq[2])
    temp += " = 0"
    return temp


def getStringToDisplay(Qtype, equation=0, m=0, i=0):
    """

    :param Qtype: 
    :param equation: 
    :param m: 
    :param i: 
    :return: 
    """
    if Qtype == 1 or Qtype == 2:
        display = "inclination: " + str(i) + " degree"
    elif Qtype == 7 or Qtype == 8:
        display = getFormattedEq(equation)
    else:
        display = getFormattedEq(equation)
    return display

cordinateGeo()