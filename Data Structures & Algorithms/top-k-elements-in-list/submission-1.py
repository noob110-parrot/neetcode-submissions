import numpy as np
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pluhh = defaultdict(int)

        for i in nums:
            pluhh[i] += 1

        maponzottttta = sorted(
            pluhh,
            key=pluhh.get,
            reverse=True
        )

        return maponzottttta[:k]

 
 






    



        