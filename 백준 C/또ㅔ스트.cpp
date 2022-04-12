#include <iostream>
#include<vector>
#include<stack>
#include<algorithm>
#define MAX 1000
//각 숫자에서 부모노드로 가면서 숫자 세기

using namespace std;

int main() {
    int N, X, Y, a, b, root = 0, cnt = 0;

    vector<int> v(MAX); //index 자식 value 부모
    stack<int> st;
    int depth[1001] = { 0, };
    depth[0] = 1;

    cin >> N >> X >> Y;

    for (int i = 0; i < N; i++) { //setting
        cin >> a >> b; //a는 부모노드 b는 자식노드 
        depth[b] = depth[a] + 1;
        v[b] = a;
    }
    while (depth[X] > depth[Y])
    {
        X = v[X];
    }
    while (depth[Y] > depth[X])
    {
        Y = v[Y];
    }
    while (X != Y) {//부모 노드가 같으면 cnt 멈추기

        if (X != Y && X != root) {
            X = v[X];
            cnt++;
        }
        if (X != Y && Y != root) {
            Y = v[Y];
            cnt++;
        }
    }
    cout << cnt;

    return 0;
}