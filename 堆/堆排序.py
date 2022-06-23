

def max_heapify(nums, root, heap_len):
    """
    root与左右孩子的最大值交换，交换后继续判断交换位置后的root。
    """
    p = root
    while p < heap_len:
        l = p * 2 + 1
        r = p * 2 + 2
        if l >= heap_len:
            break
        nex = l
        if r < heap_len and nums[r] > nums[l]:
            nex = r
        if nums[p] < nums[nex]:
            nums[p], nums[nex] = nums[nex], nums[p]
            p = nex
        else:
            break


def build_heap(nums):
    """
    从后往前遍历元素，使得每个元素作为root时，满足堆定义。
    当第一个元素作为root也满足堆定义后，堆构造完成。
    """
    for i in range(len(nums)-1, -1, -1):
        max_heapify(nums, i, len(nums))


def heap_sort(nums: list) -> list:
    """
    构建大顶堆，然后每次将堆顶元素与数组最后一个元素交换位置，堆长度减1，重新构建大顶堆。
    """
    build_heap(nums)
    last = len(nums)-1
    for _ in range(len(nums)-1):
        nums[0], nums[last] = nums[last], nums[0]
        last -= 1
        max_heapify(nums, 0, last+1)
    return nums