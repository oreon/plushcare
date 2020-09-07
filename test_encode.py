#import pytest
from .encode import encode

def test_file1_method1():
	assert encode('this is a message') == 'th3s 3s 1 m2ss1g2', \
		"encoding regular string failed"
	
def test_file1_method2():
	assert encode(None) == None,"encoding of None failed" 