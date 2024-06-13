class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort() 
        students.sort() 
        n = len(students)
        c = 0
        for i in range(n) : 
            c += abs(students[i]-seats[i])
        return c
        