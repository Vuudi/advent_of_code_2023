digitDict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


if __name__ == '__main__':
    sum = 0
    for line in example.splitlines():
        calibrationValue = ''
        digits = []
        for i in range(0, len(line)):
            if len(line) - i >= 5:
                if line[i:i + 3] in digitDict:
                    digits.append(digitDict[line[i:i + 3]])
                    continue
                if line[i:i + 4] in digitDict:
                    digits.append(digitDict[line[i:i + 4]])
                    continue
                if line[i:i + 5] in digitDict:
                    digits.append(digitDict[line[i:i + 5]])
                    continue
            if len(line) - i >= 4:
                if line[i:i + 3] in digitDict:
                    digits.append(digitDict[line[i:i + 3]])
                    continue
                if line[i:i + 4] in digitDict:
                    digits.append(digitDict[line[i:i + 4]])
                    continue
            if len(line) - i >= 3:
                if line[i:i + 3] in digitDict:
                    digits.append(digitDict[line[i:i + 3]])
                    continue
            if line[i].isdigit():
                digits.append(line[i])
        sum += int(digits[0] + digits[-1])

    print(sum)
