import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
s.loc['c']=0
def solution(s1 = pd.Series):
    result = s1.data()
    return result
print(solution(s))