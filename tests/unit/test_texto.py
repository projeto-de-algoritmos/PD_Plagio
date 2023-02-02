#alinhamento de sequencia
import sys 
sys.path.append("src/")

from controller.texto import TextoController

import unittest

class TestSequenceAlingment(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = TextoController() 

    def test_full_match(self):
        expect_match = 100.0
        str1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum purus velit, vehicula a convallis sed, tempus vitae massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus aliquet ex nec metus viverra elementum. Sed feugiat massa ut eros cursus euismod vel semper lectus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent luctus auctor ligula, rhoncus bibendum est semper non. Morbi ut accumsan nisi. Sed varius sem a velit facilisis, et sollicitudin mi luctus. Quisque non ex nunc. Nam dapibus sem in scelerisque viverra. Nullam eget leo quam. Vestibulum porttitor, enim eu euismod blandit, sem nunc dignissim leo, a egestas ante tellus eget orci. Donec consequat, neque in fringilla ornare, enim erat tincidunt velit, a rhoncus ipsum nunc convallis sem. Nullam fringilla aliquam purus, quis consectetur ligula pellentesque in. Nunc in libero vitae dolor facilisis posuere."
        str2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum purus velit, vehicula a convallis sed, tempus vitae massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus aliquet ex nec metus viverra elementum. Sed feugiat massa ut eros cursus euismod vel semper lectus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent luctus auctor ligula, rhoncus bibendum est semper non. Morbi ut accumsan nisi. Sed varius sem a velit facilisis, et sollicitudin mi luctus. Quisque non ex nunc. Nam dapibus sem in scelerisque viverra. Nullam eget leo quam. Vestibulum porttitor, enim eu euismod blandit, sem nunc dignissim leo, a egestas ante tellus eget orci. Donec consequat, neque in fringilla ornare, enim erat tincidunt velit, a rhoncus ipsum nunc convallis sem. Nullam fringilla aliquam purus, quis consectetur ligula pellentesque in. Nunc in libero vitae dolor facilisis posuere."
        match_received = self.controller.compara_str(str1, str2)
        self.assertEqual(expect_match, match_received)
    
    def test_no_match(self):
        expect_match = 0.0
        str1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum purus velit, vehicula a convallis sed, tempus vitae massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus aliquet ex nec metus viverra elementum. Sed feugiat massa ut eros cursus euismod vel semper lectus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent luctus auctor ligula, rhoncus bibendum est semper non. Morbi ut accumsan nisi. Sed varius sem a velit facilisis, et sollicitudin mi luctus. Quisque non ex nunc. Nam dapibus sem in scelerisque viverra. Nullam eget leo quam. Vestibulum porttitor, enim eu euismod blandit, sem nunc dignissim leo, a egestas ante tellus eget orci. Donec consequat, neque in fringilla ornare, enim erat tincidunt velit, a rhoncus ipsum nunc convallis sem. Nullam fringilla aliquam purus, quis consectetur ligula pellentesque in. Nunc in libero vitae dolor facilisis posuere."
        str2 = "ZZZZZZZZZZZZZZZ"
        match_received = self.controller.compara_str(str1, str2)
        self.assertEqual(expect_match, match_received)

    def test_float_match(self):
        expect_match = 13.4
        str1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum purus velit, vehicula a convallis sed, tempus vitae massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus aliquet ex nec metus viverra elementum. Sed feugiat massa ut eros cursus euismod vel semper lectus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent luctus auctor ligula, rhoncus bibendum est semper non. Morbi ut accumsan nisi. Sed varius sem a velit facilisis, et sollicitudin mi luctus. Quisque non ex nunc. Nam dapibus sem in scelerisque viverra. Nullam eget leo quam. Vestibulum porttitor, enim eu euismod blandit, sem nunc dignissim leo, a egestas ante tellus eget orci. Donec consequat, neque in fringilla ornare, enim erat tincidunt velit, a rhoncus ipsum nunc convallis sem. Nullam fringilla aliquam purus, quis consectetur ligula pellentesque in. Nunc in libero vitae dolor facilisis posuere."
        str2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum purus velit, vehicula a convallis sed, tempus vitae massa."
        match_received = self.controller.compara_str(str1, str2)
        self.assertEqual(expect_match, match_received)
        