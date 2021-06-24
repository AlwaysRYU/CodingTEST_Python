def solution(S):
    N = S.count("a")
    if N == 0 :
        length = len(S) - 3
        return (length + 1) * (length) * (length -1) 
    elif (N % 3) != 0 :
        return 0
    else:
        mok = (N // 3) 
        # print(mok)
        F, M, L = 0,0,0
        bet1, bet2 = 0, 0
        for i in S :
            if i == "a" :
                if F < mok :
                    F += 1
                    continue
                elif F == mok and M < mok :
                    M += 1
                    continue
                elif F == mok and M == mok and L < mok :
                    L += 1
                    continue

            elif i == "b" :
                if F < mok :
                    continue
                elif F == mok and M < mok :
                    bet1 += 1
                    continue
                elif F == mok and M == mok and L < mok :
                    bet2 += 1
                    continue 
        # print(bet1, bet2)
        if bet1 == 0 and bet2 == 0:
            return 1
        elif bet1 == 0 and bet2 != 0:
            return bet2 + 1
        elif bet1 !=0 and bet2 == 0:
            return bet1 + 1
        else :
            return (bet1 + 1) * (bet1 + 1)
        
print(solution("babaa"))
print(solution("ababa"))
print(solution("aba"))
print(solution("bbbbb"))