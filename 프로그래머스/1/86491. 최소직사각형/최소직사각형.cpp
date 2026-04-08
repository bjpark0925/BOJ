#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_width = 0, max_height = 0;
    
    for (auto& card : sizes){
        if (card[0] < card[1]){
            swap(card[0], card[1]);
        }
        max_width = max(max_width, card[0]);
        max_height = max(max_height, card[1]);
    }
    
    return max_width*max_height;
}