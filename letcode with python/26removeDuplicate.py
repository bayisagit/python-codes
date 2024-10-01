def bayo(nums):
    k=1
    app=[]
    app.append(nums[0])
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            app.append(nums[k])
            k+=1
    return app
nums = [0,0,1,1,1,2,2,3,3,4]
res=bayo(nums)
print(res)