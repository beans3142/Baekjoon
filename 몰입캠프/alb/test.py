KING = 1
LOOK = 2
ETC = 3


def find_king_and_look(inputs):
    pos = {}
    for y in range(8):
        for x in range(8):
            base = inputs[y][x]
            if base == KING:
                pos["king"] = (x, y)
            elif base == LOOK:
                pos["look"] = (x, y)
    return pos["king"], pos["look"]


def sol(inputs):
    king, look = find_king_and_look(inputs)

    kx, ky = king
    lx, ly = look

    # check col
    if kx < lx:
        sx, ex = (kx, lx)
        for y in inputs[ky][sx : ex + 1]:
            if y == ETC:
                break
            if y == LOOK:
                return 1
    else:
        sx,ex=(lx,kx)
        for y in inputs[ky][sx : ex + 1][::-1]:
            if y == ETC:
                break
            if y == LOOK:
                return 1

    # # check raw
    sy, ey = (ky, ly) if ky < ly else (ly, ky)
    for i in range(sy, ey + 1):
        if inputs[i][kx] == ETC:
            break
        if inputs[i][kx] == LOOK:
            return 1

    return 0


if __name__ == "__main__":
    inputs = [list(map(int, input().split())) for _ in range(8)]
    print(sol(inputs))
