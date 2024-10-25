class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        result = []
        for path in folder:
            # If the result list is empty or the current path is not a subfolder of the last added path
            if not result or not path.startswith(result[-1] + '/'):
                result.append(path)
        return result



        

         