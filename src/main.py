from converter import extract_num, convert_symbols, rests

num = input("Digite um número: ").upper()
numBase = int(input("Digite a base do número: "))
toBase = int(input("Basear para: "))

result = extract_num(num, numBase, toBase)

if toBase > 10:
    convert_symbols()

    result = ''.join(map(str, rests))

print(result)
