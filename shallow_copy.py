import copy

animals={
    "lion": ["scary","big","cat"],
    "elephant": ["big","grey","wrinkled"],
    "teddy": ["cuddly","stuffed"],
}

#things=animals  #this will give samee... changes made to 1 will reflect to other
#bellow is shallow copy code:::::::::::
#things=animals.copy()  #this will make copy, change to one will no affect other
#will not work if values are list
#animals["teddy"]="toy"

#deep copy::::
things=copy.deepcopy(animals)
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"]) # id is the location id og lists

#print(things["teddy"])
#print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
