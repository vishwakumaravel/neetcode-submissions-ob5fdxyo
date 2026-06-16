class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        window = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[j] in words[i]:
                        window.append(words[j])
        return list(set(window))
