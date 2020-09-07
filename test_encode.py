#import pytest
from .encode import encode, decode

def test_encode():
	assert encode('this is a message') == 'th3s 3s 1 m2ss1g2', \
		"encoding valid string failed"
	
def test_encode_none():
	assert encode(None) == None,"encoding of None failed" 

def test_decode():
	assert decode('th3s 3s 1 m2ss1g2') == 'this is a message', \
		"decoding valid string failed"

def test_decode_none():
	assert decode(None) == None,"encoding of None failed" 
