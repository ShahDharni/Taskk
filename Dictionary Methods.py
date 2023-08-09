stud_details={"name":"Om","marks":90,"roll_no":45,"city":"Ahmedabad"}


## 1 clear():-
stud_details.clear()
print(stud_details)

## 3 from_keys():-
stud_details={"name":"Om","marks":90,"roll_no":45,"city":"Ahmedabad"}
a=dict.fromkeys(stud_details)
print(a)

## 4 get():-
stud_details={"name":"Om","marks":90,"roll_no":45,"city":"Ahmedabad"}
a=stud_details.get("name")
print(a)

## 5 items():-
stud_details={"name":"Om","marks":90,"roll_no":45,"city":"Ahmedabad"}
a=dict.items(stud_details)
print(a)


## 6 keys():-
stud_details={"name":"Om","marks":90,"roll_no":45,"city":"Ahmedabad"}
a=dict.keys(stud_details)
print(a)

## 7 pop():-
stud_details={"name":"Om","marks":90,"roll_no":45,"city":"Ahmedabad"}
a=stud_details.pop("marks")
print(stud_details)

## 8 popitem():-
stud_details={"name":"Om","marks":90,"roll_no":45,"city":"Ahmedabad"}
a=stud_details.popitem()
print(stud_details)

## 9 setdefault():-
stud_details={"name":"Om","marks":90,"roll_no":45,"city":"Ahmedabad"}
stud_details.setdefault("marks",90)
print(stud_details)

## 10 update():-

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)


## 11 values():-
stud_details={"name":"Om","marks":90,"roll_no":45,"city":"Ahmedabad"}
a=dict.values(stud_details)
print(a)
