#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    // 개수 내림차순 > 길이 내림차순 > 사전순
    int n, m;
    cin >> n >> m;
    map<string, int> freq;
    
    for (int i=0;i<n;i++){
        string s;
        cin >> s;
        if (s.size() >= m){
            freq[s]++;
        }       
    }
    
    vector<string> words;
    for (auto& p : freq){
        words.push_back(p.first);
    }
    
    sort(words.begin(), words.end(), [&](string a, string b){
        if (freq[a] != freq[b]) return freq[a] > freq[b];
        if (a.size() != b.size()) return a.size() > b.size();
        return a < b;
    });
    
    for (string s : words){
        cout << s << "\n";
    }
    
    return 0;
}