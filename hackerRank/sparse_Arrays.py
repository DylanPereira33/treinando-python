def matchingStrings(strings, queries):
    # Write your code here
    string_counts = {}
    for string in strings:
        if string in string_counts:
            string_counts[string] += 1
        else:
            string_counts[string] = 1
    
    results = []
    for query in queries:
        if query in string_counts:
            results.append(string_counts[query])
        else:
            results.append(0)
    
    return results