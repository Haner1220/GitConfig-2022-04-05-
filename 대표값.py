from collections import Counter

e=[]
for i in range(10):
    e.append(int(input()))
cnt = Counter(e)

print(sum(e)//10,cnt.most_common()[0][0],sep='\n')