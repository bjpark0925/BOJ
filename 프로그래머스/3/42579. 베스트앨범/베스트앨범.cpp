#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    /*
    재생수 합 많은 장르 > 한 장르 내 많은 재생수 > 낮은 고유 번호
    한 장르당 최대 2곡
    {장르, 총재생수, [재생수, 고유번호]}
    key:value는 map
    */
    map<string, int> genre_freq;
    map<string, vector<pair<int, int>>> play_freq;
    
    for (int i=0;i<genres.size();i++){
        genre_freq[genres[i]] += plays[i];
        play_freq[genres[i]].push_back({plays[i], i});
    }
    /*
    for (auto& [g, c] : genre_freq){
        cout << g << c << endl;
    }
    */
    
    // genre_freq 정렬
    vector<pair<int, string>> sorted_genre_freq;
    for (auto& [genre, total] : genre_freq){
        sorted_genre_freq.push_back({total, genre});
    }
    sort(sorted_genre_freq.begin(), sorted_genre_freq.end(), [](auto& a, auto& b){
        return a.first > b.first;
    });
    
    // play_freq 정렬(재생수 내림차순, 고유번호 오름차순)
    for (auto& [genre, songs] : play_freq){
        sort(songs.begin(), songs.end(), [](auto& a, auto& b){
            // first는 재생수, second는 고유번호
            if (a.first != b.first) return a.first > b.first;
            return a.second < b.second;
        });
    }
    
    // 한 장르당 최대 2곡
    for (auto& [total, genre] : sorted_genre_freq){
        auto& songs = play_freq[genre];
        for (int i=0; i < 2; i++){
            if (i >= songs.size()) break;
            answer.push_back(songs[i].second);
        }
    }
    
    
    return answer;
}