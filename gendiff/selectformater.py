from gendiff.formaters.stylish_render import stylish_render
from gendiff.formaters.plain_render import plain_render
from gendiff.formaters.json_render import json_render

formaters = {
    'stylish': stylish_render,
    'plain': plain_render,
    'json': json_render
}


def select_formater(name):
    return formaters[name]
