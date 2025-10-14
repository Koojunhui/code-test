def solution(dartResult):
    # squareType = ["S", "D", "T"]
    # option = ["*", "#"]
    split_str = get_split_str(dartResult)
    calculateList = get_calculateList(split_str)

    return sum(calculateList)

def get_split_str(dartResult):
    split_str = []
    part = ""
    for token in dartResult:
        if token.isdigit():
            if part and part != "1":
                split_str.append(part)
                part = token
            else:
                part += token
        else:
            part += token
    split_str.append(part)

    return split_str

def get_calculateList(split_str):
    calculateList = []
    for str in split_str:
        num = 0
        for token in str:
            if token.isdigit():
                if num == 1 and token == "0":
                    num = 10
                else:
                    num = int(token)
            elif token == "S":
                num **= 1
                calculateList.append(num)
            elif token == "D":
                num **= 2
                calculateList.append(num)
            elif token == "T":
                num **= 3
                calculateList.append(num)
            elif token == "*":
                if len(calculateList) == 1:
                    calculateList[0] *= 2
                elif len(calculateList) > 1:
                    calculateList[-1] *= 2
                    calculateList[-2] *= 2
            elif token == "#":
                calculateList[-1] *= -1

    return calculateList