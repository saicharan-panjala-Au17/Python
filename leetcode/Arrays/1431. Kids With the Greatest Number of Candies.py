#1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = []
        for candy in candies:
            total= candy + extraCandies 
    
            b = True
            for candy2 in candies:
                if total < candy2:
                    b = False
            a.append(b) 
        return a