def cap(str):
    return' '.join(map(lambda s:s[:-1]+s[-1].upper(),s.title().split()))
s="i am very good girl"
print("string before:",s)
print("string after:",cap(str))
