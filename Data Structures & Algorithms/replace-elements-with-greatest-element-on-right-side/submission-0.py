class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_from_right = -1

        for i in range(n - 1, -1, -1):
            temp = arr[i] #current element 
            arr[i] = max_from_right
            max_from_right = max(max_from_right, temp) #update max_from_right if temp was larger
        return arr
