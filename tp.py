jewels = input("Enter Jewel: ")
stones = input("Enter stones: ")

jewels_set = set(jewels)
count = sum(stone in jewels_set for stone in stones)
print(count)