class TrieNode:
    def __init__(self):
        self.value = -1
        self.storage = {}

class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        cur = self.root
        parts = path.split("/")[1:]

        if path == "" or path == "/":
            return False

        for i, part in enumerate(parts):
            
            if part not in cur.storage:
                if i != len(parts) - 1:
                    return False

                cur.storage[part] = TrieNode()
                cur.storage[part].value = value
                return True
            cur = cur.storage[part]

        return False



    def get(self, path: str) -> int:
        parts = path.split("/")[1:]
        cur = self.root
        for i, part in enumerate(parts):
            if part not in cur.storage:
                return -1
            cur = cur.storage[part]
        return cur.value



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
