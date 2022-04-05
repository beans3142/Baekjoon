KING = 1
ROOK = 2
ETC = 3


def find_king_and_rook(inputs):
    pos = {}
    for y in range(8):
        for x in range(8):
            base = inputs[y][x]
            if base == KING:
                pos["king"] = (x, y)
            elif base == ROOK:
                if "look" in pos.keys():
                    pos["look2"] = (x, y)
                else:
                    pos["look"] = (x, y)
    return pos


def gameover_check(inputs, king, look):
    kx, ky = king
    rx, ry = look
    # check col
    sx, ex = (kx, rx) if kx < rx else (rx, kx)
    candidate = inputs[ky][sx : ex + 1]
    if rx < kx:
        candidate.reverse()

    for y in candidate:
        if y == ROOK:
            return 1
        if y == ETC:
            break

    # # check raw
    sy, ey = (ky, ry) if ky < ry else (ry, ky)
    if inputs[sy][kx] == ROOK:
        sy += 1
    if ky<ry:
        
    for i in range(sy, ey + 1):
        if inputs[i][kx] == ROOK:
            return 1
        if inputs[i][kx] == ETC:
            break
    return 0


def sol(inputs):
    pos = find_king_and_rook(inputs)

    if "look" not in pos.keys():
        return 0

    king = pos["king"]

    result = gameover_check(inputs, king, pos["look"])

    if result == 1:
        return 1

    if "look2" in pos.keys():
        result = gameover_check(inputs, king, pos["look2"])

    return result


if __name__ == "__main__":
    inputs = [list(map(int, input().split())) for _ in range(8)]
    print(sol(inputs))
