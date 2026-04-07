#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> s_numbers;
    for (int n : numbers){
        s_numbers.push_back(to_string(n));
    }
    
    // 두 문자 이어붙였을 때 더 큰 쪽이 앞으로
    sort(s_numbers.begin(), s_numbers.end(), [](string& a, string& b){
        return a+b > b+a;
    });
    
    if (s_numbers[0] == "0") return "0";
    
    for (string& s : s_numbers){
        answer += s;
    }
    
    return answer;
}