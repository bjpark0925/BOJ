#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, m;
    cin >> n >> m;
    
    map<string, int> nameToNum;
    vector<string> numToName(n+1);
    
    for (int i=1;i<=n;i++){
        string name;
        cin >> name;
        nameToNum[name] = i;
        numToName[i] = name;
    }
    
    for (int i=0;i<m;i++){
        string query;
        cin >> query;
        if (isdigit(query[0])){
            cout << numToName[stoi(query)] << "\n";
        }
        else{
            cout << nameToNum[query] << "\n";
        }
    }
    
    return 0;
}