import nose
from sample_class import DemoClass

class TestDemo(object):
    
    def setUp(self):
        self.auto_demo = DemoClass()
    
    def tearDown(self):
        pass
    
    def test_case1(self):
        ret_str = self.auto_demo.returnString()
        print ret_str
        pass
    
    def test_case2(self):
        ret_num = self.auto_demo.returnNumber()
        print ret_num
        pass
        
        
        
        
        
