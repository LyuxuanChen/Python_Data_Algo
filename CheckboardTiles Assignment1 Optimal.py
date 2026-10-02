row = int(input())
col = int(input())
s = int(input())
for i in range(row * s):
    line = ""
    for j in range(col * s):
        tile_row = i // s
        tile_col = j // s

        if (tile_row + tile_col) % 2 == 0:
            line += "#"
        else:
            line += "."

    print(line)

print(0%2)

    # row = int(input())
    # col = int(input())
    # s = int(input())
    #
    # total_row = row * s
    # total_col = col * s
    #
    # board = []
    #
    # for i in range(total_row):
    #     samplerow = []
    #
    #     for j in range(total_col):
    #         samplerow.append('')
    #
    #     board.append(samplerow)
    #
    # row_switch = 0
    # count = 0
    #
    # for i in range(total_row):
    #     switch = row_switch
    #
    #     for j in range(col):
    #         for z in range(s):
    #             if switch == 0:
    #                 board[i][j * s + z] = '#'
    #             else:
    #                 board[i][j * s + z] = '.'
    #
    #         if switch == 0:
    #             switch = 1
    #         else:
    #             switch = 0
    #
    #     count += 1
    #
    #     if count == s:
    #         count = 0
    #
    #         if row_switch == 0:
    #             row_switch = 1
    #         else:
    #             row_switch = 0
    #
    # for i in range(total_row):
    #     print("".join(board[i]))