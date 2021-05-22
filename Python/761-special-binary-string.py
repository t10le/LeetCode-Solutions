# def isSpecial(subString):
#     arr = []
#     if subString.count('0') == subString.count('1'):
#         for e in subString:
#             arr.append(e)
#             print("1's:{} 0's:{}".format(arr.count('1'), arr.count('0')))
#             if arr.count('1') < arr.count('0') and arr.count('0') != None:
#                 print(
#                     "1's:{} 0's:{} <-- TRIGERRED".format(arr.count('1'), arr.count('0')))
#                 return False
#     return True


def isSpecial(subString):
    if subString.count('0') == subString.count('1'):
        for i in range(len(subString)):
            print("1's:{} 0's:{}".format(
                subString.count('1'), subString.count('0')))
            if subString[:i].count('1') < subString[:i].count('0'):
                print(
                    "1's:{} 0's:{} <-- TRIGERRED".format(subString.count('1'), subString.count('0')))
                return False
    return True


print(isSpecial("1100"))
