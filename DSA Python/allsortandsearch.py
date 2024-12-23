def simpleSort(nums: list[int]) -> list[int]:
    r=len(nums)
    for i in range(r-1):
        for j in range(i+1,r):
            if nums[j]<nums[i]:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
    return nums

def selectionSort(nums: list[int]) -> list[int]:
    r=len(nums)
    for i in range(r-1):
        u=i
        for j in range(i+1,r):
            if nums[j]<nums[u]:
                u=j
        if u != i:
            temp=nums[i]
            nums[i]=nums[u]
            nums[u]=temp
    return nums

def bubleSort(nums: list[int]) -> list[int]:
    r=len(nums)
    for i in range(len(nums)-1,-1,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
    return nums

def insertionSort(nums: list[int]) -> list[int]:
    r=len(nums)
    for i in range(r):
        for j in range(i,0,-1):
            if nums[j-1]>nums[j]:
                temp=nums[j]
                nums[j]=nums[j-1]
                nums[j-1]=temp
    return nums

def simpleSearch(nums,keys: list[int]) -> bool:
    r=len(nums)
    for i in range(r):
        if keys == nums[i]:
            return True
    return False

def binarySearch(nums,keys: list[int]) ->bool: 
    l,r=0,len(nums)
    while l<r:
       mid=(l+r)//2
       if nums[mid] == keys:
           return True
       elif nums[mid] < keys:
           l=mid + 1
       elif nums[mid] > keys:
           r=mid
    return False
def binarysearch(nums: list[int],key:int,low:int,high:int) ->int:
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return low


def binaryinsertionsort(nums: list[int]) -> list[int]:
    for i in range(1,len(nums)):
        keys=nums[i]
        j=binarysearch(nums[:i],keys,0,i-1)
        nums.insert(j,keys)
        nums.pop(i+1)
    return nums
         


def main():
    while True:
        print("Main menu:")
        print("Enter 1 for sorting!")
        print("Enter 2 for searching!")
        print("enter 3 to Exit the Main and leave!")
        Seandso=int(input("Your choice: "))
        if Seandso == 1:
            print("Sorting menu:")
            print("Enter 1 for simple sorting!")
            print("Enter 2 for buble sorting!")
            print("Enter 3 for selection sorting!")
            print("Enter 4 for insertion sorting!")
            print("Enter 5 for binary insertion sorting")
            so = int(input("Your choice: "))
            nums=list(map(int,input("Enter the list numbers you want to sort!").split()))
            if so == 1:
                result=simpleSort(nums)
                print(f"the sorted elements are: {result}")
            elif so == 2:
                result=bubleSort(nums)
                print(f"the sorted elements are: {result}")
            elif so == 3:
                result=selectionSort(nums)
                print(f"the sorted elements are: {result}")
            elif so == 4:
                result=insertionSort(nums)
                print(f"the sorted elements are: {result}")
            elif so == 5:
                result=binaryinsertionsort(nums)
                print(f"the sorted elements are: {result}")
            else:
                print("there is no solution for your choice!")

        elif Seandso == 2:
            print("Search menu:")
            print("Enter 1 for simple searching!")
            print("Enter 2 for binary searching!")
            se=int(input("Your choice: "))
            nums=list(map(int,input("Enter the list numbers you want to sort!").split()))
            keys=int(input("your target number find: "))
            if se == 1:
                result=simpleSearch(nums,keys)
                print(f"the sorted elements are: {result}")
            elif se == 2:
                result=binarySearch(nums,keys)
                print(f"the sorted elements are: {result}")
            else:
                print("you have choosed the incorrect!")
        
        elif Seandso == 3:
            print("terminate the Main! good bye!")
            break
        else:
            print("The choice you made was incorrect!")

        


if __name__ == "__main__":
    main()