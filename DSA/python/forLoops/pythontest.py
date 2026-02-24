print("\n=== 2. Loop Through List ===")
fruits = {"apple", "banana", "cherry"}

while True:
    fruit = input("what do you want (or 'q' to quit): ")
    if fruit == "q":
        break # breaks the while loop
    fruits.append(fruit)

for i in fruits:
    print(f"I like {i}")

# Pop with Quick Search
print("\n=== Search and Remove ===")
while True:
    search = input("Search for a fruit to remove (or 'done' to exit): ")
    if search == "done":
        break
    
    if search in fruits:
        fruits.remove(search)
        print(f"Removed '{search}' from the list")
    else:
        print(f"'{search}' not found in list")
    
    print(f"Current list: {fruits}")

print(f"\nFinal list: {fruits}")



def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]

nums1 = [10,43,54,21,42]
nums2 = [34,65,34,83]
nums3 = nums1 + nums2
temp = 0
for i in nums3:
    temp += i
print(round(temp / len(nums3)))