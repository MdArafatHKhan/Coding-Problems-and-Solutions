class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        # if the number of points are not more than 2, they are trivially on the same line
        if len(points)<3:
            return len(points)

        maxColinearPointCounts = []

        for i in range(len(points)):
            slopeValue = []
            for j in range(len(points)):
                if i!=j:
                    if points[j][0]!=points[i][0]:
                        slopeValue.append(1.0*(points[j][1]-points[i][1])/(points[j][0]-points[i][0]))
                    else:
                        slopeValue.append('inf')
                else:
                    slopeValue.append('undefined')
        
            maxCountSlopeValue = max(slopeValue,key=slopeValue.count)
            maxPointsCount = len([x for x in slopeValue if x==maxCountSlopeValue])
            maxColinearPointCounts.append(maxPointsCount)


        return max(maxColinearPointCounts)+1
        
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(Solution().maxPoints(points))