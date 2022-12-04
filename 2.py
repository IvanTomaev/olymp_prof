def gb_to_bit(gb):
    return gb * 8 * 1024 * 1024 * 1024


def bit_to_gb(gb):
    return int(gb / 8 / 1024 / 1024 / 1024)


def bit_to_mb(gb):
    return int(gb / 8 / 1024 / 1024)


def bit_to_kb(gb):
    return int(gb / 8 / 1024)


block_size = 4096 * 8
pointer_size = 32

f_size_12s = block_size * 12

print('in 12s, kb: ', bit_to_kb(f_size_12s))

read_b_12s = 1 + 12
print('read ', read_b_12s)

pt_in_13th = int(block_size/pointer_size)

f_size_13th = block_size * pt_in_13th
print('in 13th, mb: ', bit_to_mb(f_size_13th))

read_b_13th = 1 + 12 + 1 + pt_in_13th
print('read ', read_b_13th)

f_size_14th = f_size_13th * pt_in_13th
print('in 14th, gb: ', bit_to_gb(f_size_14th))

read_b_14th = 1 + 12 + 1 + pt_in_13th * pt_in_13th
print('read ', read_b_14th)

f_size_15th = f_size_13th * pt_in_13th * pt_in_13th
print('in 15th, gb: ', bit_to_gb(f_size_15th))

read_b_15th = 1 + 12 + 1 + pt_in_13th * pt_in_13th * pt_in_13th
print('read ', read_b_15th)

diff = read_b_15th - 16 * read_b_14th

print('diff: ', diff)
