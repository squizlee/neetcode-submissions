class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> concat;
        concat.reserve(nums.size() * 2);

        concat.insert(concat.end(), nums.begin(), nums.end());
        concat.insert(concat.end(), nums.begin(), nums.end());

        return concat;
    }
};