#include<stdio.h>
void hot();
void cold();
int main(){
    int n;
    printf("enter temperature");
    scanf("%d",&n);
    if(n<=35){
        printf("hot()");
    }
    else{
        printf("cold()");
    }


}
void hot(){
    printf("temperature is hot");
}
void cold(){
    printf("temperature is cold");
}
