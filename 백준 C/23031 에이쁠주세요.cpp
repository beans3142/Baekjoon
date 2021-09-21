#include <algorithm>
#include <iostream>
#include <vector>
#include<tuple>
using namespace std;
typedef long long ll;

//���� ũ�� : �ִ� 15
string arr[20];
bool light[20][20]; //���� ���� ���ΰ�?
int n;
string a;

//��, ��, ��, ��, ������ �밢��, ���ڸ�
int dy[] = { 0, 1, 0, -1, 1, 1, -1, -1, 0 };
int dx[] = { 1, 0, -1, 0, 1, -1, 1, -1, 0 };

int move_y[] = { 0, 1, 0, -1 };
int move_x[] = { -1, 0, 1, 0 };


vector<tuple<int, int, int> >z;


int turn_left(int x) {
	if (x == 3) return 0;
	else return x + 1;
}
int turn_right(int x) {
	if (x == 0) return 3;
	else return x - 1;
}

int main() {
	//������ ���� ������ true
	bool ans = true;
	cin >> n;
	cin >> a;
	for (int i = 0; i < n; i++) cin >> arr[i];

	//�ʱ� ���� : (0, 0), �Ʒ����� ����
	int ari_y = 0, ari_x = 0, ari_dir = 1;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			//�ش� ĭ�� ���� ������ ���.
			if (arr[i][j] == 'Z') {
				z.push_back(make_tuple(i, j, 1));
			}
		}
	}

	//�־��� ������ ���� �̵��� �Ѵ�.
	for (int i = 0; i < a.size() - 1; i++) {
		char cmd = a[i];
		//1. �Ƹ� ���� �̵�
		if (cmd == 'F') {
			int ny = ari_y + move_y[ari_dir];
			int nx = ari_x + move_x[ari_dir];
			//�̵��� �� �ִٸ�
			if (0 <= ny && ny < n && 0 <= nx && nx < n) {
				ari_y = ny; ari_x = nx;
				//1. �̵��� ���� ������ �ִٸ�?
				if (arr[ari_y][ari_x] == 'S') {
					for (int k = 0; k < 9; k++) {
						int nny = ari_y + dy[k];
						int nnx = ari_x + dx[k];
						if (0 <= nny && nny < n && 0 <= nnx && nnx < n) light[nny][nnx] = true;
					}
				}
			}
		}
		else if (cmd == 'L') ari_dir = turn_left(ari_dir);
		else ari_dir = turn_right(ari_dir);
		cout <<'\n' << ari_x <<' ' << ari_y << endl;
		//2. ���� �̵�
		for (int j = 0; j < z.size(); j++) {
			int zy, zx, zdir;
			tie(zy, zx, zdir) = z[j];

			if (!light[zy][zx] && zy == ari_y && zx==ari_x) ans = false;

			int ny = zy + move_y[zdir];
			//���� �̵��� �� �ִٸ�
			if (0 <= ny && ny < n) {
				zy = ny;
				if (!light[ny][zx] && ny == ari_y && zx == ari_x) ans = false;

			}
			//���� ���� �΋Hġ�� �Ǹ�
			else {
				zdir = (zdir + 2) % 4;
			}
			cout << zx << ' ' << zy << '\t';
			z[j] = make_tuple(zy, zx, zdir);
		}
	}

	if (ans) cout << "Phew...";
	else cout << "Aaaaaah!";
	return 0;
}