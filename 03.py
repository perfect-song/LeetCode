'''

最长公共子串

'''
strs = ["flower","flow","flight"]

# m = min([len(v) for v in strs])
# print(m)


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        i = 0
        m = min([len(v) for v in strs])
        ss = strs[0]
        while i < m:
            # ss = strs[0]
            for s in strs[1:]:
                if ss[i] != s[i]:
                    return ss[:i]
            i += 1

        return ss[:i]

So = Solution()

long = So.longestCommonPrefix(strs)
print(long)