import textwrap


def wrap(string, max_width):
    wrap_l = []
    # return textwrap.fill(string, max_width)
# without wraping lib
    for i in range(0, len(string), max_width):
        wrap_l.append(string[i:max_width+i])
    return '\n'.join(wrap_l)


if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4
    result = wrap(string, max_width)
    print(result)
