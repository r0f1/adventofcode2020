lines = open("input.txt").read().translate(''.maketrans('FBLR','0101')).splitlines()
s = set(int(line,2) for line in lines)
print(max(s),[x for x in range(max(s)) if x not in s and {x-1,x+1}.issubset(s)][0])
