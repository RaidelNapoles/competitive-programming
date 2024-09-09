# UVa 272 ­ TEX Quotes
order = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    output = ""
    for char in line:
        if char == '"':
            if order % 2 == 0:
                output += "``"
            else:
                output += "''"
            order += 1
        else:
            output += char
    print(output)

# accepted!!
