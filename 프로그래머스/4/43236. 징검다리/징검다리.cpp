#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    sort(rocks.begin(), rocks.end());
    vector<int> diff; // 2 9 3 3 4 4
    diff.push_back(rocks[0]);
    for (int i=1;i<rocks.size();i++){
        diff.push_back(rocks[i]-rocks[i-1]);
    }
    diff.push_back(distance - rocks.back());
    
    int left = 0;
    int right = distance;
    while (left <= right){
        int mid = (left + right) / 2; // answer
        int cnt = 0; // 치운 돌 수
        deque<int> q(diff.begin(), diff.end());
        while (!q.empty()){
            int x = q.front();
            q.pop_front();
            if (x < mid){
                cnt++;
                if (!q.empty()){
                    int y = q.front();
                    q.pop_front();
                    q.push_front(x+y);
                }
            }
        }
        if (cnt > n){
            right = mid - 1;
        }
        else{
            left = mid + 1;
        }
    }
    
    
    return right;
}