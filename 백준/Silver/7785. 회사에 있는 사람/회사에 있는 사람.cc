#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    set<string> office_set;
    
    for (int i=0;i<n;i++){
        string name, status;
        cin >> name >> status;
        if (status == "enter"){
            office_set.insert(name);
        }
        else{
            office_set.erase(name);
        }
    }
    
    for (auto it = office_set.rbegin(); it != office_set.rend(); it++){
        cout << *it << "\n";
    }
    
    return 0;
}