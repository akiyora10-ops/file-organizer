from password_generator.generator import generate, strength, entropy_bits

def test_generate_length():
    ps = generate(20, count=3)
    assert len(ps) == 3
    assert all(len(p) == 20 for p in ps)

def test_strength():
    assert strength("abc") == "weak"
    assert entropy_bits("Aa1!") > 0
