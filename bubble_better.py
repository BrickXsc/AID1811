def bubble(value):
    for i in range(len(Value) - 1):
        flag = False
        for j in range(len(value) - i - 1):
            if value[j] < value[j + 1]:
                value[j], valeu[j + 1] = value[j + 1], value[j]
                flag = True
        if flag is False:
            break

valer = [200, 100, 108, 139, 155, 160, 165, 170, 175, 188, 190]
