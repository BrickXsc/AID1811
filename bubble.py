def bubble(value):
    # 外部循环，走访数据次数
    for i in range(len(value) - 1):
    # 内部循环，相邻数据对比次数
        for j in range(len(value) - i -1):
            if value[j] > value[j + 1]:
                value[j], value[j + 1] = value[j + 1], value[j]
            

if __name__ == "__main__":
    value = [100,190,165,170,155,108,139,175,160,188]
    print(value)
    bubble(value)
    print(value)