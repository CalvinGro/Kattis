import math

def compare(s,l):
    z=[]
    temp_l = list(l)
    s.sort()
    temp_l.sort()
    for i in s:
        if i in temp_l:
            z.append(i)
            temp_l.remove(i)
    return z

def remove_z(s,z):
    s_temp = list(s)
    for i in z:
        s_temp.remove(i)
    return s_temp

def find_e_max(x,y):
    if len(x) == len(y):
        return (len(x)*2,x,y)
    elif len(x) > len(y):
        return (len(y)*2,y,x)
    else:
        return (len(x)*2,x,y)


def find_e(z,s,l,e_max):
    w = remove_z(s,z)
    min_s = math.ceil(len(s)/2)
    len_w = min_s - len(z)
    e = list(z)
    for i in range(len_w):
        e.append(w[i])
    c = remove_z(l,z)
    for i in range(e_max-min_s):
        e.append(c[i])
    return e


def recursive_cousin_count(e_max,s,l,count):
    z = compare(s,l)
    if len(z)*2 >= len(l):
        return count
    e = find_e(z,s,l,e_max)
    e_max,s,l = find_e_max(e,l)
    count += 1
    return recursive_cousin_count(e_max,s,l,count)

def str_to_list(s):
    chars = []
    for i in s:
        chars.append(i)
    return chars


while 1 > 0:
    a=input()
    b=input()
    a = str_to_list(a)
    b = str_to_list(b)
    e_max,s,l = find_e_max(a,b)
    print(recursive_cousin_count(e_max,s,l,1))
    if a==0:
        break
