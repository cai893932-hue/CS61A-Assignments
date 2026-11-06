class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        hash_map={}
    for i , num in enumerate(nums):
        y = target - num
        if y in hash_map:
            return [hash_map[y],i]
        hash_map[num] = i
    return []

    }
};
