import unittest
import XYRobot as Rob
from math import pi, cos, sin

class TestXYRobot(unittest.TestCase):
    
    def setUp(self):
        self.r = Rob.XYRobot("TPSD")
        
    def test_angle_rad(self):
        self.assertEqual(self.r.angle_rad(),0)
        
    def test_angle(self):
        self.r.turn_right()
        self.assertEqual(self.r.angle(),90)
        
    def test_move_forward(self):
        self.r.move_forward(50)
        self.assertAlmostEqual(self.r.position(),(50,0))
        
    def test_turn_right(self):
        self.r.turn_right()
        self.assertEqual(self.r.angle_rad(),pi/2)
        
    def test_str(self):
        self.r.move_forward(100)
        self.r.turn_right()
        self.r.move_backward(50)
        self.assertEqual(self.r.__str__(),"TPSD@(100,-50) angle: 90.0")
        
               
if __name__ == "__main__":
    unittest.main()