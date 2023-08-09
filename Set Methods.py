people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}


## 1. union():-
d=people.union(names)
print(d)

## 2. add():-
set={"Jay", "Idrish", "Archi"}
set.add("Om")
print("After adding in the set",set)

## 3. clear():-
set={"Jay", "Idrish", "Archi"}
set.clear()
print("After clearing set",set)


## 4. copy():-
set={"Jay", "Idrish", "Archi"}
set1=set.copy()
print("After copying list",set1)


## 5. difference():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

a=people.difference(names)
print("After applying difference method a",a)





people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

a1=names.difference(people)
print("After applying difference method a1",a1)




## 6. difference_update():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.difference_update(names)
print("After applying difference_update method people",people)



people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

names.difference_update(people)
print("After applying difference_update method names",names)



## 7. discard():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.discard("Jay")
print("After applying discard method people",people)


## 8. intersection():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

d=people.intersection(names)
print("After applying intersection method d",d)

print()

people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

d1=names.intersection(people)
print("After applying intersection method d1",d1)


## 9. intersection_update():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.intersection_update(names)
print("After applying intersection_update method people",people)

print("intersection_update")
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

d1=names.intersection_update(people)
print("After applying intersection_update method names",names)




## 10. issubset():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.issubset(names)
print("After applying issubset",people)

names.isdisjoint(people)
print("After applying issubset",names)




## 11. issuperset():-

people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.issuperset(names)
print("After applying issuperset",people)

names.issuperset(people)
print("After applying issuperset",names)



## 12. pop():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.pop()
print("After applying pop",people)



## 13. remove():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.remove("Jay")
print("After applying pop",people)




## 14. symmetric_difference():-

people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.symmetric_difference(names)
print("After applying symmetric_difference",people)

names.symmetric_difference(people)
print("After applying symmetric_difference",names)




## 15. symmetric_difference_update():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.symmetric_difference_update(names)
print("After applying symmetric_difference_update",people)

names.symmetric_difference_update(people)
print("After applying symmetric_difference_update",names)




## 16. union():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.union(names)
print("After applying union",people)

names.union(people)
print("After applying union",names)




## 17. isdisjoint():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.isdisjoint(names)
print("After applying isdidjoint",people)

names.isdisjoint(people)
print("After applying isdidjoint",names)




## 18. update():-
people = {"Jay", "Idrish", "Archil","Om"}
names = {"Karan", "Arjun","Om","Archil","Rudra"}
best_names = {"Deepanshu", "Raju","Arjun","Rudra","Om"}

people.update(names)
print("After applying update",people)

names.update(people)
print("After applying update",names)


