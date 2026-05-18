#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    vector<int> answer;
    answer.push_back(arr[0]);
    for (int i=1;i<arr.size();i++){
        if (arr[i] != answer.back()){
            answer.push_back(arr[i]);
        }
    }

    return answer;
}