#list we can store multiple values in a single variable

food = ["gyros", "pastitsio", "souvlaki"]
food[0] = "pizza"

print(food)

for item in food:
    print(item)
for item in food:
    print(item, end=" ")

