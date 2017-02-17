import numpy as np

credit = 1000  # всего средств
total_won = 1000
cash = 20  # стоимость одной игры
flag = False
emoji = ['7️⃣', '🍒', '🍏', '🔔'] # семерка, вишня, яблоко, колокол


def play_game():
    global credit
    global cash
    global flag
    global total_won
    flag = False  # есть ли выигрыш в игре
    credit -= cash  # плата за игру
    total_won = credit
    output = ""
    lines = np.random.randint(0, 4, (3, 3))
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            output += emoji[lines[i][j]] + " "
        output += '\n'
    print(lines)
    if lines[0][0] == lines[0][1] == lines[0][2]:
        if lines[0][0] == 0:
            credit += cash * 5
        elif lines[0][0] == 1:
            credit += cash * 3
        elif lines[0][0] == 2:
            credit += cash * 1.5
        elif lines[0][0] == 3:
            credit += cash * 1
        flag = True
    if lines[1][0] == lines[1][1] == lines[1][2]:
        if lines[1][0] == 0:
            credit += cash * 5
        elif lines[1][0] == 1:
            credit += cash * 3
        elif lines[1][0] == 2:
            credit += cash * 1.5
        elif lines[1][0] == 3:
            credit += cash * 1
        flag = True
    if lines[2][0] == lines[2][1] == lines[2][2]:
        if lines[2][0] == 0:
            credit += cash * 5
        elif lines[2][0] == 1:
            credit += cash * 3
        elif lines[2][0] == 2:
            credit += cash * 1.5
        elif lines[2][0] == 3:
            credit += cash * 1
        flag = True
    if lines[0][0] == lines[1][0] == lines[2][0]:
        if lines[0][0] == 0:
            credit += cash * 5
        elif lines[0][0] == 1:
            credit += cash * 3
        elif lines[0][0] == 2:
            credit += cash * 1.5
        elif lines[0][0] == 3:
            credit += cash * 1
        flag = True
    if lines[0][1] == lines[1][1] == lines[2][1]:
        if lines[0][1] == 0:
            credit += cash * 5
        elif lines[0][1] == 1:
            credit += cash * 3
        elif lines[0][1] == 2:
            credit += cash * 1.5
        elif lines[0][1] == 3:
            credit += cash * 1
        flag = True
    if lines[0][2] == lines[1][2] == lines[2][2]:
        if lines[0][2] == 0:
            credit += cash * 5
        elif lines[0][2] == 1:
            credit += cash * 3
        elif lines[0][2] == 2:
            credit += cash * 1.5
        elif lines[0][2] == 3:
            credit += cash * 1
        flag = True
    if lines[0][0] == lines[1][1] == lines[2][2]:
        if lines[0][0] == 0:
            credit += cash * 5
        elif lines[0][0] == 1:
            credit += cash * 3
        elif lines[0][0] == 2:
            credit += cash * 1.5
        elif lines[0][0] == 3:
            credit += cash * 1
        flag = True
    if lines[0][2] == lines[1][1] == lines[2][0]:
        if lines[0][2] == 0:
            credit += cash * 5
        elif lines[0][2] == 1:
            credit += cash * 3
        elif lines[0][2] == 2:
            credit += cash * 1.5
        elif lines[0][2] == 3:
            credit += cash * 1
        flag = True
    total_won = credit - total_won
    return output

