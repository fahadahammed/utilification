class Stringify:
    """To compare characters of two strings and give the common characters."""
    def __init__(self, s1, s2):
        self.s1 = s1
        self.ls1 = len(s1)
        self.s2 = s2
        self.ls2 = len(s2)
        self.commonChars = []

    def compare(self):
        if self.ls1 == self.ls2:
            self.s1_s2_string_same_len()
        if self.ls1 > self.ls2:
            self.s2_string_smaller()
        if self.ls1 < self.ls2:
            self.s1_string_smaller()

        final_string = self.convert_list_to_str()
        return {
            "stringOne": self.s1,
            "stringTwo": self.s2,
            "commonCharacters": final_string
        }

    def convert_list_to_str(self):
        return ''.join(self.commonChars)

    def s1_s2_string_same_len(self):
        for i in self.s1:
            if self.s2.count(i) == 1:
                self.commonChars.append(i)
            if self.s2.count(i) > 1:
                if self.s1.count(i) == 1:
                    self.commonChars.append(i)
                if self.s1.count(i) > 1:
                    self.commonChars.append(i)
        return True

    def s1_string_smaller(self):
        for i in self.s1:
            if self.s2.count(i) == 1:
                self.commonChars.append(i)
            if self.s2.count(i) > 1:
                if self.s1.count(i) == 1:
                    self.commonChars.append(i)
                if self.s1.count(i) > 1:
                    self.commonChars.append(i)
        return True

    def s2_string_smaller(self):
        for i in self.s2:
            if self.s1.count(i) == 1:
                self.commonChars.append(i)
            if self.s1.count(i) > 1:
                if self.s2.count(i) == 1:
                    self.commonChars.append(i)
                if self.s2.count(i) > 1:
                    self.commonChars.append(i)
        return True


# OUTPUT
mystr1 = """I am not fahad.aahammed.

R^ONAsjkdhsuiadg78asdgf hagsdvb jafhdvbuiafdgvjhxbdavfvasdfasdas
FAHADpp pp

Late"""
mystr2 = """I Aam fahad ahammed.
asdf

U^S&*tegrij asdKate
late
Lateee
asdfas dmjhviadfjgvkadg vuiondhugadgfjhsagdfjkhasdk gaudgkadjhgay nasdfhaj FAHAD
^
asdfsad
"""
print(Stringify(s1=mystr1, s2=mystr2).compare()["commonCharacters"])






# From Files
# wordsOne = open("data/words-part1.txt", "r")
# wordsTwo = open("data/words-part2.txt", "r")
# matchedCharacters = open("data/final.txt", "a+")
#
# wordsOnereadlines = wordsOne.readlines()
# wordsTworeadlines = wordsTwo.readlines()
#
#
#
# wordsMatchedCharacters = []
#
#
# for line_no, line in enumerate(wordsOnereadlines):
#     wordOne = line.replace("\n", "")
#     wordTwo = wordsTworeadlines[line_no].replace("\n", "")
#     matchedChars = Stringify(s1=wordOne, s2=wordTwo).compare()
#     if matchedChars["commonCharacters"]:
#         wordsMatchedCharacters.append(matchedChars)
#         fstr = matchedChars["stringOne"] + " " + matchedChars["stringTwo"] + " " + matchedChars["commonCharacters"] + "\n"
#         matchedCharacters.write(fstr)
#
#
#
# print(wordsMatchedCharacters)
#
#
#
# wordsOne.close()
# wordsTwo.close()
# matchedCharacters.close()