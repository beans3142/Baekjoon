#include<iostream>
#include<vector>
#include<queue>

#define MAX 1001

using namespace std;

vector<int> myGraph[MAX];

bool visited[MAX] = { 0 };
bool check[MAX] = { 0 };

void DFS(int x) {
    visited[x] = true;

    for (int i = 0; i < myGraph[x].size(); i++) {
        int y = myGraph[x][i];

        if (visited[y] == false) {
            cout << y << " ";
            DFS(y);
        }
    }
}

void BFS(int x) {
    queue <int> q;
    q.push(x);
    check[x] = true;

    while (!q.empty()) {

        int current = q.front();
        q.pop();
        cout << current << " ";

        //이어져 있는거 다 넣어주기
        for (int i = 0; myGraph[current].size(); i++) {
            int next = myGraph[current][i];
            cout << next << " " << ;

            if (check[next] == false) {
                check[next] = true;
                q.push(next);
            }
        }
    }
}

int main(void) {
    int n, m;

    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        myGraph[a].push_back(b);
        myGraph[b].push_back(a);
    }
    cout << 0 << " ";
    DFS(0);
    cout << "\n";
    BFS(0);


    return 0;

}