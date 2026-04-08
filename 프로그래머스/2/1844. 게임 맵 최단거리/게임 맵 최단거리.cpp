#include<vector>
#include <bits/stdc++.h>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int answer = -1;
    // bfs
    int n = maps.size();
    int m = maps[0].size();
    queue<pair<int,int>> q; // {row, col}
    vector<vector<int>> dist(n, vector<int>(m, -1)); // 거리 저장 겸 visited 역할
    q.push({0,0});
    dist[0][0] = 1;
    
    int dir[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    while (!q.empty()){
        auto [row, col] = q.front();
        q.pop();
        if (row == n-1 && col == m-1){
            answer = dist[row][col];
            break;
        }
        
        for (auto [dx, dy] : dir){
            int nx = row + dx;
            int ny = col + dy;
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (dist[nx][ny] != -1) continue;
            if (maps[nx][ny]){
                q.push({nx, ny});
                dist[nx][ny] = dist[row][col]+1;
            }
        }
    }
    
    return answer;
}