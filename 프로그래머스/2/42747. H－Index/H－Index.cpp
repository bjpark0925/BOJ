#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(), citations.end());
    int n = citations.size();
    for (int i=n;i>=0;i--){
        if (citations[i] >= n-i){
            answer = n-i;
        }
    }
    return answer;
}