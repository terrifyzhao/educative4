from heapq import *


def schedule_tasks(tasks, k):
    count = 0
    dic = {}
    for task in tasks:
        dic[task] = dic.get(task, 0) + 1

    max_heap = []
    for task, fre in dic.items():
        heappush(max_heap, (-fre, task))

    while max_heap:
        wait_List = []
        n = k + 1
        while max_heap and n:
            fre, task = heappop(max_heap)
            count += 1
            if -fre > 1:
                wait_List.append((fre + 1, task))
            n -= 1

        for f, t in wait_List:
            heappush(max_heap, (f, t))

        # 下一轮有值才需要添加idle
        if max_heap:
            count += n
    return count


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
