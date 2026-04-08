#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    // map으로 연결 정보 저장{1:2,3/ 2:1,3,4,5/ ...}
    unordered_map<int, vector<int>> graph;
    for (int i=0;i<edge.size();i++){
        graph[edge[i][0]].push_back(edge[i][1]);
        graph[edge[i][1]].push_back(edge[i][0]);
    }
    /*
    for (int i=1;i<=n;i++){
        cout << graph[i].size() << "\n";
    }
    */
    
    // 이웃 탐색
    vector<int> dist(n+1, 0);
    vector<bool> visited(n+1, false);
    deque<int> q;
    
    q.push_back(1);
    visited[1] = true;
    
    while (!q.empty()){
        int now = q.front();
        q.pop_front();
        for (int next : graph[now]){
            if (visited[next]) continue;
            dist[next] = dist[now] + 1;
            visited[next] = true;
            q.push_back(next);
        }
    }
    
    // 가장 멀리 떨어진 노드 계산
    int maxValue = *max_element(dist.begin()+1, dist.end());
    for (int i=1;i<=n;i++){
        // cout << dist[i] << endl;
        if (dist[i] == maxValue) answer++;
    }
    
    return answer;
}