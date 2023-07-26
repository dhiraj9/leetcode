class TimeMap:

    def __init__(self):
        self.a = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.a:
            self.a[key] = []
        self.a[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.a.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)