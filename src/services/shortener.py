from src.core.config import config

from hashids import Hashids


MIN_LENGTH = 3


class ShortenerService:
    _hashids = Hashids(salt=config.SALT, min_length=MIN_LENGTH)

    @staticmethod
    def encode(num: int) -> str:
        return ShortenerService._hashids.encode(num)
