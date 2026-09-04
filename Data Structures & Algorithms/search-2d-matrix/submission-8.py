class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m*n)) = O(log(m) + log(n))
        def search_row(target: int, lst: List[int]) -> bool: # O(log n)
            l = 0 
            r = len(lst) - 1
            mid = (l + r ) // 2
            while l <= r:
                if target == lst[mid]:
                    return True 

                elif target < lst[mid]:
                    r = mid -1 
                    mid = (l + r) // 2

                elif target > lst[mid]:
                    l = mid + 1 
                    mid = (l + r) //2
            return False
    
        if len(matrix) == 1:
            return search_row(target, matrix[0]) 
        
        # Search for the column range, then index into there to search for the 
        l = 0
        r = len(matrix) - 1
        mid = (l + r) //2

        while l <= r: 
            
            mid = (l + r) // 2

            if target < matrix[mid][0]:
                r = mid - 1

            elif target > matrix[mid][-1]:
                l = mid + 1

            else: 
                return search_row(target, matrix[mid])
        return False
        