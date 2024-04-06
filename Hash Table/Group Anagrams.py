def group_anagrams(strings):
    dict1={}
    for i in strings:
        j = ''.join(sorted(i))
        if j in dict1:
            dict1[j].append(i)
        else:
            dict1[j]=[i]
    
    return list(dict1.values())


print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )
