# # 1. copy():-

# people: list[str]=['Bob',['Alyza','Elon'],'Mario','Trump']
# copy_people: list[str]=people.copy()


# print(people)
# print(copy_people)

# copy_people.remove('Trump')
# people[1][1]== 'Evan'
# print(people)
# print(copy_people)


# # 2. extend():-

# people: list[str]=['Bob',['Alyza','Elon'],'Mario','Trump']
# people2: list[str]=['Evan','Marie']

# people.extend([people2])
# print(people)













## 1. append():-

my_list=["Geeks","for"]
my_list.append("Geeks")
print(my_list)


## 2. extend():-
lst1=["Geeks","for","Geeks"]
lst2=[1,2,3,4,5]
lst2.extend(lst1)
print(lst2)


## 3. del() :-
lis = [2, 1, 3, 5, 4, 3, 8]
del lis[2:4]
print("After deleting list",lis)


## 4. pop():-
lis.pop(2)
print("After popping list",lis)



## 5. insert():-
lis = [2, 1, 3, 5, 3, 8]
lis.insert(3,6)
print("After inserting list",lis)



## 6. remove():-
lis = [2, 1, 3, 5, 3, 8]
lis.remove(3)
print("After removing list",lis)



## 7. sort():-
lis = [2, 1, 3, 5, 3, 8]
lis.sort()
print("After sorting list",lis)



## 8. reverse():-
lis = [2, 1, 3, 5, 3, 8]
lis.reverse()
print("After reversing list",lis)



## 9. clear():-
lis = [2, 1, 3, 5, 3, 8]
lis.clear()
print("After clear list",lis)



## 10. copy():-
lis = [2, 1, 3, 5, 3, 8]
lis1=lis.copy()
print("After copying list",lis)


## 11. count():-
str=("Geeks","for","Geeks","for","Geeks")
print("After Counting the list :",str.count("Geeks"))
