#include <stdio.h>
#include <string.h>
int size;
bool isVps;
struct Stack {
    int data[100];
    int front = 0;

    void push(int x) {
        data[front] = x;
        front++;
    }


    void pop() {
        front--;
        if (data[front] == 1) {
            data[front] = 0;
        }
        if (front < 0) {
            isVps = true;
        }
    }
};
int main() {

    //Please Enter Your Code Here

    char arr[100];

    fgets(arr, 100, stdin);

    size = strlen(arr);

    Stack s1;

    for (int i = 0; i < size; i++) {
        if (arr[size - 1] == 40) {
            isVps = true;
            break;
        }

        if (arr[i] == 40) {
            s1.push(1);
        }
        else {
            s1.pop();
        }
    }

    if (isVps == true) {
        printf("NO\n");
    }
    else {
        printf("YES\n");
    }


    return 0;
}