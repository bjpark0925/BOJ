#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int n = jobs.size();
    int total_time = 0; // answer = total_time / jobs.size()
    int current_time = 0;
    int idx = 0; // jobs 순회
    
    // jobs 정렬
    sort(jobs.begin(), jobs.end());
    /*
    for (int i=0;i<n;i++){
        cout << jobs[i][0] << " " << jobs[i][1] << "\n";
    }
    */
    
    // jobs: {요청시각, 소요시간}
    // pq: {소요시간, 요청시각, 번호}
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    
    while (idx < n || !pq.empty()){
        while (idx<n && jobs[idx][0] <= current_time){
            pq.push({jobs[idx][1], jobs[idx][0], idx});
            idx++;
        }
        
        if (!pq.empty()){
            current_time += pq.top()[0]; // +소요시간
            total_time += current_time - pq.top()[1]; // 완료시각 - 요청시각
            pq.pop();
        }
        else{
            current_time = jobs[idx][0];
        }
    }
    
    return total_time / n;
}