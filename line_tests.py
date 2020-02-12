import unittest
import line

class LineTests(unittest.TestCase):
    def test_line(self):
        # Add code here.
        l = line.Line(0, 1, 2, 3)
        self.assertEqual(l.x1, 0)
        self.assertEqual(l.y1, 1)
        self.assertEqual(l.x2, 2)
        self.assertEqual(l.y2, 3)

    def test_line_again(self):
        # Add code here.
        l = line.Line(4, 5, 6, 7)
        self.assertEqual(l.x1, 4)
        self.assertEqual(l.y1, 5)
        self.assertEqual(l.x2, 6)
        self.assertEqual(l.y2, 7)

        

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
