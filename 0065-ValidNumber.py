class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        isValidNumberPart = False
        isExponentValid = False
        isPositive = True
        isExponetPositive = True
        if s[0] == '-':
            isPositive = False
            s = s[1:]

        elif s[0] == '+':
            isPositive = True
            s = s[1:]

        elif s[0] not in ['+', '-']:
            isPositive = True
        
        if len(s.split('e'))==2:
            numberPart = s.split('e')[0]
            exponetPart = s.split('e')[1]
        elif len(s.split('E'))==2:
            numberPart = s.split('E')[0]
            exponetPart = s.split('E')[1]
        elif len(s.split('e'))==1:
            numberPart = s.split('e')[0]
            exponetPart = ''
        elif len(s.split('E'))==1:
            numberPart = s.split('E')[0]
            exponetPart = ''
        elif len(s.split('e'))>2:
            return False
        elif len(s.split('E'))>2:
            return False

        if sum([ch.isdigit() for ch in numberPart]) == 0:
            return False

        numberPartValidity = [n.isdigit() for n in numberPart]
        if len(numberPartValidity)==0:
            return False
        else:
            if len(numberPartValidity) - sum(numberPartValidity)>=2:
                return False
            elif len(numberPartValidity) - sum(numberPartValidity)==0:
                isValidNumberPart = True
            elif len(numberPartValidity) - sum(numberPartValidity)==1:
                nonCharacter = [s[i] for i in range(len(numberPartValidity)) if not numberPartValidity[i]]
                if nonCharacter[0]=='.':
                    isValidNumberPart = True
                else:
                    return False

        
        if (len(numberPart)!=len(s)) and (len(exponetPart)==0):
            return False
        elif (len(numberPart)!=len(s)) and (len(exponetPart)>0):
            if not ((exponetPart[0] in ['+', '-']) or (exponetPart[0].isdigit())):
                return False
            elif (exponetPart[0] in ['+', '-']) and len(exponetPart)==1:
                return False
            else:
                if exponetPart[0] == '-':
                    isExponetPositive = False
                    exponetPart = exponetPart[1:]
                elif exponetPart[0] == '+':
                    isExponetPositive = True
                    exponetPart = exponetPart[1:]
                
                exponentCharacters = [ec.isdigit() for ec in exponetPart]

                if len(exponentCharacters)==sum(exponentCharacters):
                    isExponentValid = True
                else:
                    isExponentValid = False
            return isValidNumberPart and isExponentValid

        elif (len(numberPart)==len(s)) and (len(exponetPart)==0):
            return isValidNumberPart


s = "-90E3"
print(Solution().isNumber(s))