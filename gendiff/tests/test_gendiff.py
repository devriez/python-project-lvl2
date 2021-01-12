from gendiff.scripts.gendiff import generate_diff

def test_generate_diff():
    given_result = '''{
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
  }'''
    result = generate_diff('gendiff/tests/fixtures/file1.json',
                           'gendiff/tests/fixtures/file2.json')
    assert result == given_result