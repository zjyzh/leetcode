from collections import defaultdict

class TireNode:
    def __init__(self, name):
        self.name = name
        self.is_file = False
        self.content = ""
        self.next = defaultdict(TireNode)




class FileSystem(object):

    def __init__(self):
        self.head = TireNode("")
        

    def findPath(self, filepath):
        current = self.head
        if filepath == '/':
            return current
        
        paths = filepath.strip('/').split('/')

        for p in paths:
            if p not in current.next:
                current.next[p] = TireNode(p)
            current = current.next[p]
        
        return current

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        cur = self.findPath(path)

        if cur.is_file:
            return [cur.name]
        
        res = [p for p in cur.next]
        res.sort()
        return res

        

                
        

    def splitpath(self, path):
        paths = path.strip("/").split("/")
        
        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        self.findPath(path)


   
        

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        cur = self.findPath(filePath)
        cur.is_file = True
        cur.content += content
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        cur = self.findPath(filePath)
        return cur.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)



