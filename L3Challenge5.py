# log = {} #dictionary to store name and index
# n = int(input())
# len = 0
# maxlen = 0
# beststart = 1
# startpos = 1
#
# for i in range (1, n+1):
#     name = input()
#     if name in log and log[name]>startpos:
#         startpos = log[name]+1
#         log[name] = i
#
#     log[name] = i
#     len = i+1-startpos
#
#     if len>maxlen:
#         maxlen = len
#         beststart = startpos
#
# print(beststart)
# print(len)

n = int(input())

maxlen = 0
beststart = 1
nms = []
log = set()
for i in range(n):
    nms.append(str(input()))

for left in range (n):
    log = set()
    curlen = 0
    for right in range(left,n):
        if nms[right] in log:
            break
        log.add(nms[right])
        curlen+=1


    if curlen>maxlen:
        maxlen = curlen
        beststart = left+1



print(beststart)
print(maxlen)
