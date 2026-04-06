#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    vector<string> arr(n);
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    sort(arr.begin(), arr.end());
    arr.erase(unique(arr.begin(), arr.end()), arr.end());
    
    // 길이 오름차순, 같으면 사전순
    sort(arr.begin(), arr.end(), [](string a, string b){
        // 같으면 사전 순
        if (a.size() == b.size()){
            return a < b;
        }
        // 길이 오름차순
        return a.size() < b.size();
    });
    
    for (string s : arr){
        cout << s << endl;
    }
    
    return 0;
}