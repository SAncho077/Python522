

lst = [-2,3,8,-11,-4,6]

def skolko(lst):
    if len(lst) == 0:
        return 0
    else:
        coint = 0
        if lst[0] <= -1:
            coint += 1

        return coint + skolko(lst[1:])


print(skolko(lst))

