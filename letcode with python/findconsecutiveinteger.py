class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.n=0
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.n+=1
        else:
            self.n=0
        return self.n >= self.k
value=int(input("inter the value: "))
k=int(input("enter the least elements: "))
mn=datastream=DataStream(value,k)
mn=datastream.consec(4)
print(mn)
mn=datastream.consec(4)
print(mn)
mn=datastream.consec(4)
print(mn)
mn=datastream.consec(3)
print(mn)
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)