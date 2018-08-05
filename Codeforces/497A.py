s = input()
vowel ='aeiou'
flag = 0

if (s[-1] not in vowel) and s[-1] != 'n':
    flag = 1
##    print('a')
    
if s[0] in vowel:
    last = 'v'
elif s[0] == 'n':
    last = 'n'
else:
    last = 'c'

for i in range(1,len(s)):
    if s[i] in vowel:
        last = 'v'
    elif (s[i] not in vowel and s[i] != 'n') and (last == 'v' or last == 'n'):
        last = 'c'
    elif s[i] == 'n' and last == 'n' or last == 'v':
        last = 'n'
    elif s[i] =='n' and last == 'c':
        flag = 1
        break  
    else:
##        print(s[i], i)
        flag = 1
        break
if flag:
    print('NO')
else:
    print('YES')
