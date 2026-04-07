#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> prices) {
    int n = prices.size();
    vector<int> answer(n);
    stack<int> st; // 인덱스 저장
    
    // 1 2 3 4 5 3 3
    for (int i=0;i<n;i++){
        while (!st.empty() && prices[st.top()] > prices[i]){
            answer[st.top()] = i - st.top();
            st.pop();
        }
        st.push(i);
    }
    
    while (!st.empty()){
        answer[st.top()] = n-1-st.top();
        st.pop();
    }
    
    /*
    vector<int> answer;
    
    for (int i=0;i<prices.size();i++){
        int cnt = 0;
        for (int j=i+1;j<prices.size();j++){
            cnt++;
            if (prices[i] > prices[j]){
                break;
            }
        }
        answer.push_back(cnt);
    }
    */
    
    return answer;
}