#include <iostream>
#include <vector>

using namespace std;

struct Object {  // ����, ����ġ, ���ΰ��� ������ �����ϱ� ���� ����ü ����
	int d = 0;  // ���� �ٷκ��� �ִ� ����(row, column)
	pair<int, int> pos = make_pair(0, 0);  // ���� ��ġ�� �ִ� ��ǥ
};

int N;  // ������ ���� �� ���� ����
string A;  // ���ΰ��� �ൿ �Է�
bool isOn[15][15];
vector<string> M;  // ���� ���� �迭
vector<struct Object> Z;  // ���� ���� �迭
Object P;  // ���ΰ� ��ü
bool isShocked;  // ���ΰ��� �����ߴ��� Ȯ���ϱ� ���� ����

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

void turn_left() { P.d = (P.d + 1) % 4; }  // ���ΰ��� �������� ȸ��
void turn_right() { P.d = (P.d + 3) % 4; }  // ���ΰ��� ���������� ȸ��
bool isValid(int r, int c) { return (0 <= r && r < N && 0 <= c && c < N); }  // ��ǥ�� ������ ����� �ʴ��� Ȯ��

void move_front() {  // ���ΰ��� ������ ��ĭ ���� & ����ġ �߽߰� �ֺ� 9ĭ ����
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

void zombies_move() {  // ���� ��ĭ ���� & ���� �ε����� 180�� ȸ��
	for (int i = 0; i < Z.size(); i++) {
		if (P.pos == Z[i].pos) {  // ����� �̵� �� ����� ����ġ�� ���
			if (isOn[P.pos.first][P.pos.second] == false) {
				isShocked = true;
				return;
			}
		}
		int next_r = Z[i].pos.first + dr[Z[i].d];
		int next_c = Z[i].pos.second + dc[Z[i].d];
		if (isValid(next_r, next_c)) {  // ���� �������� ������ ��ĭ ����
			Z[i].pos.first = next_r;
			Z[i].pos.second = next_c;
			if (P.pos == Z[i].pos) {  // ������ �̵� �� ����� ����ġ�� ���
				if (isOn[P.pos.first][P.pos.second] == false) {
					isShocked = true;
					return;
				}
			}
		}
		else {  // ���� ���� ������ 180�� ȸ��
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