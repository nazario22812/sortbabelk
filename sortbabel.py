
n = input().split()
list = [int(i) for i in n]

def posortuj_dane(lst):
    b =len(lst)
    while b > 1:
        i = 0
        while i<b-1:
            if lst[i] > lst[i+1]:
                pomoc = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = pomoc
            i+=1
        b-=1
    return lst


print(posortuj_dane(list))