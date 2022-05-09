lion_list= ["scary","big","cat"]
elephant_list= ["big","grey","wrinkled"]
teddy_list= ["cuddly","stuffed"]
animals={
    "lion":lion_list,
    "elephant":elephant_list,
    "teddy": teddy_list,
}

#things=animals.copy()  #this will give samee... changes made to 1 will reflect to other
things={
    "lion":lion_list,
    "elephant":elephant_list,
    "teddy": teddy_list,
}#this code is same as animal.copy



print(things["teddy"])
print(animals["teddy"])

print()

#things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(things["teddy"])
print(animals["teddy"])
print(teddy_list)
print(animals)
