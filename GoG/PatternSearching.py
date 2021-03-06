"""
Examples:
1) Input:

  txt[] =  "THIS IS A TEST TEXT"
  pat[] = "TEST"
Output

Pattern found at index 10
2) Input:

  txt[] =  "AABAACAADAABAAABAA"
  pat[] = "AABA"
Output:

   Pattern found at index 0
   Pattern found at index 9
   Pattern found at index 13
"""

def solution(txt, pat):
    lenh_text = len(txt)
    lenh_pat = len(pat)
    f = (lenh_text-lenh_pat)
    for i in range(f+1):
        if txt[i] == pat[0]:
            stillok = True
            j = 0
            tmp_i = i
            while stillok and (j < lenh_pat-1):
                j += 1
                tmp_i += 1
                if txt[tmp_i] != pat[j]:
                    stillok = False
            if stillok:
                print "Pattern found at index %d" % (i)

txt =  "ABAABBAABAB"
pat = "AB"

solution(txt, pat)






def solution2(smallStr, bigStr):
    m = len(smallStr)
    n = len(bigStr)
    res = 0
    if m > n:
      return -1

    for i in range(0, (n-m)+1):
       stillok = True
       j = 0
       while stillok and (j < m):
           if smallStr[j] != bigStr[i]:
             stillok = False
           else:
             i += 1
             j += 1
       if stillok:
         res += 1

    return res
print solution2(pat, txt)