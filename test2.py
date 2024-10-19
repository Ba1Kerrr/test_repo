from collections import Counter
common_list = []
for a in range(int(input())):
    common_list.append(input())
for i in range(len(common_list)): # проходимся по данному нам списку
    for j in range(common_list.count(common_list[i])): # проходимся по повтор. значениям в списке

        if "." in common_list[i]: # если попался файл с расширениием
            print(common_list[i].split(".")[0]+f"({common_list.count(common_list[j])})"+"."+common_list[i].split(".")[1]) # +значение повтора


        else: # если попался файл без расширениия
            print(common_list[i]+f"({common_list.count(common_list[j])})") # +значение повтора 
