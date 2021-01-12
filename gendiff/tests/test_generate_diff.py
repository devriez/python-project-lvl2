from gendiff.scripts.generate_diff import generate_diff

def test_generate_diff():
    given_result = '''{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22
  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'''
    result = generate_diff('gendiff/tests/fixtures/file1.json',
                           'gendiff/tests/fixtures/file2.json')
    print('given_result', given_result)
    print('result', result)
    assert result == given_result
