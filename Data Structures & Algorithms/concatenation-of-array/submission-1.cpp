class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> concat;
        concat.resize(nums.size() * 2);

        for (auto count{nums.size()}; count < concat.size(); ++count)
        {
            size_t i = count - nums.size();
            concat[i] = nums[i];
            concat[count] = nums[i];
        }

        return concat;
    }
};