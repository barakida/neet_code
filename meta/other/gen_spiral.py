def get_next_position(iy: int, ix: int, direction: str) -> tuple[int, int]:
    if direction == 'left':
        iy_next, ix_next = iy, ix + 1
    elif direction == 'down':
        iy_next, ix_next = iy + 1, ix
    elif direction == 'right':
        iy_next, ix_next = iy, ix - 1
    elif direction == 'up':
        iy_next, ix_next = iy - 1, ix
    else:
        assert False, f"direction {direction} not supported"

    return iy_next, ix_next


def gen_spiral(n: int) -> list[list[str]]:

    spiral = [[0] * n for _ in range(n)]

    directions = ["left", "down", "right", "up"]
    direction_idx = 0

    iy, ix = 0, 0
    for v in range(1, n * n + 1):

        # enter value
        spiral[iy][ix] = v

        # prep next position
        iy_next, ix_next = get_next_position(iy, ix, directions[direction_idx])
        if (iy_next < 0 or iy_next >= n or
            ix_next < 0 or ix_next >= n or
            spiral[iy_next][ix_next] != 0):
            direction_idx = (direction_idx + 1) % len(directions)
            iy_next, ix_next = get_next_position(iy, ix, directions[direction_idx])
        iy, ix = iy_next, ix_next

    return spiral


def main():
    import numpy as np
    print((np.array(gen_spiral(2))))
    print()
    print((np.array(gen_spiral(3))))
    print()
    print((np.array(gen_spiral(4))))
    print()
    print((np.array(gen_spiral(5))))
    print()


if __name__ == '__main__':
    main()
