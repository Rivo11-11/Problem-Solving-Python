class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        mymap = {}
        def convert(nums) :
            for index,num in enumerate(nums) :
                base  = 1
                new = 0
                temp = num
                if temp == 0 :
                    mymap[(temp,index)] = mapping[temp]
                    continue
                while num :
                    i = num % 10 
                    new += mapping[i] * base
                    num //= 10
                    base *= 10
                mymap[(temp,index)] = new
        convert(nums)
        indexed_data = [(key[1], key[0], value) for  (key, value) in mymap.items()]
        sorted_indexed_data = sorted(indexed_data, key=lambda item: (item[2], item[0]))
        return [key for _, key, _ in sorted_indexed_data]
        