def build_last(pattern):
    last = [-1]*256 
    
    for i in range(len(pattern)): 
        last[ord(pattern[i])] = i; 

    return last 
  
def bm_match(text, pattern):
    n_text = text.lower()
    n_pattern = pattern.lower()
    
    m = len(n_pattern) 
    n = len(n_text) 

    last = build_last(n_pattern)  
    
    s = 0

    while(s <= n-m): 
        j = m-1
        
        while j>=0 and n_pattern[j] == n_text[s+j]: 
            j -= 1
  
        if j<0:
            # pattern match
            return s
            s += (m-last[ord(n_text[s+m])] if s+m<n else 1) 
        else: 
            s += max(1, j-last[ord(n_text[s+j])])

    return -999 