#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
#include<cstring>

using namespace std;
queue<int>q;
vector<int>gold;
int visited[1000001];

void trace(int k) {
	if (k == 0)
		return;
	trace(visited[k]);
	cout << k - visited[k] << " ";
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int n;
	cin >> n;
	for (int j = 2; j < 200; j++) {
		vector<int>bi;
		string temp;
		int tmp = j;
		while (tmp) {
			bi.push_back(tmp % 2);
			tmp /= 2;
		}
		for (int i = bi.size() - 1; i >= 0; i--) {
			if (i == bi.size() - 1) continue;
			if (bi[i] == 0)
				temp += "4";
			else
				temp += "7";
		}
		gold.push_back(atoi(temp.c_str()));
	}

	memset(visited, -1, sizeof(visited));
	q.push(0);
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		if (now == n)
			break;
		for (int i = 0; i < gold.size(); i++) {
			int next = now + gold[i];
			if (next > n)
				continue;
			if (visited[next] == -1) {
				visited[next] = now;
				q.push(next);
			}
		}
	}
	if (visited[n] == -1) {
		cout << -1;
		return 0;
	}
	trace(n);
	return 0;
}