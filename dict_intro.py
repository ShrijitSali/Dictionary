vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
 #   'roadster': 'Trimph Street Triple',  # this key is already used, this value will not be used first come basis
}

# my_car=vehicles['fiesta']
# print(my_car)
#
# commuter=vehicles['virago']
# print(commuter)
#
# learner=vehicles.get("er5")
# print(learner)

vehicles["starfighter"] = "lockheer f-104"  # add data to dict
vehicles["learjet"] = "Bomber"
vehicles["toy"] = "glider"

# Upgrade Varago:
vehicles['virago'] = "Yamaha XV535"  # update values

# delete
del vehicles["starfighter"]

#del vehicles["f1"] #delete unavailable key
#vehicles.pop("f1",None) #default is none, if nothing  or not found, its none no error
result=vehicles.pop("f1", "hi.. doesnt exist")
print(result)

plane=vehicles.pop("learjet")
print(plane)

bike=vehicles.pop("tenere","not present")
print(bike)
# for k in vehicles:
#     print(k,vehicles[k],sep=", ")

for key, value in vehicles.items():
    print(key, value, sep=", ")
