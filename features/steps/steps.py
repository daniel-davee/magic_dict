from behave import *

from magic_dict import Magic_dict

@given(u'input to MagicDict is {input_} as {type_}')
def step_impl(context,input_,type_):
    context.input = eval(f'{type_}({input_})')
    context.magic_dict = Magic_dict(context.input)


@when(u'magic_dict is called')
def step_impl(context):
    context.res = context.magic_dict()


@then(u'the result is {res} as {type_}')
def step_impl(context,res,type_):
    assert context.res == eval(f'{type_}({res})')

@given(u'key is {key}')
def step_impl(context,key:str):
    context.key = key

@when(u'when key is assigned {assign} as {type_}')
def step_impl(context,assign,type_):
    if 'magic_dict' not in context.__dict__:
        context.magic_dict = Magic_dict()
    key = context.key
    try:
        context.magic_dict[key] == eval(f'{type_}({assign})')
        context.exe = None
    except Exception as e:
        context.exe = e

@then(u'a {error} is thrown with messge "{msg}"')
def step_impl(context,error,msg):
    print(context.exe,error)
    assert isinstance(context.exe,eval(error))
    assert context.exe.message == msg
