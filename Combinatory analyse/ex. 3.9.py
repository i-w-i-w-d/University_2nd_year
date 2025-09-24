def gray_code(n):
    if n == 0:
        return ['']
    previous = gray_code(n - 1)
    result = []

    for code in previous:
        result.append('0' + code)

    for code in reversed(previous):
        result.append('1' + code)

    return result

n = 5

codes = gray_code(n)

print("Результати:")

for code in codes:
    print(code)