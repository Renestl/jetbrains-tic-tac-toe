text = input()
uppers = text.title().split()
first = uppers[0].lower()

print(first + "".join(uppers[1:]))
