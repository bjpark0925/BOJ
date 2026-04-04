#include <iostream>
#include <string>
using namespace std;
int main(){
    string s;
    cin >> s;
    
    int count[26] = {0};
    for (int i=0;i<s.size();i++){
        count[toupper(s[i]) - 'A']++;
    }
    
    int maxVal = 0; // maxVal = *max_element(count, count + 26);
    for (int i=0;i<26;i++){ // sizeof(count)/sizeof(count[0]) 대신 26
        if (count[i] > maxVal){
            maxVal = count[i];
        }
    }
    
    int maxCount = 0;
    char answer;
    for (int i=0;i<26;i++){
        if (count[i] == maxVal){
            maxCount++;
            answer = 'A' + i;
        }
    }
    
    if (maxCount > 1){
        answer = '?';
    }
    
    cout << answer << endl;
    
    return 0;
}