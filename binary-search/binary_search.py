def binary_search(key, haystack, minim, maxim):
    if maxim < minim:
        return -1
    else:
        midpoint = find_midpoint(minim, maxim)
        
        if haystack[midpoint] < key:
            return binary_search(key, haystack, midpoint + 1, maxim)
        elif haystack[midpoint] > key:
            return binary_search(key, haystack, minim, midpoint-1)
        else:
            return midpoint
            
            
def find_midpoint(minim, maxim):
    return int(maxim - ((maxim - minim) / 2))


haystack = [0, 1, 4, 6, 34, 65, 76, 86, 123, 144, 233]
print(binary_search(76, haystack, 0, len(haystack)))