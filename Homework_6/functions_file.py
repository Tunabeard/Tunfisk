def digits_to_truefalse(current_time, digit, N, clock):
    if digit == "0":
        clock[0][N:N+5] = False, True, True, True, False
        clock[1][N:N+5] = True, False, False, False, True
        clock[2][N:N+5] = True, False, False, False, True
        clock[3][N:N+5] = True, False, False, False, True
        clock[4][N:N+5] = True, False, False, False, True
        clock[5][N:N+5] = True, False, False, False, True
        clock[6][N:N+5] = False, True, True, True, False
    if digit == "1":
        clock[0][N:N+5] = False, False, True, False, False
        clock[1][N:N+5] = False, True, True, False, False
        clock[2][N:N+5] = False, False, True, False, False
        clock[3][N:N+5] = False, False, True, False, False
        clock[4][N:N+5] = False, False, True, False, False
        clock[5][N:N+5] = False, False, True, False, False
        clock[6][N:N+5] = False, False, True, False, False
    if digit == "2":
        clock[0][N:N+5] = False, True, True, True, False
        clock[1][N:N+5] = True, False, False, False, True
        clock[2][N:N+5] = False, False, False, False, True
        clock[3][N:N+5] = False, False, False, True, False
        clock[4][N:N+5] = False, False, True, False, False
        clock[5][N:N+5] = False, True, False, False, False
        clock[6][N:N+5] = True, True, True, True, True
    if digit == "3":
        clock[0][N:N+5] = False, True, True, True, False
        clock[1][N:N+5] = False, False, False, False, True
        clock[2][N:N+5] = False, False, False, False, True
        clock[3][N:N+5] = False, True, True, True, False
        clock[4][N:N+5] = False, False, False, False, True
        clock[5][N:N+5] = False, False, False, False, True
        clock[6][N:N+5] = False, True, True, True, False
    if digit == "4":
        clock[0][N:N+5] = False, False, False, True, False
        clock[1][N:N+5] = False, False, True, True, False
        clock[2][N:N+5] = False, True, False, True, False
        clock[3][N:N+5] = True, False, False, True, False
        clock[4][N:N+5] = True, True, True, True, True
        clock[5][N:N+5] = False, False, False, True, False
        clock[6][N:N+5] = False, False, False, True, False
    if digit == "5":
        clock[0][N:N+5] = True, True, True, True, True
        clock[1][N:N+5] = True, False, False, False, False
        clock[2][N:N+5] = True, True, True, True, False
        clock[3][N:N+5] = False, False, False, False, True
        clock[4][N:N+5] = False, False, False, False, True
        clock[5][N:N+5] = True, False, False, False, True
        clock[6][N:N+5] = False, True, True, True, False
    if digit == "6":
        clock[0][N:N+5] = False, True, True, True, False
        clock[1][N:N+5] = True, False, False, False, False
        clock[2][N:N+5] = True, False, False, False, False
        clock[3][N:N+5] = False, True, True, True, False
        clock[4][N:N+5] = True, False, False, False, True
        clock[5][N:N+5] = True, False, False, False, True
        clock[6][N:N+5] = False, True, True, True, False
    if digit == "7":
        clock[0][N:N+5] = True, True, True, True, True
        clock[1][N:N+5] = False, False, False, False, True
        clock[2][N:N+5] = False, False, False, True, False
        clock[3][N:N+5] = False, False, True, False, False
        clock[4][N:N+5] = False, True, False, False, False
        clock[5][N:N+5] = False, True, False, False, False
        clock[6][N:N+5] = False, True, False, False, False
    if digit == "8":
        clock[0][N:N+5] = False, True, True, True, False
        clock[1][N:N+5] = True, False, False, False, True
        clock[2][N:N+5] = True, False, False, False, True
        clock[3][N:N+5] = False, True, True, True, False
        clock[4][N:N+5] = True, False, False, False, True
        clock[5][N:N+5] = True, False, False, False, True
        clock[6][N:N+5] = False, True, True, True, False
    if digit == "9":
        clock[0][N:N+5] = False, True, True, True, False
        clock[1][N:N+5] = True, False, False, False, True
        clock[2][N:N+5] = True, False, False, False, True
        clock[3][N:N+5] = False, True, True, True, True
        clock[4][N:N+5] = False, False, False, False, True
        clock[5][N:N+5] = False, False, False, False, True
        clock[6][N:N+5] = False, True, True, True, False
    return clock