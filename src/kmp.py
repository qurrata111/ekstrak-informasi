# KMP ALGORITHM
def compute_fail(pattern):
  fail = [-9999 for i in range (len(pattern))]
  fail[0] = 0

  m = len(pattern)
  j = 0
  i = 1
  
  while (i < m):
    if (pattern[i] == pattern[j]):
      fail[i] = 1 + j
      i += 1
      j += 1
    elif (j > 0):
      j = fail[j-1]
    else:
      fail[i] = 0
      i += 1

  return fail

def kmp_match(text, pattern):
  n_text = text.lower()
  n_pattern = pattern.lower()
  n = len(n_text)
  m = len(n_pattern)

  fail = compute_fail(n_pattern)
  
  i = 0
  j = 0
  
  while (i < n):
    if (n_pattern[j] == n_text[i]):
      if (j == m-1):
        return i-m+1
      i += 1
      j += 1
    elif (j > 0):
      j = fail[j-1]
    else:
      i += 1

  return -999