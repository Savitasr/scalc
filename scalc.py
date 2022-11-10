import json
#from hello_world import app
import unittest


def lambda_handler(event, context):
    n1=event["n1"]
    n2=event["n2"]

    print(add(n1,n2))
    print(sub(n1,n2))
    print(mul(n1,n2))
    print(div(n1,n2))

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return abs(n1-n2)
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return abs(n1/n2)

class calculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5,3),8)
    def test_sub(self):
        self.assertEqual(sub(5,3),2)
    def test_mul(self):
        self.assertEqual(mul(5,3),15)
    def test_div(self):
        self.assertEqual(div(4,2),2)

if __name__ == '__main__':
    unittest.main()