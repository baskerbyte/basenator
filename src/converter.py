alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rests = []
quotients = []


def convert_to_decimal(num, num_base):
    result = 0

    for i in range(len(num)):
        item = int(num[i])
        result += (num_base ** i) * item

    return result


def convert_to_base(num, to_base):
    while num > 0:
        quotients.append(num // to_base)
        rests.append(num % to_base)

        num = quotients[-1]

    rests.reverse()

    return int(''.join(map(str, rests)))


def convert_to_num(num, num_base):
    parsed = []
    result = 0

    for i in range(len(num)):
        if num[i].isalpha():
            parsed.append(10 + alphabet.find(num[i]))
        else:
            parsed.append(int(num[i]))

        result += (num_base ** i) * parsed[i]

    return result


def extract_num(num, num_base, to_base):
    if num.isnumeric():
        if num_base == 10:
            return convert_to_base(int(num), to_base)
        else:
            decimal = convert_to_decimal(num[::-1], num_base)

            return convert_to_base(decimal, to_base)
    else:
        decimal = convert_to_num(num[::-1], num_base)

        return convert_to_base(decimal, to_base)


def convert_symbols():
    for i in range(len(rests)):
        if rests[i] > 9:
            digits = [int(i) for i in str(rests[i])]
            symbol_position = rests[i] - 10

            if symbol_position >= 10:
                if symbol_position <= 26:
                    rests[i] = alphabet[symbol_position]
                else:
                    rests[i] = str(digits[0]) + alphabet[digits[1]]
            else:
                rests[i] = alphabet[digits[1]]
