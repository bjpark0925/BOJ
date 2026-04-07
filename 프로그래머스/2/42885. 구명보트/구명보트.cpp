#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    /*
    투 포인터
    합이 limit보다 크면 end만 탑승, 아니면 둘다 탑승
    50 50 70 80
    */
    sort(people.begin(), people.end());
    
    int start = 0;
    int end = people.size() - 1;
    while (start <= end){
        if (people[start] + people[end] <= limit){
            start++;
        }
        end--;
        answer++;
    }
    
    return answer;
}