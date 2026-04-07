#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int total_weight = 0;
    queue<int> q;
    for (int i=0;i<bridge_length;i++){
        q.push(0);
    }
    queue<int> trucks;
    for (int i=0;i<truck_weights.size();i++){
        trucks.push(truck_weights[i]);
    }
    
    while (!trucks.empty()){
        answer++;
        total_weight -= q.front();
        q.pop();
        
        if (total_weight + trucks.front() <= weight){
            q.push(trucks.front());
            total_weight += trucks.front();
            trucks.pop();
        }
        else{
            q.push(0);
        }
    }
    
    answer += bridge_length;
    
    
    return answer;
}