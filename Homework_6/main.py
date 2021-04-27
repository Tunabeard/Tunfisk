from functions_file import digits_to_truefalse
import os
import time
import datetime
import colored
from colored import stylize

construction_symbol = "\u25AE"
are_delimeters_active_now = False

while True:
    clear = lambda: os.system("cls")
    clear()
    clock = [[], [], [], [], [], [], []]
    for line in clock:
        while len(line) < 20:
            line.append(False)
    current_time = datetime.datetime.now().strftime("%H%M%S")
    N = 0
    for digit in current_time:
        clock = digits_to_truefalse(current_time, digit, N, clock)
        N += 5
    for line in clock:
        line[25:25] = [False]
        line[20:20] = [False, False, False]
        line[15:15] = [False]
        line[10:10] = [False, False, False]
        line[5:5] = [False]
    clock[1][12] = are_delimeters_active_now
    clock[1][26] = are_delimeters_active_now
    clock[5][12] = are_delimeters_active_now
    clock[5][26] = are_delimeters_active_now
    for line in clock:
        N = 0
        for item in line:
            if item == True:
                if N != 12 and N != 26:
                    print(stylize(construction_symbol, colored.fg(45),), end="")
                else:
                    print(stylize(construction_symbol, colored.fg(226),), end="")
            else:
                print(stylize(construction_symbol, colored.fg(234),), end="")
            N += 1
        print()
    are_delimeters_active_now = not are_delimeters_active_now
    time.sleep(1)