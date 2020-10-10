from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on job.end
        return self.end < other.end


from heapq import *


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)
    min_heap = []
    max_load = 0
    for job in jobs:
        while min_heap and job.start >= min_heap[0].end:
            heappop(min_heap)
        heappush(min_heap, job)
        max_load = max(max_load, sum([j.cpu_load for j in min_heap]))
    return max_load


def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
