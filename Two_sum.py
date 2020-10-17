#Given an array and a number, we should return the indexes of arrray whose sum of two interges is equal to given number.


def Two_sum(List,target):
    dict={}
    for i in range(len(List)):
        x=List[i]
        if target-x in dict:
            return (dict[target-x],i)
        dict[x]=i
        
       
       
#Input :: List = [2,6,5,8,11], target = 14 :: Output = [1,3]
