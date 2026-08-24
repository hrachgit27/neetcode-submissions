class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        net_income = 0

        for index, num in enumerate(prices):
            for index2, num2 in enumerate(prices):
                if num2 - num > net_income and index2 > index:
                    net_income = num2 - num

        
        return net_income
        
