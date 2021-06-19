def recursiveSolver(nums, start, k, ans, target, nos):
    if start == len(nums) and nos == k:
        for j in range(k - 1):
            if ans[j] != ans[j + 1] or ans[j] != target:
                break
        else:
            return True
    if start == len(nums):
        return False
    for i in range(len(ans)):
        if ans[i] > -1:
            ans[i] += nums[start]
            if recursiveSolver(nums, start + 1, k, ans, target, nos):
                return True
            ans[i] -= nums[start]
        else:
            ans[i] = 0 + nums[start]
            if recursiveSolver(nums, start + 1, k, ans, target, nos + 1):
                return True
            ans[i] = -1

def canPartitionKSubsets(nums, k):
    sumi = sum(nums)
    if sumi % k != 0:
        return False
    target = sumi // k
    ans = [-1 for _ in range(k)]
    return recursiveSolver(nums, 0, k, ans, target, 0)

print(canPartitionKSubsets([4,3,2,3,5,2,1],
4))