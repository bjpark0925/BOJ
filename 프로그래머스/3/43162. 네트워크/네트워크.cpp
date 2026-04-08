#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    // bfs
    deque<int> q;
    vector<bool> visited(n, false); // {i번 노드의 방문여부}
    for (int i=0;i<n;i++){
        q.push_back(i);
        if (visited[i]) continue;
        
        while (!q.empty()){
            int now = q.front();
            visited[now] = true;
            q.pop_front();
            for (int next=0;next<n;next++){
                if (next == now || computers[now][next] == 0 || visited[next])
                    continue;
                q.push_back(next);
            }
        }
        answer++;
    }
    
    return answer;
}