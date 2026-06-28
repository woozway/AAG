f, ans = [0] * 100, [0] * 13
s = [[0] * 5 for _ in range(14)]

def main():
    global f, ans, s
    for i in range(1, 14):
        s[i][1:] = input().split()
    f[ord('A')] = 1
    for i in range(2, 10): f[ord('0') + i] = i
    f[ord('0')] = 10
    f[ord('J')] = 11
    f[ord('Q')] = 12
    f[ord('K')] = 13
    for i in range(1, 5):
        t = s[13][i]
        while f[ord(t)] != 13:
            ans[f[ord(t)]] += 1
            tmp = s[f[ord(t)]][4]
            for j in range(4, ans[f[ord(t)]], -1):
                s[f[ord(t)]][j] = s[f[ord(t)]][j - 1]
            t = tmp
    cnt = 0
    for i in range(1, 13):
        if ans[i] == 4: cnt += 1
    print(cnt)
    
main()