from gendiff.scripts.generate_diff import generate_diff


def test_generate_diff():
    f = open('gendiff/tests/fixtures/result_gendiff.txt')
    result = f.read()
    print('result', result)
    result_json = generate_diff('gendiff/tests/fixtures/file1.json',
                                'gendiff/tests/fixtures/file2.json')
    print('result_json', result_json)

    assert result_json == result

    result_yml = generate_diff('gendiff/tests/fixtures/file1.yml',
                               'gendiff/tests/fixtures/file2.yml')
    print('result_yml', result_yml)
    assert result_yml == result
