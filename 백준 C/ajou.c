#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 8

int board[N][N];
int blocked[4][2];  // 퀸이 위치할 수 없는 랜덤한 4개의 자리

void setBoard();
void printBoard();
void setBlockedPositions();
int isBlocked(int row, int col);
int isSafe(int row, int col);
int solveNQueens(int row);

int main(void) {
    srand(time(NULL));  // 랜덤 넘버 생성기 초기화

    setBoard();  // N x N 체스판, 0으로 초기화 (빈칸)
    setBlockedPositions();  // 랜덤한 4개의 blocked 자리 설정

    if (solveNQueens(0)) {
        printBoard();  // 성공하면 퀸의 배치를 출력
    }
    else {
        printf("Solution does not exist\n");
    }

    return 0;
}

// 체스판을 0으로 초기화
void setBoard() {
    // 과제1. 구현(1) setBoard 함수 구현하기
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            board[i][j] = 0;
        }
    }
}

// 랜덤한 4개의 자리를 blocked 위치로 설정
void setBlockedPositions() {
    // 과제1. 구현(2) printBoard 함수 구현하기
    int left = 4; // 4개 만큼 배치할 거니까
    while (left)
    {
        int randRow = rand() % N; // 0~N-1
        int randCol = rand() % N; // 0~N-1
        if (board[randRow][randCol] == -1) continue; // 이미 -1인 경우 (blocked 에 포함되있는 경우 건너뛰기)

        left -= 1; // 채울 곳 한 곳을 찾았으므로 -1

        // 블럭 변경 및 blocked에 원소 넣기
        board[randRow][randCol] = -1;
        blocked[left][0] = randRow;
        blocked[left][1] = randCol;
    }
}

// 체스판 출력 함수
void printBoard() {
    // 과제1. 구현(3) printBoard 함수 구현하기
    printf("Blocked positions:\n");
    for (int i = 0; i < 4; i++)
    {
        printf("(%d, %d)\n", blocked[i][0], blocked[i][1]);
    }
    printf("\n"); // 개행
    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
        {
            if (board[row][col] == 0) printf(". ");
            else if (board[row][col] == -1) printf("X ");
            else print("Q ");
        }
        printf("\n");
    }
}

// 해당 자리가 blocked 위치인지 확인
int isBlocked(int row, int col) {
    // 과제1. 구현(4) isBlocked 함수 구현하기
    // board랑 확인해서 -1이면 blocked 위치면 1 아니면 0 반환
    return board[row][col] == -1;
}

// 현재 위치에 퀸을 놓을 수 있는지 확인
int isSafe(int row, int col) {
    // 과제1. 구현(5) isSafe 함수 구현하기
    // 방향 정하기 col+dcol[i]*반복횟수, row+drow[i]*반복횟수 꼴로 표현할 수 있고,dist를 증가시키면 해당 방향으로 증가하는 효과
    // 예를 들어 i가 0인 경우 dcol[0], drow[0] 은 1,1로 ↘ 방향으로 진행함과 동일함
    int dcol[6] = { 1,1,-1,-1,0,0 };
    int drow[6] = { 1,-1,-1,1,1,-1 };

    for (int i = 0; i < 6; i++) // 6방향 왼위, 위, 오른위, 오른아래, 아래, 왼아래 탐색 (방향만 말한거 순서와는 상관없음)
    {
        int nrow = row;
        int ncol = col;
        while (-1 < nrow && nrow < N && -1 < ncol && ncol < N)
        {
            if (board[nrow][ncol] == 1) return 0; // 다음 위치에 퀸이 있으면 return 0
            nrow += drow[i];
            ncol += dcol[i];
        }
    }
    // 모두 탐색했을 때 없다면
    return 1;
}

// 퀸을 체스판에 배치하는 재귀 함수
int solveNQueens(int row) {
    // 과제1. 구현(6) solveNQueens 함수 구현하기
    if (row == N) return 1; // 마지막 열까지 탐색을 마쳤다면 반환
    for (int col = 0; col < N; col++)
    {
        if (!isBlocked(row, col) && isSafe(row, col))
        {
            board[row][col] = 1;
            return solveNQueens(row + 1);
        }
    }
    return 0;
}