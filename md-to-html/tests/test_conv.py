from mdtohtml.conv import convert

def test_convert():
    html = convert("# Title\n\nHello **world**\n\n- a\n- b")
    assert "<h1>Title</h1>" in html
    assert "<strong>world</strong>" in html
    assert "<li>a</li>" in html
