import pytest
import hypot_vb.source as hypot
#test sqrt function
def test_sqrt():
    input = 4
    e_output = 2.0
    output = hypot.sqrt(input)
    assert output == e_output
    
def test_abs():
    input = -9
    e_output = 9
    output = hypot.abs(input)
    assert output == e_output
    
def test_hypot():
    input1= 3
    input2= 4
    e_output = 5
    output = hypot.hypot(input1, input2)
    assert output == e_output
    
#test hypot function