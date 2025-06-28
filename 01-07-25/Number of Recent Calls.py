class RecentCounter(object):

    def __init__(self):
        self.recent_calls = deque()

    def ping(self, t):
        self.recent_calls.append(t)
        threshold = t-3000
        while self.recent_calls[0] < threshold:
            self.recent_calls.popleft()
        return len(self.recent_calls)
