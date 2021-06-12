import collections

dobuleEnded = collections.deque(["Mon","Tue","Wed"])

dobuleEnded.append('Thr')
dobuleEnded.appendleft('Sun')
print(list(dobuleEnded))

dobuleEnded.pop()
dobuleEnded.popleft()
print(list(dobuleEnded))