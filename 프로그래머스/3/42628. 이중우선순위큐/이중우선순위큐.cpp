#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer(2,0);
    priority_queue<pair<int, int>> pq_max;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq_min;
    vector<bool> alive;
    int num_cnt = 0;
    int idx = 0;
    
    for (auto& s : operations){
        int num = stoi(s.substr(2));
        
        
        if (s[0] == 'I'){
            pq_max.push({num, idx});
            pq_min.push({num, idx});
            alive.push_back(true);
            idx++;
            num_cnt++;
        }
        else{
            if (num_cnt == 0){
                continue;
            }
            
            if (num == 1){
                while (!pq_max.empty() && !alive[pq_max.top().second]){
                    pq_max.pop();
                }
                if (!pq_max.empty()){
                    alive[pq_max.top().second] = false;
                    pq_max.pop();
                    num_cnt--;
                }
            }
            else{
                while (!pq_min.empty() && !alive[pq_min.top().second]){
                    pq_min.pop();
                }
                if (!pq_min.empty()){
                    alive[pq_min.top().second] = false;
                    pq_min.pop();
                    num_cnt--;
                }
            }
        }
    }
    
    if (num_cnt > 0){
        while (!pq_max.empty() && !alive[pq_max.top().second]) pq_max.pop();
        while (!pq_min.empty() && !alive[pq_min.top().second]) pq_min.pop();
        answer[0] = pq_max.top().first;
        answer[1] = pq_min.top().first;
    }
    
    return answer;
}