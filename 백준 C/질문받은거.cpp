#include <iostream>
#include <vector>

using namespace std;

struct Object {  // 좀비, 스위치, 주인공의 정보를 저장하기 위한 구조체 선언
	int d = 0;  // 현재 바로보고 있는 방향(row, column)
	pair<int, int> pos = make_pair(0, 0);  // 현재 위치해 있는 좌표
};

int N;  // 지도의 가로 및 세로 길이
string A;  // 주인공의 행동 입력
bool isOn[15][15];
vector<string> M;  // 지도 정보 배열
vector<struct Object> Z;  // 좀비 정보 배열
Object P;  // 주인공 객체
bool isShocked;  // 주인공이 기절했는지 확인하기 위한 변수

int dr[4] = { 1, 0, -1, 0 };
int dc[4] = { 0, 1, 0, -1 };

void input() {
	cin >> N;
	cin >> A;
	for (int row = 0; row < N; row++) {
		string input_row;
		cin >> input_row;
		M.push_back(input_row);
		for (int column = 0; column < N; column++) {
			if (input_row[column] == 'Z') {
				Object newZombie;
				newZombie.pos.first = row;
				newZombie.pos.second = column;
				Z.push_back(newZombie);
			}
		}
	}
}

void turn_left() { P.d = (P.d + 1) % 4; }  // 주인공을 왼쪽으로 회전
void turn_right() { P.d = (P.d + 3) % 4; }  // 주인공을 오른쪽으로 회전
bool isValid(int r, int c) { return (0 <= r && r < N && 0 <= c && c < N); }  // 좌표가 지도를 벗어나지 않는지 확인

void move_front() {  // 주인공을 앞으로 한칸 전진 & 스위치 발견시 주변 9칸 밝힘
	int next_r = P.pos.first + dr[P.d];
	int next_c = P.pos.second + dc[P.d];
	if (isValid(next_r, next_c)) {
		P.pos.first = next_r;
		P.pos.second = next_c;
	}
	else return;
	if (M[next_r][next_c] == 'S') {
		for (int i = next_r - 1; i <= next_r + 1; i++) {
			for (int j = next_c - 1; j <= next_c + 1; j++) {
				if (isValid(i, j)) isOn[i][j] = true;
			}
		}
	}
}

void zombies_move() {  // 좀비를 한칸 전진 & 벽에 부딪히면 180도 회전
	for (int i = 0; i < Z.size(); i++) {
		if (P.pos == Z[i].pos) {  // 사람의 이동 후 좀비와 마주치는 경우
			if (isOn[P.pos.first][P.pos.second] == false) {
				isShocked = true;
				return;
			}
		}
		int next_r = Z[i].pos.first + dr[Z[i].d];
		int next_c = Z[i].pos.second + dc[Z[i].d];
		if (isValid(next_r, next_c)) {  // 길이 막혀있지 않으면 한칸 전진
			Z[i].pos.first = next_r;
			Z[i].pos.second = next_c;
			if (P.pos == Z[i].pos) {  // 좀비의 이동 후 사람과 마주치는 경우
				if (isOn[P.pos.first][P.pos.second] == false) {
					isShocked = true;
					return;
				}
			}
		}
		else {  // 길이 막혀 있으면 180도 회전
			Z[i].d = (Z[i].d + 2) % 4;
		}
	}
}

int main() {
	input();
	for (int i = 0; i < A.size(); i++) {
		char curr_movement = A[i];
		if (curr_movement == 'F') {
			move_front();
			zombies_move();
			if (isShocked) break;
		}
		else if (curr_movement == 'L') {
			turn_left();
			zombies_move();
		}
		else if (curr_movement == 'R') {
			turn_right();
			zombies_move();
		}
	}
	if (isShocked) cout << "Aaaaaah!";
	else cout << "Phew...";
}