from scripting import status, success, error


def test_utf8_encoding():
    status('hi')
    success('yay!')
    error('boo!')
