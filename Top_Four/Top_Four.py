N = long(raw_input())
vals = [ int(raw_input()) for i in range(4) ]
for n in range(N-4) :
    value = int(raw_input())
    if value > min(vals) :
        vals[vals.index(min(vals))] = value
vals = sorted(vals, reverse=True)
for v in vals :
    print(v)
