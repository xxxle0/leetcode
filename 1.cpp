class Solution {
  public:
    vector<int> twoSum(vector<int> &nums, int target) {
      unordered_map map<int, int>;
      for (int i = 0; i < nums.length; i++) {
        int remain = target - nums[i];
        if (dict.find(remain) != dict.end()) {
          return {i, dict[nums[i]]};
        }
        dict[nums[i]] = i;
      }
      return {};
    }
}
