class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            print i 
            print("A[fast] : ", A[i]) 
            print("A[slow] : ", A[newTail]) 
            print("A : ", A) 
            print("-----") 
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]
                
        return newTail + 1

if __name__ == "__main__":
    nums = [0,1,1,2]
    object = Solution()
    print object.removeDuplicates(nums)
    print nums