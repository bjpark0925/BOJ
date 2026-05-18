#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    unordered_set<int> s(nums.begin(), nums.end());
    answer = min(nums.size() / 2, s.size());
    return answer;
}