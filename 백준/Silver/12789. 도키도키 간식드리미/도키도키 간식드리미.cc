#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    queue<int> running_q;
    for (int i=0;i<n;i++){
        int x;
        cin >> x;
        running_q.push(x);
    }
    
    int now = 1;
    stack<int> waiting_s;
    while (!running_q.empty()){
        if (running_q.front() == now){
            running_q.pop();
            now++;
        }
        else{
            if (!waiting_s.empty() && waiting_s.top() == now){
                waiting_s.pop();
                now++;
            }
            else{
                waiting_s.push(running_q.front());
                running_q.pop();
            }
        }
    }
    
    string answer = "Nice";
    while (!waiting_s.empty()){
        if (waiting_s.top() == now){
            waiting_s.pop();
            now++;
        }
        else{
            answer = "Sad";
            break;
        }
    }
    
    cout << answer;
    
    return 0;
}