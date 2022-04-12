#include <iostream>
#include<vector>
#include<stack>
#include<algorithm>
#define MAX 1000
//�� ���ڿ��� �θ���� ���鼭 ���� ����

using namespace std;

int main() {
    int N, X, Y, a, b, root = 0, cnt = 0;

    vector<int> v(MAX); //index �ڽ� value �θ�
    stack<int> st;
    int depth[1001] = { 0, };
    depth[0] = 1;

    cin >> N >> X >> Y;

    for (int i = 0; i < N; i++) { //setting
        cin >> a >> b; //a�� �θ��� b�� �ڽĳ�� 
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
    while (X != Y) {//�θ� ��尡 ������ cnt ���߱�

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