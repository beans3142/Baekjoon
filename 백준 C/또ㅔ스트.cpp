#include <stdio.h>
#include<string.h>
int main() {
    char arr[1001];
    //Please Enter Your Code Here
    fgets(arr, 1001, stdin);
    int len = strlen(arr);
    //printf("%d",len);
    //12
    for (int i = 0; i < len / 2; i++) {
        char temp;
        temp = arr[i];
        arr[i] = arr[len - i - 1];
        arr[len - i - 1] = temp;
    }
    for (int i = 0; i < len; i++) {
        printf("%c", arr[i]);
    }
    return 0;
}