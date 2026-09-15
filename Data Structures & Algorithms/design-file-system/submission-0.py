class FileSystem:

    def __init__(self):
        self.storage = {}



    def createPath(self, path: str, value: int) -> bool:
        if path in self.storage:
            return False
        splitList = path.split("/")
        parent = ""
        for i in range(1, len(splitList) - 1):
            parent += "/" + splitList[i]
            if parent not in self.storage:
                return False
        self.storage[path] = value

        return True
        


    def get(self, path: str) -> int:
        return self.storage.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
