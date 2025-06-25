class Solution:
      def isPowerOfFour(self, n: int) -> bool:
        num=1
        while True:
            if n == 1:
                return True
            elif n%2!=0:
                return False
            else:
                result=2**i
                if n == result:
                    return True
                elif result>n:
                    return False
                else:
                    num+=1
                    