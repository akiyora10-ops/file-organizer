import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_snake_camel():
    assert main.to_snake("HelloWorld") == "hello_world"
    assert main.to_camel("hello_world") == "helloWorld"
    assert main.to_kebab("Hello World") == "hello-world"

def test_converters():
    assert main.CONVERTERS["upper"]("abc") == "ABC"
