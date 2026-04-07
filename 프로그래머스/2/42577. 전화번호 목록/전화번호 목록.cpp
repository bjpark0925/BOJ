#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool solution(vector<string> phone_book) {
    unordered_set<string> phone_set;
    
    for (string s : phone_book){
        phone_set.insert(s);
    }
    
    for (string s : phone_book){
        string temp = "";
        for (int i=0;i<s.size()-1;i++){
            temp += s[i];
            if (phone_set.count(temp)){
                return false;
            }
        }
    }
    
    return true;
}