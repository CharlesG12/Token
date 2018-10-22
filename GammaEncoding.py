class GammaEncoding:
    def __init__(self):
        self.gamma_codes = []

    def run(self, gaps):
        for i in range(len(gaps)):
            r = self.encoding(gaps[i])
            self.gamma_codes.append(r)
        return self.gamma_codes

    def encoding(self, gap):
        b_code = format(gap, "b")
        offset = b_code[1:]
        len_offset = len(offset)
        unary_len = self.unary(len_offset)
        return str(unary_len) + str(offset)

    @staticmethod
    def unary(num):
        ans = 0
        for i in range(num):
            ans += 10 * i
        return ans


