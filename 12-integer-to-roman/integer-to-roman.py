class Solution:
    def intToRoman(self, num: int) -> str:
        def sol1(num):
            intToRomanSymbol = {
            1 : "I",
            4 : "IV",
            5 : "V",
            9: "IX",
            10 : "X",
            40 : "XL",
            50 : "L",
            90 : "XC",
            100 : "C",
            400: "CD",
            500 : "D",
            900 : "CM",
            1000 : "M"
        }
            
            roman = str()
            for i in reversed(intToRomanSymbol.keys()):
                while (num - i >= 0):
                    num -= i
                    roman += intToRomanSymbol[i]
          
            return roman

        def sol2(num):
            def getFirstDigit(number):
                firstDigit = number // (10 ** (len(str(number))-1))

                return firstDigit

            intToRomanSymbol = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M"
        }   

            romanValues = [1000, 500, 100, 50, 10, 5, 1]

            index = 0
            roman = str()
    
            while (num > 0):
                firstDigit = getFirstDigit(num)
                if not (firstDigit == 4 or firstDigit == 9):
                    if num - romanValues[index] >= 0:
                        num -= romanValues[index]
                        roman += intToRomanSymbol[romanValues[index]]
                    else:
                        index += 1
                else:
                    if romanValues[index] < num:
                        if firstDigit == 9:
                            num = num - romanValues[index-1] + romanValues[index+1]
                            roman = roman + intToRomanSymbol[romanValues[index+1]] + intToRomanSymbol[romanValues[index-1]]
                        if firstDigit == 4:
                            num = num - romanValues[index-1] + romanValues[index]
                            roman = roman + intToRomanSymbol[romanValues[index]] + intToRomanSymbol[romanValues[index-1]]
                    index += 1
                    
            return roman

       
        return sol1(num)


        