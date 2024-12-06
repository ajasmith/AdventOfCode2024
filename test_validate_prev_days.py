import unittest
import day1
import day2
import day3
import day4
import day5
import day6

class validate_previous_days(unittest.TestCase):
    def test_day1(self):
        self.assertEqual(day1.part1("test/day1.txt"), 11)
        self.assertEqual(day1.part2("test/day1.txt"), 31)

    def test_day1_real_data(self):
        self.assertEqual(day1.part1("data/day1.txt"), 3569916)
        self.assertEqual(day1.part2("data/day1.txt"), 26407426)

    def test_day2(self):
        self.assertEqual(day2.run("test/day2.txt", 1), 2)
        self.assertEqual(day2.run("test/day2.txt", 2), 4)

    def test_day2_real_data(self):
        self.assertEqual(day2.run("data/day2.txt", 1), 606)
        self.assertEqual(day2.run("data/day2.txt", 2), 644)

    def test_day3(self):
        self.assertEqual(day3.part1("test/day3.txt"), 161)
        self.assertEqual(day3.part2("test/day3.txt"), 48)

    def test_day3_real_data(self):
        self.assertEqual(day3.part1("data/day3.txt"), 153469856)
        self.assertEqual(day3.part2("data/day3.txt"), 77055967)

    def test_day4(self):
        self.assertEqual(day4.part1("test/day4.txt"), 18)
        self.assertEqual(day4.part2("test/day4.txt"), 9)

    def test_day4_real_data(self):
        self.assertEqual(day4.part1("data/day4.txt"), 2496)
        self.assertEqual(day4.part2("data/day4.txt"), 1967)

    def test_day5(self):
        self.assertEqual(day5.run("test/day5.txt"), [143, 123])
    
    def test_day5_real_data(self):
        self.assertEqual(day5.run("data/day5.txt"), [6242, 5169])

    def test_day6(self):
        self.assertEqual(day6.run("test/day6.txt"), (41, 6))
    
    def test_day6_real_data(self):
        self.assertEqual(day6.run("data/day6.txt"), (4776, 1586))
    
if __name__ == '__main__':
    unittest.main()