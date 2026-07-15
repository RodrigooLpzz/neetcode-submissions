class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary_words = {}

        for word in strs:
            key = [0] * 26
            for letter in word:
            # print(strs[n][m])
                key[ord(letter) - 97] += 1
  
            tuple_key = tuple(key)

            if tuple_key not in dictionary_words:
                dictionary_words[tuple_key] = []
  
            dictionary_words[tuple_key].append(word)


        result = []
        for values in dictionary_words.values():
            result.append(values)

        return result;  