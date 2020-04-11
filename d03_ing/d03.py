# solved in python

def par(left, right, code):
    if code == None:
        code = 1
        par(left - 1, right, code)
    else:
        if left != 0:
            if left < right:
                code *= 10
                par(left - 1, right, code + 1)
                par(left, right - 1, code)
            elif left == right:
                code *= 10
                par(left - 1, right, code + 1)
        elif right != 0:
            code *= 10
            par(left, right - 1, code)
        else:
            decode(code)

def decode(code):
    while (code != 0):
        if (code % 10) == 1:
            print(')', end = ' ')
        elif (code % 10) == 0:
            print('(', end = ' ')
        code = code // 10
    print('')

count = int(input("Input: "))
par(count, count, None)
