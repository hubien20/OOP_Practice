class Polynomial:
    def __init__(self, coeffs: list):

        self.coeffs = list(coeffs)

    def __str__(self):
        n = len(self.coeffs)

        if not self.coeffs or all(c == 0 for c in self.coeffs):
            return "0"

        terms = []
        for i, c in enumerate(self.coeffs):
            if c == 0:
                continue
            
            power = n - 1 - i  
            
            if power == n - 1 - (next(idx for idx, val in enumerate(self.coeffs) if val != 0)):

                if c == -1 and power > 0:
                    coeff_str = "-"
                elif c == 1 and power > 0:
                    coeff_str = ""
                else:
                    coeff_str = str(c)
            else:

                if c > 0:
                    coeff_str = f"+ {c if c != 1 or power == 0 else ''}"
                else:
                    coeff_str = f"- {abs(c) if abs(c) != 1 or power == 0 else ''}"

            if power == 0:
                term_str = coeff_str
            elif power == 1:
                term_str = f"{coeff_str}x"
            else:
                term_str = f"{coeff_str}x^{power}"
                
            terms.append(term_str)

        res = " ".join(terms).strip()

        if res.startswith("- "):
            res = "-" + res[2:]
        return res

    def __call__(self, x) -> int:
        result = 0
        for c in self.coeffs:
            result = result * x + c
        return result

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        len1 = len(self.coeffs)
        len2 = len(other.coeffs)
        max_len = max(len1, len2)
        
        c1 = [0] * (max_len - len1) + self.coeffs
        c2 = [0] * (max_len - len2) + other.coeffs

        new_coeffs = [a + b for a, b in zip(c1, c2)]

        return Polynomial(new_coeffs)