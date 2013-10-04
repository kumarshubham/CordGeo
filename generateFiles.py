__author__ = 'kumar'

import csv
from pylab import *


def generateCSV(ques):
    data = []
    count = 0
    for q in ques:
        Question = q['Q']
        hint1 = q['hints'][0]
        hint2 = q['hints'][1]
        hint3 = q['hints'][2]
        options = []
        feedback = []
        index = 0
        correct = 4
        topic = 7
        difficulty = 1
        for d in q['details']:
            index += 1
            options.append(d['option'])
            feedback.append(d['feedback'])
            if d['correct']:
                correct = index

        option1 = options[0]
        option2 = options[1]
        option3 = options[2]
        option4 = options[3]
        feedback1 = feedback[0]
        feedback2 = feedback[1]
        feedback3 = feedback[2]
        feedback4 = feedback[3]
        data.append(
            [Question, 4, option1, option2, option3, option4, correct, hint1, hint2, hint3, topic, difficulty,
                feedback[0], feedback[1], feedback[2], feedback[3]])
        count += 1

    with open('test.csv', 'wb') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(data)
    print "Done", len(data)


def generateSVG(eq, display, name, Qtype=0, points=None):
    if Qtype == 16:
        p1 = points[1]
        p2 = points[0]
        a = eq[1][0]
        b = eq[1][1]
        c = eq[1][2]
    else:
        if points:
            p1 = points[0]
            if len(points) > 1:
                p2 = points[1]
        a = eq[0][0]
        b = eq[0][1]
        c = eq[0][2]
    list1 = [10, 11, 12, 13, 15, 16]
    list2 = [10, 11, 12, 13, 14]
    list3 = [4, 6, 10, 11, 12, 13, 14, 15, 16]
    list4 = [10, 11, 12, 13]
    figure(figsize=(8, 6), dpi=40)
    m = 0
    if b != 0:
        X = np.linspace(-12, 12, 256, endpoint=True)
        m = -a * 1.0 / b
        c = -c * 1.0 / b
        Y = m * X + c
        # print "Y: ", m, c
    else:
        Y = np.linspace(-12, 12, 256, endpoint=True)
        X = -(c * 1.0 / a) * (Y / Y)
        m = 'NA'
        # print "X: ", m, c

    if type(m) is int and m > 0:
        loc = "upper left"
    else:
        if m == 0 and c > 0:
            loc = "lower left"
        elif m == "NA":
            if c > 0:
                loc = "lower right"
            else:
                loc = "lower left"
        else:
            loc = "upper right"
    # print Qtype
    # print eq[0]
    # print p1
    if Qtype == 15 or Qtype == 16:
        plot(X, Y, color="blue", linewidth=2.5, linestyle="-")
    else:
        plot(X, Y, color="blue", linewidth=2.5, linestyle="-", label=display[0])

    if Qtype in list1:
        if Qtype == 16:
            a = eq[0][0]
            b = eq[0][1]
            c = eq[0][2]
        else:
            a = eq[1][0]
            b = eq[1][1]
            c = eq[1][2]
        m = 0
        if b != 0:
            m = -a * 1.0 / b
            c = -c * 1.0 / b
            Y1 = m * X + c
            plot(X, Y1, color="red", linewidth=2.5, linestyle="-", label=display[1])
        else:
            X1 = -(c * 1.0 / a) * (Y / Y)
            m = 'NA'
            plot(X1, Y, color="red", linewidth=2.5, linestyle="-", label=display[1])

    xlim(X.min() * 1.1, X.max() * 1.1)
    ylim(-13, 13)
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    ax.set_xticks(np.arange(-12, 12, 2))
    ax.set_yticks(np.arange(-12, 12, 2))
    plt.grid()

    if Qtype not in list2:
        legend(loc=loc)

    ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
    ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

    if Qtype in list3:
        pointA = (round(p1[0], 2), round(p1[1], 2))
        pointB = (round(p1[2], 2), round(p1[3], 2))
        scatter([p1[0],],[p1[1],], 50, color ='blue')
        scatter([p1[2],],[p1[3],], 50, color ='blue')
        annotate(r'$' + str(pointA) + '$', xy=(p1[0], p1[1]), xycoords='data',
                 xytext=(+30, +50), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", facecolor='red'))
        annotate(r'$' + str(pointB) + '$', xy=(p1[2], p1[3]), xycoords='data',
                 xytext=(+80, +110), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", facecolor='red'))

    if Qtype in list4:
        # print eq[1]
        # print p2
        point1A = (round(p2[0], 2), round(p2[1], 2))
        point1B = (round(p2[2], 2), round(p2[3], 2))
        scatter([p2[0],],[p2[1],], 50, color='red')
        scatter([p2[2],],[p2[3],], 50, color='red')
        annotate(r'$' + str(point1A) + '$', xy=(p2[0], p2[1]), xycoords='data',
                 xytext=(+50, +70), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", facecolor='red'))
        annotate(r'$' + str(point1B) + '$', xy=(p2[2], p2[3]), xycoords='data',
                 xytext=(+70, +90), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", facecolor='red'))

    if Qtype == 14:
        point1A = (round(p2[0], 2), round(p2[1], 2))
        scatter([p2[0],],[p2[1],], 50, color='blue')
        annotate(r'$' + str(point1A) + '$', xy=(p2[0], p2[1]), xycoords='data',
                 xytext=(+50, +70), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", facecolor='red'))

    savefig(name + ".png", dpi=48, bbox_inches='tight')

# generateSVG([5,3,10], ["5x-3y+10 = 0"])