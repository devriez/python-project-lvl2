from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json_render import json_render

formaters = {
    'stylish': stylish,
    'plain': plain,
    'json': json_render
}

def select_formater(name):
    return formaters[name]
