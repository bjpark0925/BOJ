#include <iostream>

using namespace std;
int main(){
    int n;
    cin >> n;
    int count = 0;
    
    for (int i=0;i<n;i++){
        string s;
        cin >> s;

        bool visited[26] = {false};
        bool isGroup = true;

        for (int j=0;j<s.size();j++){
            int c = s[j] - 'a';
            if (s[j] != s[j-1]){
                if (visited[c]){
                    isGroup = false;
                    break;
                }
                visited[c] = true;
            }
        }
        if (isGroup) count++;
    }
    cout << count << endl;
    return 0;
}