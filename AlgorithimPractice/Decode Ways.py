def Decode(N):
    inputWord = "1212"
    map dict dp(N)
    if N== len(inputWord):
        return 1
    else if N > len(inputWord):
        return 0

    oneDigit = input(inputWord[N])
    twoDigit = input(inputWord[N:N+2]) if N+1 < len(inputWord) else 0

    if oneDigit != 0:
        if 10 <= twoDigit <= 26:
            return Decode(N+1) + Decode(N+2)
        else:
            return Decode(N+1)