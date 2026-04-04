#include <iostream>
#include <string>
using namespace std;
int main(){
    int T;
    cin >> T;
    for (int i=0;i<T;i++){
        string s;
        cin >> s;
        cout << s.front() << "" << s.back() << endl;
    }
    return 0;
}