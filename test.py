given_list = []

for i in range(int(input())):
    given_list.append(input())
#take all given files


from collections import Counter

count = Counter(given_list)
print(len(count))


replay_list = [] 

if len(count) == 1:
    for i in range(count[i]):
        c = i.split(".")[0]+f"({count[i]})"+"."+i.split(".")[1]
        replay_list.append(c)
else:
     for i in count:
        for g in range(0,count[i]):
            if count[i] > 1:
                if len(i.split(".")) > 1:
                        c = i.split(".")[0]+f"({count[i]-1+g})"+"."+i.split(".")[1]
                        replay_list.append(c)
                else:
                    c = i+f"({count[i]-1})"
                replay_list.append(c)
            elif len(count) == 1: 
                    for i in range(count[i]):
                            c = i.split(".")[0]+f"({count[i]})"+"."+i.split(".")[1]
                            replay_list.append(c)
f = set(given_list+replay_list) # remove duplicates using type Set
f = list(f).sort() # sort the List that was Set
print("-"*100)
for i in f:
    print(i)