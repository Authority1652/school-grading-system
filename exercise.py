# names=["mariam", "ben", "saul"]
# # print(dir(names))
# new_names =["mosh", "son"]
# names.append("mariam")
# names.append(True)
# names.extend(new_names)            #extending the list for multiple data
# # print(names)
# names.clear()
# print(names)
# del(names)
# print(names)
# another_names =names.copy()             #copy means keeping a copy or backup
# print(another_names)

# names=["mariam", "ben", "saul"]
# name ="ben"
# names.count(name)
# print(names.count(name))                   #counting the names on the list

# names=["mariam", "ben", "saul"]
# poped=names.pop()
# poped=names.pop(2)
# print(poped)
# print(names)                            #removing a particular name fron a list

# names.remove("ben")
# print(names)


               #NESTING

              #toyota                       bmw              audi  subaru
# cars =[["camry", "corolla", "praddo",], ["m5", "m6" "m7"], "audi", "subaru"]
# # (cars[0][1])
# # print(cars[0][1])
# # cars.append("camry")
# # print(cars[0][1])
# cars[1][1]="m6"
# print(cars)


                                  #DICTIONARY   {}

cars ={
    "bmw": "m5",
    "audi": "audi",
    "number": 4,
    "status": True
}
# print(cars["bmw"])


# print(dir(cars))

our_keys =list(cars.keys())
print(our_keys)
print(len(cars))

our_values=list(cars.values())
print(our_values)