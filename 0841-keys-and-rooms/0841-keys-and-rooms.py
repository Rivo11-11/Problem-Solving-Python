class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        myset = set()
        n = len(rooms)
        def dfs(i) :
            myset.add(i)
            for key in rooms[i] :
                    if key not in myset :
                         dfs(key)
        dfs(0)
        return n == len(myset)