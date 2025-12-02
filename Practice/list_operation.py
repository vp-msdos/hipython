"""
reverse
sort
count
Membership operation
"""

nums = [1, 2, 3, 4, 6, 5,5]
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)

#count
print(nums.count(5))

#membership
print(5 in nums)
print(8 not in nums)

#Numerical Operations in list

print(min(nums))
print(max(nums))
print(sum(nums))

#Nested lists
n1 = [1, 2, 3]
n2 = [4, 5, 6]
n3 = [7, 8, 9]
#n1.append(n2)
print(n1)
print(len(n1))
n1.extend(n2)
n1.extend(n3)
print(n1)
