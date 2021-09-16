#include<stdio.h>
#include<stdlib.h>

int arr[1001];
int cnt[1001];

int cmp(const void* a, const void* b) {
    int n1 = *(int*)a;
    int n2 = *(int*)b;

    return n1 - n2;
}

int main() {

    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    qsort(arr, n, sizeof(int), cmp);

    int max = 0, r = 0;

    while (r < n) {
        int sum = 0;
        for (int i = n - 1; i >= r; i--) {
            sum += arr[r];
        }
        r++;

        if (max < sum) {
            max = sum;
        }
    }

    printf("%d", max);

}