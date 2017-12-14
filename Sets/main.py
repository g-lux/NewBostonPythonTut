# like a list but cannot have duplicates. helpful to prevent duplicate datasets

groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'beer'}
print(groceries)

if 'milk' in groceries:
    print("you already have milk")
else:
    print("you need milk")
