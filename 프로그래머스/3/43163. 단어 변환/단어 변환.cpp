#include <bits/stdc++.h>

using namespace std;

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    deque<pair<string, int>> dq;
    unordered_set<string> visited;
    dq.push_back({begin, 0});
    visited.insert(begin);

    while (!dq.empty()){
        auto [now, cnt] = dq.front();
        dq.pop_front();
        if (now == target){
            answer = cnt;
            break;
        }
        
        for (auto next : words){
            if (visited.count(next) != 0){
                continue;
            }
            int same_cnt = 0;
            for (int i=0;i<now.size();i++){
                if (now[i] == next[i]){
                    same_cnt++;
                }
            }
            if (same_cnt == now.size() - 1){
                dq.push_back({next, cnt+1});
                visited.insert(next);
            }
        }
    }
    
    return answer;
}