#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    set<string> record;
    int answer = 0;
    
    for (int i=0;i<n;i++){
        string s;
        cin >> s;
        if (s == "ENTER"){
            record.clear();
        }
        else{
            if (record.find(s) == record.end()){
                record.insert(s);
                answer++;
            }
        }
    }
    
    cout << answer;
    
    return 0;
}