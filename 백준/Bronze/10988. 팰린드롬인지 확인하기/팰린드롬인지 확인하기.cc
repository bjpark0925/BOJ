#include <iostream>
#include <string>
using namespace std;
int main(){
    string s;
    cin >> s;
    int answer = 1;
    for (int i=0;i<(s.size()/2);i++){
        if (s[i] != s[s.size()-1-i]){
            answer = 0;
            break;
        }
    }
    cout << answer << endl;
    return 0;
}