#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    /*
    # 48의 약수: 1,2,3,4, 6*8, 12,16,24,48
    # 노랑 24의 약수: 1,2,3, 4(6-2)*6(8-2), 8,12,24
    # 갈색 24 = (6+8)*2-4
    */
    
    int num = brown + yellow;
    for (int i=3;i<num;i++){
        if (i*i > num){
            break;
        }
        if (num % i == 0 && yellow % (i-2) == 0 && (i + (num / i))*2 - 4 == brown){
            answer.push_back(num / i);
            answer.push_back(i);
        }
    }
    
    return answer;
}