class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        boxes=[]
        for i in range(len(nums)+1):
            boxes.append([])
        for i in counts:
            score = counts[i]
            boxes[score].append(i)
        result=[]
        for i in range(len(boxes)-1,0,-1):
            for i in boxes[i]:
                result.append(i)
                if len(result)==k:
                    return result