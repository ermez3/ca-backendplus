import unittest
import kata_consecutive_strings

class Test_Kata_Consecutive_Strings(unittest.TestCase):
    def test_kata(self):
        self.assertEqual(kata_consecutive_strings.longest_consec(["it","it","it", "it", "it","iti"], 6), "ititititititi")
        self.assertEqual(kata_consecutive_strings.longest_consec([1],5),"")
        self.assertEqual(kata_consecutive_strings.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEqual(kata_consecutive_strings.longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        self.assertEqual(kata_consecutive_strings.longest_consec([], 3), "")
        self.assertEqual(kata_consecutive_strings.longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEqual(kata_consecutive_strings.longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEqual(kata_consecutive_strings.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEqual(kata_consecutive_strings.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertEqual(kata_consecutive_strings.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertEqual(kata_consecutive_strings.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Kata_Consecutive_Strings)
    unittest.TextTestRunner(verbosity=0).run(suite)
