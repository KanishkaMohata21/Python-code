def printBoard(x, o):
    state0 = "X" if x[0] else ("O" if o[0] else 0)
    state1 = "X" if x[1] else ("O" if o[1] else 1)
    state2 = "X" if x[2] else ("O" if o[2] else 2)
    state3 = "X" if x[3] else ("O" if o[3] else 3)
    state4 = "X" if x[4] else ("O" if o[4] else 4)
    state5 = "X" if x[5] else ("O" if o[5] else 5)
    state6 = "X" if x[6] else ("O" if o[6] else 6)
    state7 = "X" if x[7] else ("O" if o[7] else 7)
    state8 = "X" if x[8] else ("O" if o[8] else 8)

    print(f"{state0}|{state1}|{state2}")
    print("-|-|-")
    print(f"{state3}|{state4}|{state5}")
    print("-|-|-")
    print(f"{state6}|{state7}|{state8}")

def check_winner(x, o):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]

    for combo in winning_combinations:
        if all(x[i] == 1 for i in combo):
            return "X WON"
        elif all(o[i] == 1 for i in combo):
            return "O WON"

    return None  # No winner yet

print("WELCOME TO TIC-TAC-TOE")
x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
o = [0, 0, 0, 0, 0, 0, 0, 0, 0]
t = 0
c = 9

while c != 0:
    if t == 0:
        printBoard(x, o)
        print("X Play")
        val = int(input("Enter the position you want to place X in: "))
        x[val] = 1
        winner = check_winner(x, o)
        if winner:
            print(winner)
            break
        c -= 1
        t = 1
    else:
        printBoard(x, o)
        print("O Play")
        val = int(input("Enter the position you want to place O in: "))
        o[val] = 1
        winner = check_winner(x, o)
        if winner:
            print(winner)
            break
        c -= 1
        t = 0

if c == 0:
    print("IT'S A TIE")

