class SumSolution():
  def threeSumClosest(self, nums: list[int], target: int) -> int:
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
      for j in range(i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums)):
          current_sum = nums[i] + nums[j] + nums[k]
          if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
    return closest_sum

solutionObject = SumSolution()
print(solutionObject.threeSumClosest([-1,2,1,-4], 1))