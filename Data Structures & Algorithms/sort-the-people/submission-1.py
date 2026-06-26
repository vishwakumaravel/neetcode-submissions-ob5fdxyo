class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dicto={}
        for x, y in zip(names, heights):
            dicto[y] = x
        
        # Sort the height keys in descending order
        sorted_heights = sorted(dicto.keys(), reverse=True)
        
        # Return the names corresponding to the sorted heights
        return [dicto[h] for h in sorted_heights]