class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = list()

        line = list()
        lenght = 0
        for word in words:
            if (lenght + len(word)) > maxWidth:
                lines.append(self.justifyLine(line, maxWidth, False))
                line = list()
                line.append(word)
                lenght = len(word) + 1
            else:
                line.append(word)
                lenght = lenght + len(word) + 1
        lines.append(self.justifyLine(line, maxWidth, True))
            
        return lines

    
    def justifyLine(self, words_line, maxWidth, lastLine=False):
        line = str()
        num_slots = len(words_line)
        spaces_per_slot = [0] * num_slots
        for i in range(num_slots - 1):
            spaces_per_slot[i] += 1
        spaces_padding = maxWidth - sum([len(word) for word in words_line]) - sum(spaces_per_slot)

        if not lastLine:
            divisor = max(1, (num_slots - 1))
            quotient = spaces_padding // divisor
            remainder = spaces_padding % divisor
            for i in range(num_slots - 1):
                spaces_per_slot[i] += quotient
                if i < remainder:
                    spaces_per_slot[i] += 1
        
        for i, word in enumerate(words_line):
            spaces = " " * spaces_per_slot[i]
            line += word + spaces

        while len(line) < maxWidth:
            line += " "
        return line