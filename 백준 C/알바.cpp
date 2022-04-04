#include <stdio.h>
#include <stdlib.h>

int main() {

    int num;
    scanf("%d", &num);

    int info[num][3];
    for (int i = 0; i < num; i++) {
        for (int j = 0; j < 3; j++) {
            scanf("%d", &info[i][j]);
        }
    }

    int result = 0;

    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= 9; j++) {
            for (int k = 1; k <= 9; k++) {

                int pass = 0;

                for (int l = 0; l < num; l++) {
                    int expect = info[l][0];
                    int strike = info[l][1];
                    int ball = info[l][2];

                    int _strike = 0, _ball = 0;

                    // compare
                    int hundred = expect / 100;
                    int ten = (expect % 100) / 10;
                    int one = expect % 10;

                    if (hundred == i) {
                        _strike++;
                    }

                    if (ten == j) {
                        _strike++;
                    }

                    if (one == k) {
                        _strike++;
                    }

                    if (hundred == j) {
                        _ball++;
                    }

                    if (hundred == k) {
                        _ball++;
                    }

                    if (ten == i) {
                        _ball++;
                    }

                    if (ten == k) {
                        _ball++;
                    }

                    if (one == i) {
                        _ball++;
                    }

                    if (one == j) {
                        _ball++;
                    }


                    if (strike == _strike && ball == _ball) {
                        pass++;
                    }
                    else {
                        break;
                    }
                }

                if (pass == num) {
                    result++;
                }
            }
        }
    }

    printf("%d", result);

    return 0;
}