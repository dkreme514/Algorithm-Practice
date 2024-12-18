def countingValleys(n,s):
    if n <=0:
        return 0
    state = 0
    level = 0
    numValleys = 0
    for c in s:
        assert (c=='U' or c=='D'), "Invalid letter"
        if state == 0:
            if c == 'U':
                level += 1
                state = 1
            else:
                level -= 1
                state = 2
        elif state == 1:
            if c == 'U':
                level += 1
            else:
                level -= 1
                if level == 0:
                    state = 0
        else:
            if c == 'D':
                level-= 1
            else:
                level += 1
                if level == 0:
                    numValleys += 1
                    state = 0
    return numValleys

n = 8
s = "DDUUUUDD"
result = countingValleys(n,s)
print(f'result = {result}')