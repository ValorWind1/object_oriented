class secretString:

    def __init__(self,plain_string,pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """ if string is correct show string"""

        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return " "

string1 = secretString("Password : Hidden","abcd")
print(string1.decrypt("abcd"))


print(string1._secretString__plain_string)