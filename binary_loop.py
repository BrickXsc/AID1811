# 二分查找

def binary(value,key):
    left = 0
    right = len(value) - 1
    while True:
        middle = (left + right) // 2
        if value[middle] == key:
            return middle
        elif value[middle] < key:
            # 则在右侧继续查找
            left = middle + 1
        else:
            right = middle - 1
    return -1

if __name__ == "__main__":
    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    key = 9
    res = binary(value, key)
    if res == -1:
        print("Fail")
    else:
        print(res)
        
    































