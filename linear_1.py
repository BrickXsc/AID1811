# values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# key = 9

# left = values[0]
# riget = values[len(values) - 1]
# middle = (left + right) // 2
def binary(value, key, left, right):
    # 第一个想到的,退出条件
    if left > right:
        # 查找失败,返回-1
        return -1
    # 获取中间元素对应下标值
    middle = (left + right) // 2
    # 对比中间元素值与指定查找值
    if value[middle] == key:
        return middle
    elif value[middle] > key:
        # 左侧

        return binary(value, key, left, middle-1)
    else:
        # 右侧
        return binary(value, key, middle+1, right)
    
if __name__ == "__main__":

    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    key = 9

    # 二分查找
    res = binary(value, key, 0, len(value)-1)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功,对应下标值:", res)
















