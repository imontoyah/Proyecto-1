
def sumaGrupo(start, nums, target): 
    if start >= len(nums):
        if target == 0:
            return True
        else:
            return False
    return sumaGrupo(start+1, nums, target) or sumaGrupo(start+1, nums, target-nums[start])

print(sumaGrupo(0, [2,4,8], 10))