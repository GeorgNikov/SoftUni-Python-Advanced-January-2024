jobs = [int(job) for job in input().split(", ")]
index = int(input())
# print sum of all elements [3, 1, 10, 1, 2] if element <= element of index 0 -> [3] -> sum(3, 1, 1, 2) -> return 7
print(sum([x for x in jobs if x <= jobs[index]]))