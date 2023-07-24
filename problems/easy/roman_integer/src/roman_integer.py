class Solution:
    DECODING_MAP = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                    }

    @classmethod
    def decoder(cls, s: str) -> int:
        return cls.DECODING_MAP[s]

    def romanToInt(self, s: str) -> int:
        sum_ = 0

        for current_index in range(len(s) - 1):
            next_index = current_index + 1

            current_value = self.decoder((s[current_index]))
            next_value = self.decoder((s[next_index]))

            if next_value > current_value:
                sum_ -= current_value
            else:
                sum_ += current_value

        last_char_value = self.decoder(s[-1])
        return last_char_value + sum_
