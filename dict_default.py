from contents import pantry

chicken_quantity= pantry.setdefault("chicken",0)
print(f"chicken: {chicken_quantity}")

beans_quantity=pantry.setdefault("beans",0)
print(f"Beans: {beans_quantity}")

ketchup_quantity=pantry.get("ketchup",0)
print(f"ketchup: {ketchup_quantity}")
# this gives output 0 too if not present, the get method
# but doesn't add it to dictionary, while set default does add

print()
print(" `pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)