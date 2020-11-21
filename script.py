def smallestSubString(S):
    distChar = 0
    x, y = [0]*26, [0]*26
    for i in range(len(S)):
        if x[ord(S[i]) - ord('a')] == 0:
            distChar += 1
        x[ord(S[i]) - ord('a')] += 1

    low, high, count = 0, 0, 0
    res = 0

    while count < distChar:
        if y[ord(S[high]) - ord('a')] == 0:
            count += 1
        y[ord(S[high]) - ord('a')] += 1
        while low < high:
            if y[ord(S[low]) - ord('a')] == 1:
                break
            y[ord(S[low]) - ord('a')] -= 1
            low += 1
        high += 1
    res = high - low

    while high < len(S):
        y[ord(S[high]) - ord('a')] += 1
        while low < high:
            if y[ord(S[low]) - ord('a')] == 1:
                break
            y[ord(S[low]) - ord('a')] -= 1
            low += 1
        high += 1
        res = min(res, high - low)
    return res

if __name__=='__main__':
    S = str(input())
    if S.islower():
        print(smallestSubString(S))
    else:
        print("Input Error! Please check input and try again.")
