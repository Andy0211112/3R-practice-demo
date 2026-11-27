import pytest

from practice_demo.practice_demo import hello_world, prime_factorize

@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("testing", "Hello world!: testing"),
        ("123", "Hello world!: 123"),
    ],
)
def test_hello_world(test_input, expected):
    assert hello_world(test_input) == expected

@pytest.mark.parametrize(
    "n, expected",
    [(2, [2]), (12, [2, 2, 3]), (97, [97]), (360, [2, 2, 2, 3, 3, 5])],
)
def test_prime_factorize(n, expected):
    assert prime_factorize(n) == expected


def test_prime_factorize_invalid():
    with pytest.raises(ValueError):
        prime_factorize(1)