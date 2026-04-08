#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int answer = 0;

// global 선언보다 함수 인자 전달이 효율적(참조 가능, 초기화 실수 없음)
void dfs(vector<int>& numbers, int target, int idx, int sum){
    if (idx == numbers.size()){
        if (sum == target){
            answer++;
        }
        return;
    }
        
    dfs(numbers, target, idx+1, sum+numbers[idx]);
    dfs(numbers, target, idx+1, sum-numbers[idx]);
}

int solution(vector<int> numbers, int target) {    
    dfs(numbers, target, 0,0); // dfs(1,4) -> dfs(2,5) -> dfs(3,7) -> dfs(4,8)
    
    return answer;
}