import re

def get_binary_string(n):
    binary = bin(n)
    binary_string = binary[2:]

    return binary_string

def get_decimal(binary_string):
    decimal = int(binary_string, 2)

    return decimal

def binary_to_symbol(binary_string):
    symbol_string = re.sub(r'[0]', ' ', binary_string)
    symbol_string = re.sub(r'[1]', '#', symbol_string)

    return symbol_string

# print(get_binary_string(31))
# print(get_decimal("1011"))

binary_string = get_binary_string(9)
symbol_string = binary_to_symbol(binary_string)
replace_string = binary_string.replace("1", "#").replace("0", " ")
print(symbol_string)
print(replace_string)

print(int("1010", 2)) # 2진수 문자열 -> 10진수 변환