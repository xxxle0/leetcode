class Solution {
  public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> results;
        int prev = 0;
        for (int i = 0; i < nums.size(); i++) {
          results.push_back(nums[i] + prev);
          prev = nums[i] + prev;
        }
    }
    return results;
}
