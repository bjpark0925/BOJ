#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    unordered_map<string, unordered_set<string>> clothes_map;
    for (auto& p : clothes){
        clothes_map[p[1]].insert(p[0]);
    }
    
    for (auto& [type, items] : clothes_map){
        answer *= (items.size()+1);
    }
    answer--;
    
    
    /*
    for (auto& c : clothes_map){
        cout << c.second.size() << "\n";
    }
    */
    
    return answer;
}