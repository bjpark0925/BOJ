#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int m;
    cin >> m;
    
    int S = 0;
    
    while (m--){
        string op;
        cin >> op;
        
        if (op == "all"){
            S = (1<<21) - 1; // 모든 비트 1로
        }
        else if(op == "empty"){
            S = 0;
        }
        else{
            int x;
            cin >> x;
            
            if (op == "add"){
                S |= (1<<x);
            }
            else if (op == "remove"){
                S &= ~(1<<x);
            }
            else if (op == "check"){
                if (S & (1<<x)) cout << 1 << "\n";
                else cout << 0 << "\n";
            }
            else if (op == "toggle"){
                S ^= (1<<x);
            }
        }
    }
    
    return 0;
}