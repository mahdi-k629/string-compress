class string_compress():
    def compressing(self, chars):
        ans = []
        size = len(chars)
        ################
        pointer1 = 0
        ################
        while (pointer1 < size):
            char = chars[pointer1]
            pointer2 = pointer1 + 1
            count = 1
            while (pointer2 < size):
                temp2 = chars[pointer2]
                if char == temp2:
                    pointer2 += 1
                    count += 1
                else:
                    break
            ############################
            pointer1 = pointer2
            ############################
            if count == 1:
                ans.append(char)
            elif count >= 20:
                ans.append(char)
                for digit in str(count):
                    ans.append(digit)
            else:
                    ans.append(char)
            ans.append(str(count))
        chars[::] = ans
        return chars

list = ["a", "b", "a", "b", "b"]
stc = string_compress()
print(stc.compressing(list))