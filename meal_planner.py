from contents import pantry, recipes

def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add tuple containing item and amount to data"""
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item]=data.setdefault(item, 0) + amount   #this method helps add data if key present, if not present creat new key and add default value 0

# display_dict= {str(index+1): meal for index,meal in enumerate(recipes)}
# print(display_dict)
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list={}
while True:
    # display a menu of recipe
    print("please choose your recipes")
    print("--------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected: {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
#          if food_item in pantry:
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item}: ok")
            else:
                quantity_to_buy=required_quantity-quantity_in_pantry
                print(f"You need to buy {quantity_to_buy} of {food_item}")
                #print(f"\tYou dont have necessary ingredient {food_items}")
                add_shopping_item(shopping_list,food_item,quantity_to_buy)

for things in shopping_list.items():
    print(things)