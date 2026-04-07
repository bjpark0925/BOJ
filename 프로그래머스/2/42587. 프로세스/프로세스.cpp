#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    
    deque<int> pq(priorities.begin(), priorities.end());
    deque<int> lq;
    for (int i=0;i<priorities.size();i++){
        lq.push_back(i);
    }
    
    int pmax = *max_element(pq.begin(), pq.end());
    while (!pq.empty()){
        if (pq.front() == pmax){
            answer++;
            if (lq.front() == location){
                return answer;
            }
            else{
                pq.pop_front();
                lq.pop_front();
                pmax = *max_element(pq.begin(), pq.end());
            }
        }
        else{
            pq.push_back(pq.front());
            pq.pop_front();
            lq.push_back(lq.front());
            lq.pop_front();
        }
    }
    
    
    
    return answer;
}