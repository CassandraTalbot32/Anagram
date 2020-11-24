import itertools
import unittest

class Anagrams:

    
    with open ('C:/Users/Cassie/Downloads/words.txt') as f:
        words = f.read().split()


    letters = input("Enter the letters")
    for p in itertools.permutations(letters):
        word = "".join(p)
        if word in words:
            print(word)
        
    def get_anagrams(self, word):
        pass

class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEquals(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])
        self.assertEquals(anagrams.get_anagrams('Earth'), ['hater', 'Heart', 'Earth'])
        
                          
if __name__ == '__main__':
    unittest.main()
