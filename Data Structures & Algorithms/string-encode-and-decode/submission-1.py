class Solution:

    def encode(self, strs: List[str]) -> str:
        lista = []
        for word in strs:
            lista.append(str(len(word)) + "#" + word)

        string = "".join(lista)
        return string

    def decode(self, s: str) -> List[str]:
        resultado = []
        start = 0
        while start < len(s):
            decorator = s.find('#', start)
            lenght = int(s[start:decorator])
            resultado.append(s[decorator + 1:decorator + 1 + lenght])
            start = decorator + 1 + lenght
        
        return resultado
