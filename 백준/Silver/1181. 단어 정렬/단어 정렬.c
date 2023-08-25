#pragma warning(disable: 4996)
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX_SIZE 51

//버블소트, 선택정렬이 O(n^2)이라 시간초과
//stdlib.h의 qsort()함수 이용

typedef struct {
    char string[MAX_SIZE];
    int len;
}WORD;

int compare(const void* a, const void* b)
{
    WORD real_a = *(WORD*)a;
    WORD real_b = *(WORD*)b;
    int len_a = strlen(real_a.string);
    int len_b = strlen(real_b.string);
    if (len_a != len_b)
        return (len_a - len_b);
    return strcmp(real_a.string, real_b.string);
}

int main()
{
    int N;
    scanf("%d", &N);

    WORD* word = (WORD*)malloc(sizeof(WORD) * N);
    
    //같은 단어 제외 위해
    int flag = 0;
    int real_N = 0;
    char temp[MAX_SIZE] = { 0 };

    for (int i = 0; i < N; i++)
    {
        scanf("%s", temp);

        //같은 단어는 저장하지 않음
        for (int j = 0; j < i; j++)
        {
            if (strcmp(word[j].string, temp) == 0)
            {
                flag = 1;
                break;
            }
        }

        //같은 단어가 아니라면
        if (flag == 0)
        {
            strcpy(word[real_N].string, temp);
            word[real_N].len = strlen(temp);
            real_N++;
        }
        flag = 0;
    }

    qsort(word, real_N, sizeof(WORD), compare);
    for (int i = 0; i < real_N; i++)
        printf("%s\n", word[i].string);

    free(word);

    return 0;
}