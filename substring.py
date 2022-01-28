class Solution:
    
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        word_count = DefaultDict(list)
        for i, c in enumerate(s):
            if c not in word_count:
                word_count[c].extend([i,i])
            else: 
                word_count[c][1] = i
    #expanding each letter

        for key in word_count:
            start, end = word_count[key]
            stack = [(start, end)]

            while stack:
                len_s, len_e = stack.pop()
                for i in range (len_s, len_e+1):
                    new_s, new_e = word_count[s[i]]

                    if new_s < start:
                        stack.append((new_s, start-1))
                        start = new_s

                    if new_e > end:
                        stack.append((end+1, new_e))
                        end = new_e
            word_count[key] = (start, end)
        sorted_ranges = sorted(word_count.values(), key = lambda x: x[1] - x[0])
        word_ranges = []
        result = []

        for start, end in sorted_ranges:
            if any( end >= s1 and e1 >= start for s1, e1 in word_ranges):
                continue
            word_ranges.append((start, end))
            result.append(s[start: end+1])
        return result

        
