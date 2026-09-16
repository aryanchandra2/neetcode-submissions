class TrieNode:

    def __init__(self):
        # dir name : TrieNode()
        self.subDirectories = {}
        # file name : content
        self.files = {}


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        cur = self.root
        if path == "/":
            return sorted(list(cur.subDirectories.keys()) + list(cur.files.keys()))
        pathList = path.split("/")[1:]

        for p in pathList[:-1]:
            cur = cur.subDirectories[p]
        
        lastP = pathList[-1]
        if lastP in cur.subDirectories:
            cur = cur.subDirectories[lastP]
            return sorted(list(cur.subDirectories.keys()) + list(cur.files.keys()))
        if lastP in cur.files:
            return [lastP]
        
        return []

    def mkdir(self, path: str) -> None:
        cur = self.root
        pathList = path.split("/")[1:]

        for p in pathList:
            if p not in cur.subDirectories:
                cur.subDirectories[p] = TrieNode()
            cur = cur.subDirectories[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        pathList = filePath.split("/")[1:]

        for p in pathList[:-1]:
            cur = cur.subDirectories[p]
        
        lastP = pathList[-1]
        if lastP not in cur.files:
            cur.files[lastP] = content
        else:
            cur.files[lastP] += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        pathList = filePath.split("/")[1:]

        for p in pathList[:-1]:
            cur = cur.subDirectories[p]
        
        return cur.files[pathList[-1]]



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
