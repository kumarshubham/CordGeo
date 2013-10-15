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


def coordinateGeo(assess, num=3, name="test"):
    """

    :param startIndex:
    :param lastIndex:
    """
    Mtype = 1
    Mtype1 = 2
    ques = []
    withImages = [1, 2, 4, 5, 7, 8, 10, 12, 15, 16, 17, 18, 19]
    withoutImages = [3, 6, 9, 11, 13, 14] + range(20, 44)
    if num == 1:
        assess = [val for val in assess if val in withImages]
    elif num == 2:
        assess = [val for val in assess if val in withoutImages]
    count = 0
    for x in assess:
        count += 1
        typeSet1 = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
        temp = {}
        Qtype = x
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
            hints = getHints(Qtype, inclination, points, m=m1)
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
            m = round(slope1, 2)
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
            hints = getHints(Qtype, inclination, points, e=equation, m=m, inversM=slope)
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
            x = points1[0]
            loop = True
            while loop:
                points2 = getRandomLinePoints()
                points3 = getRandomLinePoints()
                points4 = getRandomLinePoints()
                x1 = [points2[0], points2[2], points3[0], points3[2], points4[0], points4[2]]
                y1 = [points2[1], points2[3], points3[1], points3[3], points4[1], points4[3]]
                if Qtype == 24:
                    if 0 not in x1 and y not in y1:
                        loop = False
                        points1[0] = 0
                if Qtype == 25:
                    if 0 not in y1 and x not in x1:
                        loop = False
                        points1[1] = 0
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
            feedback = getOptionsNFeedback(Qtype, options, OFmap, p=points1)
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
        elif Qtype in typeSet1:
            loop = True
            while loop:
                points = getRandomLinePoints()
                if (points[0] != points[2]) and (points[1] != points[3]) and (points[0] != 0) and (points[1] != 0) and \
                        (points[2] != 0) and (points[3] != 0):
                    loop = False
            eq = getEqFromPoints(points)
            question = getQuestion(Qtype,p=[points], e=eq)
            hints = getHints(Qtype)
            options = getOptions(Qtype, eq=[eq], points=[points], set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
        elif Qtype == 40 or Qtype == 41:
            temp1 = random.sample([1, 3, 5, 7], 1)[0]
            points = getRandomLinePoints()
            if Qtype == 40:
                inclination = getInclination(temp=temp1, pi=True)
            elif Qtype == 41:
                inclination = getInclination(temp=temp1)
            inclination1 = getInclination(temp=temp1)
            m = getSlope(inclination1)
            question = getQuestion(Qtype,i=inclination,p=[points])
            hints = getHints(Qtype)
            options = getOptions(Qtype,m=m,i=inclination1,points=[points],set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
        elif Qtype == 42:
            points = getRandomLinePoints()
            if points[0] != 0 and points[2] != 0:
                points[0] = 0
            m = getSlopeFromPoints(points)
            question = getQuestion(Qtype,m=m,p=[points])
            hints = getHints(Qtype)
            options = getOptions(Qtype, m=m, points=points, set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
        elif Qtype == 43:
            points = getRandomLinePoints()
            points[1] = 0
            eq = getEqFromPoints(points)
            equation = [eq[0], eq[1], eq[2] + 6]
            question = getQuestion(Qtype,p=[points],e=equation)
            hints = getHints(Qtype)
            options = getOptions(Qtype,eq=eq,set=angleSet[temp1])
            OFmap = options[1]
            options = options[0]
            feedback = getOptionsNFeedback(Qtype, options, OFmap)
        else:
            points = getLinePoints(slope=slope)
            equation = getEqFromPoints(points)
            question = getQuestion(Qtype, m1, inclination, [points], equation)
            hints = getHints(Qtype, inclination, points, e=equation)
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
        print temp
        ques.append(temp)
        print "\n\n"
        print "NEW QUESTION...........................\n"
        print Qtype
        print "Question: ", question
        print "Hints: ", hints
        print "Options: ", options
        print "OFmap: ", OFmap
        print "Details: ", feedback
    generateCSV(ques, name)
    print "Done ", count


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


def getInclination(temp=random.randint(0, 7), pi=False):
    """

    :rtype : object
    """
    temp1 = random.randint(0, 1)
    theta = angleSet[temp][temp1]
    if pi:
        if temp == 1:
            theta = "&Pi;/6"
        elif temp == 3:
            theta = "&Pi;/3"
        elif temp == 5:
            theta = "2&Pi;/3"
        elif temp == 7:
            theta = "5&Pi;/6"
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
        c1 = 0
        for x in p:
            c2 = 0
            for y in x:
                if y % 1 == 0:
                    p[c1][c2] = int(p[c1][c2])
                else:
                    p[c1][c2] = round(p[c1][c2], 2)
                c2 += 1
            c1 += 1
        if len(p) > 1:
            p1 = p[1]
        p = p[0]
    ques = ""
    if Qtype == 1 or Qtype == 3:
        ques = "Given an inclination of the line as " + "$" + str(i) + "$" + " degrees, find the slope of the line"
        if Qtype == 1:
            ques += "<img>" + str(Qtype) + "</img>"
    elif Qtype == 2:
        ques = "Which of these figures represent a line with slope as " + "$" + str(m) + "$" + ": "
    elif Qtype == 4 or Qtype == 6:
        ques = "Given that a line passes through the points " + "$" + str((p[0], p[1])) + "$" + " and " + \
               "$" + str((p[2], p[3])) + "$" + ", find the slope of the line"
    elif Qtype == 5 or Qtype == 8:
        ques = "Which of the figures represents a slope of " + "$" + str(m) + "$"
    elif Qtype == 7 or Qtype == 9:
        ques = "Given a line denoted by the equation of a line " + getFormattedEq(e) + ", find the " \
               "slope of the line"
    elif Qtype == 10 or Qtype == 11:
        ques = "If " + "$" + str((p[0], 'K')) + "$" + " & " + "$" + str((p[2], p[3])) + "$" + " are parallel to the line passing through" \
               " the points " + "$" + str((p1[0], p1[1])) + "$" + " and " + "$" + str((p1[2], p1[3])) + "$" + " Find the value of K "
    elif Qtype == 12 or Qtype == 13:
        ques = "If the line passing through the points" + "$" + str((p[0], p[1])) + "$" + " & " + "$" + str((p[2], p[3])) + \
               "$" + " is perpendicular to the line passing through the points " + "$" + str((p1[0], p1[1])) + "$" + " and " + \
               "$" + str((p1[2], 'K')) + "$" + " Find the value of K "
    elif Qtype == 14:
        ques = "If " + "$" + str((p[0], p[1])) + ", " + str((p[2], 'K')) + "$" + " & " + "$" + str((p1[0], p1[1])) + "$" + " are collinear," \
               " find the value of K"
    elif Qtype == 15:
        ques = "If the line " + getFormattedEq(e) + " is parallel to the line passing through the points " +\
               "$" + str((p[0], 'K')) + "$" + " and " + "$" + str((p[2], p[3])) + "$" + ", Find the value of K "
    elif Qtype == 16:
        ques = "If the line " + getFormattedEq(e) + " is perpendicular to the line passing through the points " +\
               "$" + str((p1[0], p1[1])) + "$" + " and " + "$" + str((p1[2], 'K')) + "$" + ", Find the value of K "
    elif Qtype == 17:
        ques = "Which of these lines is parallel to the line " + getFormattedEq(e)
    elif Qtype == 18:
        ques = "Which of these lines is perpendicular to the line " + getFormattedEq(e)
    elif Qtype == 19:
        ques = "Which of these three points are collinear ?"
    elif Qtype == 20 or Qtype == 21 or Qtype == 22 or Qtype == 23:
        ques = "The equation " + getFormattedEq(e) + " represents"
    elif Qtype == 24 or Qtype == 25:
        ques = "Of the given lines, the line which cuts the axis at " + "$" + str((p[0], p[1])) + "$" + " is"
    elif Qtype == 26:
        ques = "The point of intersection of lines $ x=" + str(p[0]) + "$" + " and $ y=" + str(p[1]) + "$" + " is"
    elif Qtype == 27 or Qtype == 28 or Qtype == 29 or Qtype == 30 or Qtype == 31 or Qtype == 32:
        form = {27: 'Slope-Point', 28: 'Slope-Intercept', 29: 'Two-Points', 30: 'Double-Intercept', 31: 'Parametric',
                32: 'Normal'}
        ques = "Which of these equation represent a line in " + form[Qtype] + " form"
    elif Qtype == 33 or Qtype == 34 or Qtype == 35 or Qtype == 36 or Qtype == 37 or Qtype == 38 or Qtype == 39:
        form = {33: 'SP', 34: 'SI', 35: 'TP', 36: 'DI', 37: 'P', 38: 'Po', 39: 'N'}
        ques = "The equation \'" + getFormattedEq(eq=e, eqtype=form[Qtype], points=p) + "\' is in "
    elif Qtype == 40:
        ques = "The equation of a line whose inclination is " + "$" + str(i) + "$" + " and passes through the point " + \
               "$" + str((p[0], p[1])) + "$" + " is"
    elif Qtype == 41:
        ques = "The equation of a line whose inclination is " + "$" + str(i) + "$" + " degree and passes through the point " + \
               "$" + str((p[0], p[1])) + "$" + " is"
    elif Qtype == 42:
        ques = "If a line has slope as " + "$" + str(round(m, 2)) + "$" + ", cuts the Y axis at " + "$" + str((p[0], p[1])) + "$" + ", its equation" \
               " would be"
    elif Qtype == 43:
        ques = "If a line is parallel to the line " + getFormattedEq(e) + " and has x intercept as " + "$" + str(p[0]) + \
               "$" + ", its equation would be"
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
                if m == 1 or m == -1:
                    t1 = GetNewIfEqual([m])
                else:
                    t1 = GetNewIfEqual([m], inverseM)
                options.append(t1)
                t2 = "tan<sup>-1</sup>(" + str(m) + ")"
                t3 = "tan<sup>-1</sup>(" + str(t1) + ")"
                options.append(t2)
                options.append(t3)
                OFmap = [m, inverseM, t2, t3]
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
    elif Qtype == 27 or Qtype == 28 or Qtype == 29 or Qtype == 30 or Qtype == 31 or Qtype == 32:
        eqType = {27: ["SP", "SI", "TP", "DI"], 28: ["SI", "SP", "TP", "DI"], 29: ["TP", "SP", "SI", "DI"],
                  30: ["DI", "SP", "SI", "TP"], 31: ["P", "N", "PY", "PX"], 32: ["N", "P", "PY", "PX"]}
        op1 = getFormattedEq(eq[0],eqtype=eqType[Qtype][0], points=points[0])
        op2 = getFormattedEq(eq[0],eqtype=eqType[Qtype][1], points=points[0])
        op3 = getFormattedEq(eq[0],eqtype=eqType[Qtype][2], points=points[0])
        op4 = getFormattedEq(eq[0],eqtype=eqType[Qtype][3], points=points[0])
        options.append(op1)
        options.append(op2)
        options.append(op3)
        options.append(op4)
        OFmap = options
    elif Qtype == 33 or Qtype == 34 or Qtype == 35 or Qtype == 36 or Qtype == 37 or Qtype == 38 or Qtype == 39:
        form = {33: 'Slope-Point', 34: 'Slope-Intercept', 35: 'Two-Points', 36: 'Double-Intercept', 37: 'Parametric',
                38: 'Polar', 39: 'Normal'}
        eqType = {33: [33, 34, 35, 36], 34: [34, 33, 35, 36], 35: [35, 33, 36, 34], 36: [36, 33, 34, 35],
                  37: [37, 39, 33, 34], 38: [38, 39, 33, 34], 39: [39, 38, 35, 36]}
        options.append(form[eqType[Qtype][0]] + " form")
        options.append(form[eqType[Qtype][1]] + " form")
        options.append(form[eqType[Qtype][2]] + " form")
        options.append(form[eqType[Qtype][3]] + " form")
        OFmap = options
    elif Qtype == 40 or Qtype == 41:
        def op(inc, point, m, reverseI, num):
            c = point[1] - (m[0] / m[1] * point[0])
            if num == 3 or num == 4:
                c = -c + 1
            if num == 2 or num == 3:
                inc = reverseI
            m1 = getFormattedSlope(inc, "eq")
            eq = "$ y = " + m1 + "(x" + getSignedString(c) + ") $"
            return eq
        reverseI = i
        if i in set2:
            reverseI = angleSet[3][0]
        elif i in set4:
            reverseI = angleSet[1][0]
        elif i in set6:
            reverseI = angleSet[7][0]
        elif i in set8:
            reverseI = angleSet[5][0]
        op1 = op(i, points[0], m, reverseI, 1)
        op2 = op(i, points[0], m, reverseI, 2)
        op3 = op(i, points[0], m, reverseI, 3)
        op4 = op(i, points[0], m, reverseI, 4)
        options = [op1, op2, op3, op4]
        OFmap = options

    elif Qtype == 42:
        eq = getEqFromPoints(points)
        op1 = getFormattedEq(eq)
        op2 = getFormattedEq([eq[0], eq[1], eq[2] + 4])
        op3 = getFormattedEq([eq[0], eq[1], eq[2] + 8])
        op4 = getFormattedEq([eq[0], eq[1], eq[2] - 4])
        options = [op1, op2, op3, op4]
        OFmap = options

    elif Qtype == 43:
        op1 = getFormattedEq(eq)
        op2 = getFormattedEq([eq[0], -eq[1], eq[2] + 4])
        op3 = getFormattedEq([eq[0], -eq[1], eq[2] + 8])
        op4 = getFormattedEq([-eq[0], eq[1], eq[2] - 4])
        options = [op1, op2, op3, op4]
        OFmap = options

    return [options, OFmap]


def getOptionsNFeedback(Qtype, option, OFmap, p=None):
    """

    :param Qtype:
    :param option:
    :param OFmap:
    :return:
    """
    if not p: p = [0, 1]
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

    ## for 1.1.3
    feedbackStr13 = "Your answer is incorrect as you have used the formula -b/a which is the reciprocal " \
                    "of the slope. The correct formula for slope of a line $ ax+by+c = 0 $ is $ -\\frac{a}{b} $"
    feedbackStr14 = "Your answer is incorrect since you have incorrectly used -c/a as the formula for slope. " \
                    "The correct formula for slope of a line $ ax+by+c = 0 $ is $ -\\frac{a}{b} $"
    feedbackStr15 = "Your answer is incorrect since you have incorrectly used -c/a as the formula for slope. " \
                    "The correct formula for slope of a line $ ax+by+c = 0 $ is $ -\\frac{a}{b} $"
    feedbackStr16 = "Your answer is incorrect since the slope of the selected line is " + str(option[0])

    # for 1.1.4 and 1.1.5
    feedbackStr17 = "You seem to have used the formula for parallel lines incorrect as $ m1 = - m2 $"
    feedbackStr18 = "You seem to have used the formula for perpendicular lines $ (m1*m2 = -1) $ and " \
                    "not parallel lines $ (m1 = m2) $"
    feedbackStr19 = "You seem to have used the formula for parallel lines $ (m1 = m2) $ and not  " \
                    "perpendicular lines $ (m1*m2 = -1) $ "
    feedbackStr20 = "You seem to have used the formula for perpendicular lines incorrectly since " \
                    "$ m1*m2 = -1 $ and not 1"
    feedbackStr21 = "The selected option is incorrect since it makes the lines perpendicular"

    #for 1.2.1
    feedbackStr22 = "Since the equation is of the type $ x = a $ and not $ y = b $, it cannot be parallel to the X axis"
    feedbackStr23 = "The equation is of the type $ x = a $ but a is not zero hence it is not the Y axis"
    feedbackStr24 = "Since the equation is of the type $ y = b $ and not $ x = a $, it cannot be parallel to the Y axis"
    feedbackStr25 = "The equation for the X axis is $ y = 0 $ and not $ x = 0 $"
    feedbackStr26 = "The equation is of the type $ x = a $ but $ a = 0 $ hence it is the Y axis"
    feedbackStr27 = "The equation for the Y axis is $ x = 0 $ and not $ y = 0 $"
    feedbackStr28 = "The equation is of the type $ y = b $ but $ b = 0 $ hence it is the X axis"
    feedbackStr29 = "In the form $ y = mx + c $, m is the slope and c is the Y coordinate  and not the X coordinate"
    feedbackStr30 = "The point $ " + str((p[0], p[1])) + " $ does not lie on the line denoted by the selected equation"
    feedbackStr31 = "In the form $ x = -\\frac{1}{m}x + c $, m is the slope and c is the X coordinate  " \
                    "and not the Y coordinate"
    feedbackStr33 = "The point of intersection should satisfy both the line equations which is not true in this case"
    feedbackStr34 = "The equation is of the type x = b but b is not zero hence it is not the X axis"

    # for 1.2.2
    form = {27: 'Slope-Point', 28: 'Slope-Intercept', 29: 'Two-Points', 30: 'Double-Intercept', 31: 'Polar/Parametric',
                32: 'Normal'}
    if Qtype in form:
        feedbackStr35 = "The selected equation is in the form $ y = mx + c $ which is the slope intercept " \
                        "form and not the " + form[Qtype] + " form"
        feedbackStr36 = "The selected equation is in the form $ \\frac{y-y1}{y1-y2} = \\frac{x-x1}{x1-x2} $" \
                        "which is the two points form and not the " + form[Qtype] + " form"
        feedbackStr37 = "The selected equation is in the form $ \\frac{x}{a} + \\frac{y}{b} = 1 $ which is the double "\
                        "intercept form and not the " + form[Qtype] + " form"
        feedbackStr38 = "The selected equation is in the form $ y-y1 = m(x -x1) $ which is the " \
                        "slope point form and not the " + form[Qtype] + " form"
        feedbackStr39 = "The equation is in normal form and not polar / parametric form"
        feedbackStr40 = "The equation is of the type y = b and hence not in " + form[Qtype] + " form"
        feedbackStr41 = "The equation is of the type x = a and hence not in " + form[Qtype] + " form"
        feedbackStr42 = "The equation is in polar / parametric form and not normal form"

    # for 1.2.3
    feedbackStr43 = "Incorrect Answer since the equation for slope intercept form is of the type $ y = mx + c $"
    feedbackStr44 = "Incorrect Answer since the equation for two points form is of the type " \
                    "$ \\frac{y-y1}{y1-y2} = \\frac{x-x1}{x1-x2} $"
    feedbackStr45 = "Incorrect answer since the equation for double intercept form is of the type " \
                    "$ \\frac{x}{a} + \\frac{y}{b} = 1 $"
    feedbackStr46 = "Incorrect Answer since the equation for slope point form is of the type $ y-y1 = m(x -x1) $"
    feedbackStr47 = "Incorrect Answer since the equation for normal form is of the type " \
                    "$ x cos&Theta; + y sin&Theta; = d $"
    feedbackStr48 = "Incorrect Answer since the equation for polar / parametric form is of the type " \
                    "$ y = y1 +a cos&Theta; ; x = x1 +asin&Theta; $"
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
        feedback = [feedbackStr1, feedbackStr13, feedbackStr14, feedbackStr15]
    elif Qtype == 8:
        feedback = [feedbackStr1, feedbackStr16, feedbackStr16, feedbackStr10]
    elif Qtype in [10, 11, 14, 15, 17]:
        feedback = [feedbackStr1, feedbackStr17, feedbackStr18, feedbackStr10]
    elif Qtype in [12, 13, 16, 18]:
        feedback = [feedbackStr1, feedbackStr19, feedbackStr20, feedbackStr10]
    elif Qtype == 19:
        feedback = [feedbackStr1, feedbackStr17, feedbackStr21, feedbackStr10]
    elif Qtype == 20:
        feedback = [feedbackStr1, feedbackStr22, feedbackStr23, feedbackStr10]
    elif Qtype == 21:
        feedback = [feedbackStr1, feedbackStr24, feedbackStr34, feedbackStr10]
    elif Qtype == 22:
        feedback = [feedbackStr1, feedbackStr25, feedbackStr26, feedbackStr10]
    elif Qtype == 23:
        feedback = [feedbackStr1, feedbackStr27, feedbackStr28, feedbackStr10]
    elif Qtype == 24:
        feedback = [feedbackStr1, feedbackStr29, feedbackStr30, feedbackStr30]
    elif Qtype == 25:
        feedback = [feedbackStr1, feedbackStr31, feedbackStr30, feedbackStr30]
    elif Qtype == 26:
        feedback = [feedbackStr1, feedbackStr33, feedbackStr33, feedbackStr33]
    elif Qtype == 27:
        feedback = [feedbackStr1, feedbackStr35, feedbackStr36, feedbackStr37]
    elif Qtype == 28:
        feedback = [feedbackStr1, feedbackStr38, feedbackStr36, feedbackStr37]
    elif Qtype == 29:
        feedback = [feedbackStr1, feedbackStr38, feedbackStr35, feedbackStr37]
    elif Qtype == 30:
        feedback = [feedbackStr1, feedbackStr38, feedbackStr35, feedbackStr36]
    elif Qtype == 31:
        feedback = [feedbackStr1, feedbackStr39, feedbackStr40, feedbackStr41]
    elif Qtype == 32:
        feedback = [feedbackStr1, feedbackStr42, feedbackStr40, feedbackStr41]
    elif Qtype == 33:
        feedback = [feedbackStr1, feedbackStr43, feedbackStr44, feedbackStr45]
    elif Qtype == 34:
        feedback = [feedbackStr1, feedbackStr46, feedbackStr44, feedbackStr45]
    elif Qtype == 35:
        feedback = [feedbackStr1, feedbackStr46, feedbackStr45, feedbackStr43]
    elif Qtype == 36:
        feedback = [feedbackStr1, feedbackStr46, feedbackStr43, feedbackStr44]
    elif Qtype == 37:
        feedback = [feedbackStr1, feedbackStr47, feedbackStr46, feedbackStr43]
    elif Qtype == 38:
        feedback = [feedbackStr1, feedbackStr47, feedbackStr46, feedbackStr43]
    elif Qtype == 39:
        feedback = [feedbackStr1, feedbackStr48, feedbackStr44, feedbackStr45]
    elif Qtype == 40 or Qtype == 41 or Qtype == 42 or Qtype == 43:
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


def getHints(Qtype=0, i=0, p=None, e=None, m=0, inverseM=0):
    """

    :param Qtype:
    :param i:
    :param p:
    :return:
    """
    if not p: p = [0, 1, 2, 3]   ## Just for initialization
    if not e: e = [0, 1, 2]
    hintStr1 = "Identify the angle made between the line and the X axis. Check the figure and see if you can find " \
               "the angle"
    hintStr2 = "The value of slope of the line = tan (inclination in degrees or radians)"
    hintStr3 = "The inclination is " + str(i) + " degrees and hence the slope is tan(" + str(i) + ")"
    hintStr4 = "If the value of slope = 1 then the value of inclination should be either 45 degrees (or \/4c) or " \
               "225 degrees (or 5\/4c)"
    hintStr5 = "Identify the angle made between the line and the X axis."
    hintStr6 = "Use the equation for slope when given two points i.e. slope $ = \\frac{y2-y1}{x2-x1} $"
    hintStr7 = "Substitute appropriate values of x1,y1,x2 and y2 in the equation mentioned in the previous hint"
    hintStr8 = "Put x1 = " + str(p[0]) + ", y1 = " + str(p[1]) + ",  x2 = " + str(p[2]) + " " \
               "and y2 = " + str(p[3]) + " in the equation given in Hint 1 to get the answer for slope"
    hintStr9 = "Since the value of the slope is positive, the inclination angle should be either between 0 to 90 " \
               "degrees or 180 to 270 degrees"
    hintStr10 = "Since the value of the slope is negative, the inclination angle should be either between 90 to 180 " \
                "degrees or 270 to 360 degrees"
    hintStr11 = "Substitute appropriate values of x1,y1,x2 and y2 from each of the figures in the equation " \
                "mentioned in the previous hint to find slope"
    hintStr12 = "Arrange the equation in the form $ ax + by + c = 0 $"
    hintStr13 = "Find the values of a and b as per the standard equation and use the formula for slope i.e. $ m =" \
                " -\\frac{a}{b} $"
    hintStr14 = "In this case $ a = " + str(e[0]) + " $ and $ b = " + str(e[1]) + " $"
    hintStr15 = "Find the slopes of each line given by slope $ = -\\frac{a}{b} $"
    hintStr16 = "Compare the slopes with " + str(m) + " to find the correct option"
    hintStr17 = "Since both the lines are parallel to each other their slopes i.e. m1 and m2 would be equal"
    hintStr18 = "Find the equations of the two lines and derive the value of slope "
    hintStr19 = "Equate the values of slope to get the value of K"
    hintStr20 = "Since both the lines are perpendicular to each other $ m1*m2 = -1 $ considering m1 and m2 " \
                "are the slopes of line 1 and line 2 respectively"
    hintStr21 = "Find the equations of the two lines and derive the value of slope . Let them be m1 and m2 respectively"
    hintStr22 = "Substitute the values of m1 and m2 in $ m1*m2 = -1 $ to get the value of K"
    hintStr23 = "Since the three points are collinear, lines drawn through any two of the three points " \
                "would be parallel i.e their slopes would be equal"
    hintStr24 = "Find the equations of the two lines taking two points at a time while ensuring " \
                "that the same points are not repeated and one of the points is K in one of the lines"
    hintStr25 = "Find the slopes m1 and m2 of the two lines and equate the values of slope to get the value of K"
    hintStr26 = "Find the slope of the equation "
    hintStr27 = "Use the fact that for parallel lines, m1 = m2 . Equate the value of m1 with the equation " \
                "for slope of m2 considering two points"
    hintStr28 = "Use the fact that for perpendicular lines, $ m1*m2 = -1 $. Equate the value of $ -\\frac{1}{m1} $" \
                "with the equation for slope of m2 considering two points"
    hintStr29 = "Find the slope of the line " + getFormattedEq(e) + " using the formula $ -\\frac{a}{b} $"
    hintStr30 = "Since you need to find the parallel line, select the line which has slope " \
                "equal to the line " + getFormattedEq(e)
    hintStr31 = "Since the slope of the line " + getFormattedEq(e) + " is " + str(m) + ", the correct option " \
                "would also have the slope " + str(m)
    hintStr32 = "Since you need to find the perpendicular line, select the line which has slope equal to the " \
                "negative reciprocal of the slope of the line " + getFormattedEq(e)
    hintStr33 = "Since the slope of the line " + getFormattedEq(e) + " is " + str(m) + ", the correct option " \
                "would have the slope as " + str(inverseM) + " which would make $ m1*m2 = -1 $"
    hintStr34 = "Find the slope of the line joining the any two of the three points given. Do this for two combinations"
    hintStr35 = "Find the combination where m1 = m2 to show that they are parallel " \
                "(also collinear since there would be a common point)"
    hintStr36 = "Identify the type of equation i.e is it of the type $ x = a $ or $ y = b $"
    hintStr37 = "If the given equation is of the type x = a, it will be parallel to the Y axis and " \
                "if the equation is of the type y = b it will be parallel to X axis"
    hintStr38 = "Note that if a or b are 0 then the equation would be $ x = 0 $ or $ y = 0 $" \
                "which represents Y axis or X axis respectively"
    hintStr39 = "Since the Y intercept is given, the equation representing the line should be of the " \
                "type $ y = mx + c $ with  c = Y intercept on  axis"
    hintStr40 = "Y intercept = 4"
    hintStr41 = "Since the X intercept is given, the equation representing the line should be of the " \
                "type yx= (-1/m)x + c with c = X intercept on  axis"
    hintStr42 = "X intercept = 4"
    hintStr43 = "An equation in the Slope - Point form is represented as $ y-y1 = m(x-x1) $"
    hintStr44 = "An equation in the Slope - Intercept form is represented as $ y=mx + c $"
    hintStr45 = "An equation in the Two-Points form is represented as $ \\frac{y-y1}{y1-y2} = \\frac{x-x1}{x1-x2} $"
    hintStr46 = "An equation in the double Double Intercepts form is represented as $ \\frac{x}{a} +\\frac{y}{b} = 1 $"
    hintStr47 = "An equation in the Parametric form / Polar form is represented as " \
                "$ y = y1 + acos&Theta; ; x = x1 +asin&Theta; $"
    hintStr48 = "An equation in the Normal Form is represented as  $ x cos&Theta; +y sin&Theta; = d $"
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
        hint.append(hintStr12)
        hint.append(hintStr13)
        hint.append(hintStr14)
    elif Qtype == 8:
        hint.append(hintStr12)
        hint.append(hintStr15)
        hint.append(hintStr16)
    elif Qtype == 10 or Qtype == 11:
        hint.append(hintStr17)
        hint.append(hintStr18)
        hint.append(hintStr19)
    elif Qtype == 12 or Qtype == 13:
        hint.append(hintStr20)
        hint.append(hintStr21)
        hint.append(hintStr22)
    elif Qtype == 14:
        hint.append(hintStr23)
        hint.append(hintStr24)
        hint.append(hintStr25)
    elif Qtype == 15:
        hint.append(hintStr26)
        hint.append(hintStr27)
    elif Qtype == 16:
        hint.append(hintStr26)
        hint.append(hintStr28)
    elif Qtype == 17:
        hint.append(hintStr29)
        hint.append(hintStr30)
        hint.append(hintStr31)
    elif Qtype == 18:
        hint.append(hintStr29)
        hint.append(hintStr32)
        hint.append(hintStr33)
    elif Qtype == 19:
        hint.append(hintStr34)
        hint.append(hintStr35)
    elif Qtype == 20 or Qtype == 21 or Qtype == 22 or Qtype == 23:
        hint.append(hintStr36)
        hint.append(hintStr37)
        hint.append(hintStr38)
    elif Qtype == 24:
        hint.append(hintStr39)
        hint.append(hintStr40)
    elif Qtype == 25:
        hint.append(hintStr41)
        hint.append(hintStr42)
    elif Qtype == 27:
        hint.append(hintStr43)
    elif Qtype == 28:
        hint.append(hintStr44)
    elif Qtype == 29:
        hint.append(hintStr45)
    elif Qtype == 30:
        hint.append(hintStr46)
    elif Qtype == 31:
        hint.append(hintStr47)
    elif Qtype == 32:
        hint.append(hintStr48)
    elif Qtype == 40:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 41:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 42:
        hint.append(hintStr6)
        hint.append(hintStr9)
        hint.append(hintStr11)
    elif Qtype == 43:
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


def getFormattedEq1(eq=None, eqtype=None, points=None):
    """


    :rtype : object
    :param eq: 
    :return: 
    """
    temp = ""
    if not eqtype:
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
    else:
        x1 = points[0]
        y1 = points[1]
        x2 = points[2]
        y2 = points[3]
        m = (y2 - y1) / (x2 - x1)
        if m % 1 == 0:
            m = int(m)
        else:
            m = round(m, 2)
        if m == 0:
            m = random.randint(2, 9)
        if x1 % 1 == 0:
            x1 = int(x1)
        if y1 % 1 == 0:
            y1 = int(y1)
        if x2 % 1 == 0:
            x2 = int(x2)
        if y2 % 1 == 0:
            y2 = int(y2)
        if eqtype == "SP":
            temp += "y" + getSignedString(-y1) + " = " + str(m) + "(x" + getSignedString(-x1) + ")"
        elif eqtype == "SI":
            c = round(-((y2-y1)/(x2-x1)) * x1 + y1)
            if c % 1 == 0:
                c = int(c)
            temp += "y = " + GetCoeffString(m) + "x" + getSignedString(c)
        elif eqtype == "TP":
            d1 = GetCoeffString(y2 - y1)
            d2 = GetCoeffString(x2 - x1)
            if d1 == "":
                pass
            elif d1 == "-":
                d1 == "/(-1)"
            else:
                t1 = d1
                if "-" in t1:
                    d1 = "/(" + t1 + ")"
                else:
                    d1 = "/" + t1
            if d2 == "":
                pass
            elif d2 == "-":
                d2 == "/(-1)"
            else:
                t2 = d2
                if "-" in t2:
                    d2 = "/(" + t2 + ")"
                else:
                    d2 = "/" + t2
            temp += "(y" + getSignedString(-y1) + ")" + d1 + " = (x" + getSignedString(-x1) + \
                    ")" + d2
        elif eqtype == "DI":
            d1 = GetCoeffString(y1)
            d2 = GetCoeffString(x1)
            if d1 == "":
                pass
            elif d1 == "-":
                d1 == "/(-1)"
            else:
                t1 = d1
                if "-" in t1:
                    d1 = "/(" + t1 + ")"
                else:
                    d1 = "/" + t1
            if d2 == "":
                pass
            elif d2 == "-":
                d2 == "/(-1)"
            else:
                t2 = d2
                if "-" in t2:
                    d2 = "/(" + t2 + ")"
                else:
                    d2 = "/" + t2
            temp += "y" + d1 + "+ x" + d2 + " = 1"
        elif eqtype == "P" or eqtype == "Po":
            temp += "y = " + str(y1) + getSignedString(-eq[0]) + "cos&Theta; ;"
            temp += "x = " + str(x1) + getSignedString(eq[1]) + "cos&Theta;"
        elif eqtype == "N":
            t = random.randint(0, 7)
            t1 = angleSet[t][1]
            temp += "x cos" + str(t1) + "+y sin" + str(t1) + " = " + str(t)
        elif eqtype == "PX":
            t = random.randint(0, 7)
            t1 = angleSet[t][0]
            temp += "x = " + str(x1) + " cos" + str(t1)
        elif eqtype == "PY":
            t = random.randint(0, 7)
            t1 = angleSet[t][0]
            temp += "y = " + str(y1) + " cos" + str(t1)


    return temp


def getFormattedEq(eq=None, eqtype=None, points=None):
    """


    :rtype : object
    :param eq:
    :return:
    """
    temp = ""
    if not eqtype:
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
    else:
        x1 = points[0]
        y1 = points[1]
        x2 = points[2]
        y2 = points[3]
        m = (y2 - y1) / (x2 - x1)
        if m % 1 == 0:
            m = int(m)
        else:
            m = round(m, 2)
        if m == 0:
            m = random.randint(2, 9)
        if x1 % 1 == 0:
            x1 = int(x1)
        if y1 % 1 == 0:
            y1 = int(y1)
        if x2 % 1 == 0:
            x2 = int(x2)
        if y2 % 1 == 0:
            y2 = int(y2)
        if eqtype == "SP":
            temp += "y" + getSignedString(-y1) + " = " + str(m) + "(x" + getSignedString(-x1) + ")"
        elif eqtype == "SI":
            c = round(-((y2-y1)/(x2-x1)) * x1 + y1)
            if c % 1 == 0:
                c = int(c)
            temp += "y = " + GetCoeffString(m) + "x" + getSignedString(c)
        elif eqtype == "TP":
            d1 = GetCoeffString(y2 - y1)
            d2 = GetCoeffString(x2 - x1)
            n1 = "(y" + getSignedString(-y1) + ")"
            n2 = "(x" + getSignedString(-x1) + ")"
            if d1 == "":
                lhs = n1
            elif d1 == "-":
                lhs = "-" + n1
            else:
                lhs = "\\frac{" + n1 + "}{" + d1 + "}"
            if d2 == "":
                rhs = n2
            elif d2 == "-":
                rhs = "-" + n2
            else:
                rhs = "\\frac{" + n2 + "}{" + d2 + "}"
            temp += lhs + " = " + rhs

        elif eqtype == "DI":
            d1 = GetCoeffString(y1)
            d2 = GetCoeffString(x1)
            n1 = "y"
            n2 = "x"
            if d1 == "":
                f1 = n1
            elif d1 == "-":
                f1 = "-" + n1
            else:
                if "-" in d1:
                    f1 = "- \\frac{" + n1 + "}{" + MultiplyMinus(d1) + "}"
                else:
                    f1 = "\\frac{" + n1 + "}{" + d1 + "}"
            if d2 == "":
                f2 = "+ " + n2
            elif d2 == "-":
                f2 = "- " + n2
            else:
                if "-" in d2:
                    f2 = "- \\frac{" + n2 + "}{" + MultiplyMinus(d2) + "}"
                else:
                    f2 = "+ \\frac{" + n2 + "}{" + d2 + "}"
            temp += f1 + f2 + " = 1"

        elif eqtype == "P" or eqtype == "Po":
            temp += "y = " + str(y1) + getSignedString(-eq[0]) + "cos&Theta; ;"
            temp += "x = " + str(x1) + getSignedString(eq[1]) + "cos&Theta;"

        elif eqtype == "N":
            t = random.randint(0, 7)
            t1 = angleSet[t][1]
            temp += "x cos" + str(t1) + " + y sin" + str(t1) + " = " + str(t)
        elif eqtype == "PX":
            t = random.randint(0, 7)
            t1 = angleSet[t][0]
            temp += "x = " + str(x1) + " cos" + str(t1)
        elif eqtype == "PY":
            t = random.randint(0, 7)
            t1 = angleSet[t][0]
            temp += "y = " + str(y1) + " cos" + str(t1)

    temp = "$" + temp + "$"

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
        display = getFormattedEq1(equation)
    else:
        display = getFormattedEq1(equation)
    return display


def getFormattedSlope(deg=None, where=None):
    fm = ""
    if deg:
        if deg in set1:
            fm = "0"
        elif deg in set2:
            fm = "\\frac{1}{&radic;3}"
        elif deg in set3:
            if where == "eq":
                fm = ""
            else:
                fm = "1"
        elif deg in set4:
            fm = "&radic;3"
        elif deg in set5:
            fm = "&infin;"
        elif deg in set6:
            fm = "-&radic;3"
        elif deg in set7:
            if where == "eq":
                fm = "-"
            else:
                fm = "-1"
        elif deg in set8:
            fm = "\\frac{-1}{&radic;3}"
    return fm


if __name__ == "__main__":
    assess1 = [1, 2, 3]
    assess2 = [4, 5, 6]
    assess3 = [7, 8, 9]
    assess4 = [10, 11, 12, 13, 14]
    assess5 = [15, 16, 17, 18, 19]
    assess6 = [20, 21, 22, 23, 24, 25, 26]
    assess7 = [27, 28, 29, 30, 31, 32]
    assess8 = [33, 34, 35, 36, 37, 38, 39]
    assess9 = [40, 41, 42, 43]
    assessImages = [1, 2, 4, 5, 7, 8, 10, 12, 15, 16, 17, 18, 19]
    assessNoImages = [3, 6, 9, 11, 13, 14] + range(20, 44)
    all = range(0, 44)
    assess = [all, assess1, assess2, assess3, assess4, assess5, assess6, assess7, assess8, assess9, assessImages, assessNoImages]
    choice = -1
    count = 0
    while choice not in range(0, 12):
        if count != 0:
            print "\nSorry! You have entered a incorrect assessment number. Please try again and " \
                  "enter a valid number\n\n"
        choice = input("Enter the Assessment number to generate the assessment(0-11):\n "
                       "0 for All question in a single assessment\n"
                       "1-9 for a specific assessment\n"
                       "10 for all questions with images in a single assessment\n"
                       "11 for all question without images in a single assessment:  ")
        count += 1
    if choice in range(0, 10):
        choice1 = 0
        count = 0
        while choice1 not in range(1, 4):
            if count != 0:
                print "\nSorry! Incorrect input. Please try again...\n\n"
            choice1 = input("\nPress 1 if you want questions with images only\n"
                            "Press 2 if you want questions without images only\n"
                            "press 3 to skip: ")
            count += 1
    else:
        choice1 = 3
    name = raw_input("Enter a name for the CSV: ")
    coordinateGeo(assess[choice], choice1, name)