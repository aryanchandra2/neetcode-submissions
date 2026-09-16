class TrieNode:
    
    def __init__(self):
        # dir : TrieNode
        self.children = {}

        # filename : content
        self.files = {}

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(list(self.root.children.keys()) + list(self.root.files.keys()))

        cur = self.root
        pathList = path.split("/")[1:]
        
        for p in pathList[:-1]:
            if p not in cur.children:
                return []
            cur = cur.children[p]

        if pathList[-1] in cur.files:
            return [pathList[-1]]
        if pathList[-1] in cur.children:
            cur = cur.children[pathList[-1]]
            return sorted(list(cur.children.keys()) + list(cur.files.keys())) 

        return []

    def mkdir(self, path: str) -> None:
        cur = self.root
        pathList = path.split("/")[1:]

        for p in pathList:
            if p not in cur.children:
                cur.children[p] = TrieNode()
            cur = cur.children[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        pathList = filePath.split("/")[1:]
        
        for p in pathList[:-1]:
            if p not in cur.children:
                return []
            cur = cur.children[p]

        if pathList[-1] in cur.files:
            cur.files[pathList[-1]] += content
        else:
            cur.files[pathList[-1]] = content


    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        pathList = filePath.split("/")[1:]
        
        for p in pathList[:-1]:
            if p not in cur.children:
                return ""
            cur = cur.children[p]

        if pathList[-1] in cur.files:
            return cur.files[pathList[-1]]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
