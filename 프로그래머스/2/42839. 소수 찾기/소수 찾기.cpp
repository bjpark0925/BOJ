#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

set<int> candidates; // 소수 후보 저장

bool isPrime(int num){
    if (num < 2) return false;
    for (int i=2;i*i<=num;i++){
        if (num%i == 0) return false;
    }
    return true;
}

void permutation(string current, string remain){
    if (!current.empty()){
        candidates.insert(stoi(current));
        // cout << current << "\n";
    }
    
    // {"", 217} -> {"2", 17}
    for (int i=0;i<remain.size();i++){
        if (current.empty() && remain[i] == '0') continue;
        string next = remain;
        next.erase(i, 1);
        permutation(current + remain[i], next);
    }
}

int solution(string numbers) {
    int answer = 0;
    permutation("", numbers);
    
    for (auto num : candidates){
        if (isPrime(num)) answer++;
    }
    
    return answer;
}