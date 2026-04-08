#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

long long solution(int n, vector<int> times) {
    // long long answer = 0;
    long long left = 0;
    long long right = (long long)*min_element(times.begin(), times.end()) * n;
    
    while (left < right){
        long long mid = (left + right) / 2;
        long long cnt = 0;
        for (auto t : times){
            cnt += mid / t;
            if (cnt >= n) break;
        }
        if (cnt >= n){
            right = mid;
        }
        else{
            left = mid+1;
        }
    }
    
    return left;
}