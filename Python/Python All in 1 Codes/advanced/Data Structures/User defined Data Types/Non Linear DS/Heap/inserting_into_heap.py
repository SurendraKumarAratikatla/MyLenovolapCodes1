import heapq

h = [21,1,45,78,3,5]

# Covert to a heap
heapq.heapify(h)
print(h)

# Add element
heapq.heappush(h,8)
print(h)
