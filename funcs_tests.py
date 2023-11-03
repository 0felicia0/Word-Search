import unittest
from funcs import *

# here is a sample puzzle for you to use in your tests
puzzle = ["WAQHGTTWEE",
          "CBMIVQQELS",
          "AZXWKWIIIL",
          "LDWLFXPIPV",
          "PONDTMVAMN",
          "OEDSOYQGOB",
          "LGQCKGMMCT",
          "YCSLOACUZM",
          "XVDMGSXCYZ",
          "UUIUNIXFNU"]
		  
class TestCases(unittest.TestCase):
          
   # add your tests here
   def test_check_up1(self):
      self.assertEqual(check_up(puzzle, 2, 0, "ACW"), True)
   def test_check_up2(self):
      self.assertEqual(check_up(puzzle, 0, 0, "WL"), False)
   def test_check_up3(self):
      self.assertEqual(check_up(puzzle, 1, 7, "EWG"), False)

   def test_check_down1(self):
      self.assertEqual(check_down(puzzle, 1, 0, "CALPOLY"), True)
   def test_check_down2(self):
      self.assertEqual(check_down(puzzle, 1, 0, "CPOLY"), False)
   def test_check_down3(self):
      self.assertEqual(check_down(puzzle, 7, 0, "YXUZD"), False)
   def test_check_down4(self):
      self.assertEqual(check_down(puzzle, 9, 0, "UNIX"), False)

   def test_check_forward1(self):
      self.assertEqual(check_forward(puzzle, 5, 3, "SOY"), True)
   def test_check_forward2(self):
      self.assertEqual(check_forward(puzzle, 5, 3, "SOYB"), False)
   def test_check_forward3(self):
      self.assertEqual(check_forward(puzzle, 8, 7, "CYZXS"), False)

   def test_check_backward1(self):
      self.assertEqual(check_backward(puzzle, 4, 8, "MAV"), True)
   def test_check_backward2(self):
      self.assertEqual(check_backward(puzzle, 4, 8, "NAV"), False)
   def test_check_backward3(self):
      self.assertEqual(check_backward(puzzle, 9, 2, "IUUXCV"), False)

   def test_check_diagonal1(self):
      self.assertEqual(check_diagonal(puzzle, 6, 5, "GCC"), True)
   def test_check_diagonal2(self):
      self.assertEqual(check_diagonal(puzzle, 6, 5, "GCCX"), False)
   def test_check_diagonal3(self):
      self.assertEqual(check_diagonal(puzzle, 7, 7, "UYUZXC"), False)
   def test_check_diagonal4(self):
      self.assertEqual(check_diagonal(puzzle, 9, 9, "UNIX"), False)

   def test_get_locations_c1(self):
      self.assertEqual(get_locations_c(puzzle, "W"), [(0, 0), (0, 7), (2, 3), (2, 5), (3, 2)])
   def test_get_locations_c2(self):
      self.assertEqual(get_locations_c(puzzle, "Z"), [(2, 1), (7, 8), (8, 9)])

   def test_check_all0(self):
      self.assertTrue(check_all(puzzle, 2, 0, "ACW"), True)
   def test_check_all1(self):
      self.assertTrue(check_all(puzzle, 1, 0, "CALPOLY"), True)
   def test_check_all2(self):
      self.assertTrue(check_all(puzzle, 5, 3, "SOY"), True)
   def test_check_all3(self):
      self.assertTrue(check_all(puzzle, 4, 8, "MAV"), True)
   def test_check_all4(self):
      self.assertTrue(check_all(puzzle, 6, 5, "GCC"), True)
   def test_check_all5(self):
      self.assertFalse(check_all(puzzle, 2, 9, "UNIX"), False)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

