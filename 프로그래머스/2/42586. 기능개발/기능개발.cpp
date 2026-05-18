#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int n = progresses.size();
    int cnt = 0;
    
    while (cnt < n){
        for (int i=cnt; i<n; i++){
            progresses[i] += speeds[i];
        }
        
        if (progresses[cnt] >= 100){
            int cur = cnt + 1;
            while (cur < n && progresses[cur] >= 100){
                cur++;
            }
            answer.push_back(cur-cnt);
            cnt = cur;
        }
    }
    
    return answer;
}