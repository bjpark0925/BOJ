#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> type(n);
    for (int i = 0; i < n; i++) cin >> type[i];

    deque<int> dq;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (type[i] == 0) dq.push_back(x);  // queue만 저장
    }

    int m;
    cin >> m;

    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        dq.push_front(x);            // 앞에 삽입
        cout << dq.back() << "\n";   // 뒤에서 출력
        dq.pop_back();               // 뒤에서 삭제
    }

    return 0;
}