#include <algorithm>
#include <iostream>
#include <vector>
#include<tuple>
using namespace std;
typedef long long ll;

//지도 크기 : 최대 15
string arr[20];
bool light[20][20]; //불이 켜진 곳인가?
int n;
string a;

//우, 하, 좌, 상, 나머지 대각선, 제자리
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
	//기절을 하지 않으면 true
	bool ans = true;
	cin >> n;
	cin >> a;
	for (int i = 0; i < n; i++) cin >> arr[i];

	//초기 설정 : (0, 0), 아래보며 시작
	int ari_y = 0, ari_x = 0, ari_dir = 1;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			//해당 칸에 좀비가 있으면 기록.
			if (arr[i][j] == 'Z') {
				z.push_back(make_tuple(i, j, 1));
			}
		}
	}

	//주어진 순서에 따라 이동을 한다.
	for (int i = 0; i < a.size() - 1; i++) {
		char cmd = a[i];
		//1. 아리 먼저 이동
		if (cmd == 'F') {
			int ny = ari_y + move_y[ari_dir];
			int nx = ari_x + move_x[ari_dir];
			//이동할 수 있다면
			if (0 <= ny && ny < n && 0 <= nx && nx < n) {
				ari_y = ny; ari_x = nx;
				//1. 이동한 곳에 전구가 있다면?
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
		//2. 좀비 이동
		for (int j = 0; j < z.size(); j++) {
			int zy, zx, zdir;
			tie(zy, zx, zdir) = z[j];

			if (!light[zy][zx] && zy == ari_y && zx==ari_x) ans = false;

			int ny = zy + move_y[zdir];
			//좀비가 이동할 수 있다면
			if (0 <= ny && ny < n) {
				zy = ny;
				if (!light[ny][zx] && ny == ari_y && zx == ari_x) ans = false;

			}
			//좀비가 벽에 부딫치게 되면
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