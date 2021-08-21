nums = [88, 55, 3, 10001, 1, 6, 98]
maxi = nums[0]

for i in range(len(nums) - 1):
    maxi = max(maxi, nums[i + 1])

print(maxi)
