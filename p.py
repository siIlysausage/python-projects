def FindMiddle(start,end)   :
    return start + (abs(end - start) / 2)

def Div(one,two):
    while one >= two:
        one -= two
    return one

def FindFullFraction(one,two,other):
    return two * (other / one)

print(FindMiddle(100, 6000))
print("------------------")
print(Div(10,5))
print("-")
print(FindFullFraction(7,9,70))