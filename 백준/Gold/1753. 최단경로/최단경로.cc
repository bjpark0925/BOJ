#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int V, E;
    cin >> V >> E;
    
    int K; // 시작점
    cin >> K;
    
    vector<vector<pair<int, int>>> graph(V+1); // {가중치, 도착정점}
    
    for (int i=0;i<E;i++){
        int u,v,w;
        cin >> u >> v >> w;
        graph[u].push_back({w,v}); // 방향 그래프
    }
    
    vector<int> distances(V+1, INT_MAX); // 파이썬 float('INF') 대체
    distances[K] = 0;
    
    // {거리, 정점} 최소힙
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push({0,K});
    
    while (!pq.empty()){
        auto [dist, now] = pq.top();
        pq.pop();
        
        // 이미 처리된 정점 스킵
        if (dist > distances[now]) continue;
        
        // 이웃 방문(간선 완화)
        for (auto [weight, next] : graph[now]){
            if (distances[now] + weight < distances[next]){
                distances[next] = distances[now] + weight;
                pq.push({distances[next], next});
            }
        }
    }
    
    for (int i=1;i<=V;i++){
        if (distances[i] == INT_MAX){
            cout << "INF" << "\n";
        }
        else{
            cout << distances[i] << "\n";
        }
    }
    
    return 0;
}