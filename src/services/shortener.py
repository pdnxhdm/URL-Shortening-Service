from string import digits, ascii_lowercase, ascii_uppercase


ALPHABET = digits + ascii_lowercase + ascii_uppercase
BASE = len(ALPHABET)


class ShortenerService:
    @staticmethod
    def encode(num: int) -> str:
        if num == 0:
            return ALPHABET[0]
        
        arr = []

        while num:
            num, rem = divmod(num, BASE)
            arr.append(ALPHABET[rem])
        
        arr.reverse()
        return "".join(arr)
    
    @staticmethod
    def decode(code: str) -> int:
        num = 0

        for char in code:
            num = num * BASE + ALPHABET.index(char)
        
        return num