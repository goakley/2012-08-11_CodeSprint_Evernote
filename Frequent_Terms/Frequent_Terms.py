dictionary = dict()
dictionary[None] = -1
N = long(raw_input())
for i in range(N) :
    value = raw_input()
    try :
        dictionary[value] += 1
    except KeyError :
        dictionary[value] = 1

d_order = dict()
while len(dictionary) > 0 :
    best_key = None
    for key in dictionary.iterkeys():
        if dictionary[best_key] < dictionary[key] :
            best_key = key
    try :
        d_order[dictionary[best_key]]
    except KeyError :
        d_order[dictionary[best_key]] = []
    d_order[dictionary[best_key]].append(best_key)
    d_order[dictionary[best_key]] = sorted(d_order[dictionary[best_key]])
    del dictionary[best_key]

k = long(raw_input())
kc = 0

d_order_keys = sorted(d_order, reverse=True)
for x in d_order_keys :
    for y in d_order[x] :
        print y
        kc += 1
        if kc == k :
            break
    if kc == k :
        break
