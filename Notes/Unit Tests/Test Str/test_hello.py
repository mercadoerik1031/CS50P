from hello import hello

def test_hello():
    hello() == "hello, world"


def test_argument():
    for name in [Erik, Jose, Joe]:
        assert hello(name) == f"hello, {name}"