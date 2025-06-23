#!/usr/bin/env python

# construct the neighbor bitmask for each position
uint64max = (1 << 64) - 1
lmask = (1 << 63 - 9) | (1 << 63 - 1) | (1 << 63 + 7)
rmask = lmask << 2
mask = lmask | rmask | (1 << 63 - 8) | (1 << 63 + 8)
neighbors = []
for i in range(0x40):
    neighbors.append(
        uint64max
        # account for not wrapping the edges
        & (~rmask if i     % 8 == 0 else mask)
        & (~lmask if (i+1) % 8 == 0 else mask)
    )
    mask >>= 1
    lmask >>= 1
    rmask >>= 1

def print_frame(state:int):
    print(f'state: {state:016x}')
    for i in range(0x40):
        print('#' if state & 1 else ' ', end='' if (i+1) % 8 else '\n')
        state >>= 1

def next_frame(state:int) -> int:
    next = 0
    pointer = 1 << 63
    for n in neighbors:
        count = (state & n).bit_count()
        if count == 3:
            next |= pointer
        elif count == 2:
            next |= state & pointer
        pointer >>= 1
    return next

if __name__ == '__main__':
    import sys
    import time
    import random
    # accept an initial state as hex code or generate a random initial state.
    if len(sys.argv) > 1:
        frame = int(sys.argv[-1], 16)
    else:
        frame = random.randint(0, uint64max)
        frame = neighbors[64-19]

    try:
        while frame:
            print(chr(27) + '[2J') # clear screen
            print_frame(frame)
            next = next_frame(frame)
            if frame == next:
                # we've reached a static state, exit
                break
            frame = next
            time.sleep(0.5)
        print_frame(frame)
    except KeyboardInterrupt:
        pass

