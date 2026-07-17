class Solution:

    def encode(self, strs: List[str]) -> str:
        lista_of_strings = []

        for string in strs:
            lista_of_strings.append(str(len(string)) + "#" + string)

        x = "".join(lista_of_strings)
        return x

        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
    
            lenght = int(s[i:j])
            word = s[j + 1: j + 1 + lenght]
            result.append(word)
            i = j + 1 + lenght

        return result