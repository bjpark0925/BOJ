#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int n = answers.size();
    vector<int> cnt(3,0);
    vector<int> a = {1,2,3,4,5};
    vector<int> b = {2,1,2,3,2,4,2,5};
    vector<int> c = {3,3,1,1,2,2,4,4,5,5};
    for (int i=0;i<n;i++){
        // 1번 수포자
        if (answers[i] == a[i%a.size()]){
            cnt[0]++;
        }
        // 2번 수포자
        if (answers[i] == b[i%b.size()]){
            cnt[1]++;
        }
        // 3번 수포자
        if (answers[i] == c[i%c.size()]){
            cnt[2]++;
        }
    }
    
    int maxVal = *max_element(cnt.begin(), cnt.end());
    for (int i=0;i<cnt.size();i++){
        if (cnt[i] == maxVal){
            answer.push_back(i+1);
        }
    }
    
    return answer;
}