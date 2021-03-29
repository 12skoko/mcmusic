octave = {0: [0, 0, 0],
          1: [1, 1, -3],
          2: [2, 0, 0],
          3: [3, 1, -3],
          4: [4, 0, 0],
          5: [5, 0, 0],
          6: [6, 1, -3],
          7: [7, 0, 0],
          8: [6, 1, -3],
          9: [9, 0, 0],
          10: [10, 1, -3],
          11: [11, 0, 0]
          }


def correct(num):
    if num >= 24 and num <= 107:
        t = num - 24
        i = int(t / 12)
        j = t % 12

        ccr = [3 + 12 * i, 0, 0]

        for k in range(3):
            ccr[k] += octave[j][k]

        return ccr

    elif num == 108:
        return [87, 0, 0]

    elif num == 21:
        return [0, 0, 0]

    elif num == 22:
        return [1, 1, 3]

    elif num == 23:
        return [2, 0, 0]
    else:
        return [0, 0, 0]


def calendcoor(basecoor,num):
    correctcoor=correct(num)
    endcoor=basecoor
    for i in range(0,3):
        endcoor[i]+=correctcoor[i]
    return endcoor
