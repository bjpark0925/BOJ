#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    deque<char> dq;
    for (char& num : number){
        while (!dq.empty() && k>0 && dq.back() < num){
            dq.pop_back();
            k--;
        }
        dq.push_back(num);
    }
    
    for (int i=0;i<dq.size();i++){
        answer += dq[i];
    }
    
    if (k>0){
        answer = answer.substr(0, answer.size()-k);
    }
    
    return answer;
}