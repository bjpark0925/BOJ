#include <bits/stdc++.h>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> mp;
    for (auto s : participant){
        mp[s] += 1;
    }
    
    for (auto s : completion){
        mp[s] -= 1;
    }
    
    for (auto i : mp){
        if (i.second != 0){
            answer += i.first;
            break;
        }
    }
    
    return answer;
}