#include <bits/stdc++.h>

using namespace std;

vector<string> answer;
vector<bool> visited;
bool found = false;

void dfs(const string& cur, vector<string>& path, vector<vector<string>>& tickets){
    // found = true이면 바로 종료
    if (found == true){
        return;
    }
    // path에 cur 넣기
    path.push_back(cur);
    // 종료 조건
    if (path.size() == tickets.size()+1){
        answer = path;
        found = true;
        return;
    }
    // 다음 경로 재귀
    for (int i=0;i<tickets.size();i++){
        if (visited[i] == false && tickets[i][0] == cur){
            visited[i] = true;
            dfs(tickets[i][1], path, tickets);
            if (found) return;
            visited[i] = false;
        }
    }
    
    path.pop_back();
    return;
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    // [atl:icn], [atl:sfo], [icn:atl], [icn:sfo], [sfo:atl]
    visited.assign(tickets.size(), false);
    vector<string> path;
    
    dfs("ICN", path, tickets);    
    
    return answer;
}