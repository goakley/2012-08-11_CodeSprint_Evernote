N = long(raw_input())
elements = [long(raw_input()) for i in range(N)]
for n in range(N) :
    value = 1
    for i in range(N) :
        if i != n :
            value *= elements[i]
    print value
