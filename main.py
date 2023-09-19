num = input("Digite um número: ").upper()
numBase = int(input("Digite a base do número: "))
toBase = int(input("Basear para: "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rests = []
quotients = []


def convert_to_decimal(numb):
    sum = 0

    for i in range(len(numb)):
        item = int(numb[i])
        sum += (numBase ** i) * item

    return sum


def convert_to_base(numb, base):
    while numb > 0:
        quotients.append(numb // base)
        rests.append(numb % base)

        numb = quotients[-1]

    rests.reverse()

    return int(''.join(map(str, rests)))


def convert_to_num(numb):
    nums = []
    sum = 0

    for i in range(len(numb)):
        if numb[i].isalpha():
            nums.append(10 + alphabet.find(numb[i]))
        else:
            nums.append(int(numb[i]))

        sum += (numBase ** i) * nums[i]

    return sum


def extract_num():
    if num.isnumeric():
        if numBase == 10:
            return convert_to_base(int(num), toBase)
        else:
            decimal = convert_to_decimal(num[::-1])

            return convert_to_base(decimal, toBase)
    else:
        decimal = convert_to_num(num[::-1])

        return convert_to_base(decimal, toBase)


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


result = extract_num()

if toBase > 10:
    convert_symbols()

    result = ''.join(map(str, rests))

print(result)
