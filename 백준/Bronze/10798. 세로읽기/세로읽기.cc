#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
	string s[5];
    for (int i=0;i<5;i++){
        cin >> s[i];
    }
    
    for (int j=0;j<15;j++){
        for (int i=0;i<5;i++){
            if (j < s[i].size())
            cout << s[i][j];
        }
    }
	return 0;
}