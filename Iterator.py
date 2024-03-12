
class DatasetIter:
    def __init__(self, path:str):
        self.file = open(path, 'r')
        
    def __del__(self):
        self.file.close()
        
    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        return line


dataset = "train1.json"      

index = 0
for data in DatasetIter(dataset):
    index += 1

print(index)
