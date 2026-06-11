#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<stdio.h>
/*
輸入：
1.選模式
    0:測資測試
    1:人機對戰
    2:多人遊玩
    3:電腦自我對戰
A.測資模式
    2.輸入人數
    3.輸入手牌數量
    4.輸入手牌
B.人機對戰模式
    2.輸入玩家數量
    3.輸入手牌數量
    4.輸入手牌
C.多人遊玩模式
    2.輸入玩家數量
    3.輸入手牌數量
    4.輸入手牌
D.電腦自我對戰模式
    2.輸入電腦數量
    3.輸入手牌數量
    4.輸入手牌  
A,D 測試(優先處理)
B,C 進階實作
*/
typedef struct{
    int num;
    char color;
}card;
char *num[]={"","A","2","3","4","5","6","7","8","9","10","J","Q","K"};
char *color[]={"H","D","C","S"};
int main()
{

}