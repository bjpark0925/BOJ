#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(){
    string s;
    vector<string> croatia = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    cin >> s;
    
    int cnt = 0;
    int i=0;
    while (i<s.size()){
        bool found = false;
        for (string c: croatia){
            if (s.substr(i, c.size()) == c){
                cnt++;
                i += c.size();
                found = true;
                break;
            }
        }
        if (found == false){
            i++;
            cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}