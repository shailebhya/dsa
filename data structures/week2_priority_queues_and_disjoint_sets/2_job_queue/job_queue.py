# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

# The Method 
# Here's the systematic strategy we'll apply for solving problems:
# 1. State the problem clearly. Identify the input & output formats.

# --> n indi. threads and m jobs. a thread can process only one job at a time. ouptut which job is in which thread and the time it starts the job
# --> input: "no. of threads(n)" "no. of jobs(m)"
#             "time taken by m jobs in sequence"
#               eg : 2 5
#                    1 5 2 5 2
#-->  output : "thread doing the job" "time the process starts"
#                               "
#                               "
#                               m times
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
#--> input:   2 5        
#             1 2 3 4 5   

#--> output:    0 0
#               1 0
#               0 1 
#               1 2
#               0 4

# 3. Come up with a correct solution for the problem. State it in plain English.

#  Used shiftDown from q1(changed to return heap instead of swaps and sort jobs on processing time,
#  (Created a named tuple for workers with thread and processing times as attributes).
#  List of workers passed to shift down
#  Steps 
# For every job, get  heap[0]
# upgrade job processing time
# insert at heap[0]
# shiftDown(heap,0)

# 1. Create array_worker with the size of n_workers and array_next_free_time with the size of n_workers.
#  You will use array_next_free_time to build the heap and array_worker to keep track of the worker_ID. (similar to the Union by Rank video)

# 2. For each job, get the first item of  array_next_free_time and array_n_worker and append to the result. 
# 3. Add the time taken by job to the first item of array_next_free_time. Sift it down using the siftdown() in the pseudo course video. 
# 4. Create the logic of assigning minIndex when:
# parent == left child, parent > left child
# left  == right child, left > right child 
# 5. swap i and minIndex

# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.




def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    print(next_free_time)
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        print(next_worker)
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

class JobQueue:
    def __init__(self, n_workers, jobs):
        self.n = n_workers
        self.jobs = jobs
        self.finTime = []
        self.assignedJobs = []
        for i in range(self.n):
            self.finTime.append([i, 0])

    def SiftDown(self, i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < self.n:
            if self.finTime[min_index][1] > self.finTime[left][1]:
                min_index = left
            elif self.finTime[min_index][1] == self.finTime[left][1]:
                if self.finTime[min_index][0] > self.finTime[left][0]:
                    min_index = left
        if right < self.n:
            if self.finTime[min_index][1] > self.finTime[right][1]:
                min_index = right
            elif self.finTime[min_index][1] == self.finTime[right][1]:
                if self.finTime[min_index][0] > self.finTime[right][0]:
                    min_index = right
        if min_index != i:
            self.finTime[i], self.finTime[min_index] = self.finTime[min_index], self.finTime[i]
            self.SiftDown(min_index)

    def NextWorker(self, job):
        root = self.finTime[0]
        next_worker = root[0]
        started_at = root[1]
        self.assignedJobs.append(AssignedJob(next_worker,started_at))
        self.finTime[0][1] += job
        self.SiftDown(0)


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    job_queue = JobQueue(n_workers, jobs)
    for job in jobs:
        job_queue.NextWorker(job)
    assignedJobs = job_queue.assignedJobs

    for job in assignedJobs:
        print(job.worker, job.started_at)

if __name__ == "__main__":
    main()
