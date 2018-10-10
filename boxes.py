def box(size, number):
    if size < 3 or number < 1:
        print("Size must be 3 or higher and number must be at least 1")
    else:
        print('+' + number * ((size - 2) * '-' + '+'))
        for i in range(number):
            if size % 2 == 0:
                level = 0
                while level <= (size // 2) - 2:
                    print(
                        '|' + (level * ' ' + ('\\' + ' ' * (size - 4 - 2 * level) + '/') + level * ' ' + '|') * number)
                    level += 1
                level = (size // 2) - 2
                while level >= 0:
                    print(
                        '|' + (level * ' ' + ('/' + ' ' * (size - 4 - 2 * level) + '\\') + level * ' ' + '|') * number)
                    level -= 1
                print('+' + number * ((size - 2) * '-' + '+'))
            elif size % 2 != 0:
                level = 0
                while level <= (size // 2) - 2:
                    print(
                        '|' + (level * ' ' + ('\\' + ' ' * (size - 4 - 2 * level) + '/') + level * ' ' + '|') * number)
                    level += 1
                print((('|' + (size // 2 - 1) * ' ' + 'X' + (size // 2 - 1) * ' ') * number) + '|')
                level = (size // 2) - 2
                while level >= 0:
                    print(
                        '|' + (level * ' ' + ('/' + ' ' * (size - 4 - 2 * level) + '\\') + level * ' ' + '|') * number)
                    level -= 1
                print('+' + number * ((size - 2) * '-' + '+'))