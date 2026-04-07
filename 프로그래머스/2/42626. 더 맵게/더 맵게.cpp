#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    for (auto& p : scoville){
        pq.push(p);
    }
    /*
    while (!pq.empty()){
        cout << pq.top() << endl;
        pq.pop();
    }
    */
    bool fail = false;
    while (true){
        if (pq.top() < K){
            if (pq.size() > 1){
                int a = pq.top();
                pq.pop();
                int b = pq.top();
                pq.pop();
                pq.push(a+(b*2));
                answer++;
            }
            else{
                fail = true;
                break;
            }
        }
        else{
            break;
        }
    }
    
    if (fail) answer = -1;
    
    
    return answer;
}