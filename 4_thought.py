found = False
operators = ["*", "//", "+", "-"]
m = int(input())


    


def find_value(first, second, third, n):
    total = eval(f"4{first}4{second}4{third}4")
    if total == n:
        return True
    return False


for _ in range(m):
    n = input()
    try:
        n = int(n)
    except:
        n = float(n)

    for first in operators:
        for second in operators:
            for third in operators:
                found = find_value(first, second, third, n)

                if found:
                    operation = [first, second, third]
                    break
            if found:
                break
        if found:
            break
    
    if found:
        for i in range(len(operation)):
            if operation[i] == '//':
                operation[i] = '/'
        
        print(f"4 {operation[0]} 4 {operation[1]} 4 {operation[2]} 4 = {n}")
    else:
        print("no solution")
            