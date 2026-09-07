class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for word in strs:
            bucket = [0] * 26
            for letter in word:
                bucket[ord(letter) - 97] += 1

            bucket_tupple = tuple(bucket)

            if bucket_tupple not in dictionary:
                dictionary[bucket_tupple] = []

            dictionary[bucket_tupple].append(word)

        list_result = []

        for values in dictionary.values():
            list_result.append(values)

        return list_result
        