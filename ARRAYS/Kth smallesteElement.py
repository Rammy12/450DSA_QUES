'''
QUESTION:

Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Note :-  l and r denotes the starting and ending index of the array.

Example 1:

Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.
Example 2:

Input:
N = 5
arr[] = 7 10 4 20 15
K = 4
Output : 15
Explanation :
4th smallest element in the given 
array is 15.
Your Task:
You don't have to read input or print anything. Your task is to complete the function kthSmallest() which takes the array arr[], integers l and r denoting the starting and ending index of the array and an integer K as input and returns the Kth smallest element.
 
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(log(n))
Constraints:
1 <= N <= 10^5
1 <= arr[i] <= 10^5
1 <= K <= N
'''

#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        
        # 3, 4,7,10,15,20
        #METHOD 1---------------------------------------------------------------------------------------
        
        arr.sort()
        return arr[k-1]
      
      
      #METHOD-2------------------------------------------------------------------------------------
        
        #using set data structure
        
        #s={4,7,10,15,20}
        #k=4 ->3->2 ->1
        
        s= set(arr)
        for i in s:
            if k == 1:
                return i     # i is the Kth element in the set
                break
            k -= 1
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends
