from behave import *
from magic_dict import Magic_dict
from typing import Any
import logging
import sys

def yes_or_no(question:str, answer:bool):
    return question + '\n' + ('yes' if answer else 'no')
    
def value_as_type(value,type_):
    return eval(type_)(value)

@given(u'foo is testing Magic_dict')
def step_impl(context):
    context.name = 'foo'
    context.create = Magic_dict

@given(u'log level is set to {level}')
def step_impl(context,level):
    """[sets the log level]

    Args:
        context ([type]): [description]
        level ([type]): [description]
    """
    log_level = logging.DEBUG if level.lower() == 'debug' else \
                logging.INFO
    handlers=[logging.FileHandler("debug.log"),logging.StreamHandler(sys.stdout)]
    logging.basicConfig(handlers=handlers)
    logging.getLogger().setLevel(log_level)
    logging.debug(f'what is log level:{logging.getLevelName(logging.root.getEffectiveLevel())}')

@given(u'foo is created')
def step_impl(context):
    _input = context.input if hasattr(context,'input') else None
    context.foo = context.create(_input) if _input else context.create()
    


@then(u'{obj} is isinstance of Magic_dict')
def step_impl(context, obj:Any):
    """
    foo needs to be an instance of Magic_dict
    """
    obj = getattr(context,obj)
    assert isinstance(obj, Magic_dict), step_impl.__doc__

@when(u'foo exist')
def step_impl(context):
    """ {yes_or_no('Does foo exist?', context.foo)}
        What is context?{context=}
        yes_or_no('context has foo',hasattr(context,'foo'))
        """
        
    assert context.foo, eval("f'{}'".format(step_impl.__doc__))
    context.result = bool(context.foo)


@then(u'result is {value} as {type_}')
def step_impl(context,value,type_):
    """{context.result=} is {value=} as {type_}"""
    value = value_as_type(value, type_)
    msg = f"""{context.result=} is {value=} as {type_}
                what is context?
                {dir(context)=}
                what is {value=} as {type_=}?
                {value_as_type(value,type_)} as type {type(value)}
                what is result?
                {context.result=}
                {yes_or_no('is result the same as value, check type again?', context.result == value)}"""
    assert context.result == value, msg
    
@given(u'foo.{key} = {value} as {type_}')
def step_impl(context, key, value, type_):
    """foo.key ={value=} as {type_}"""
    value = value_as_type(value,type_)
    setattr(context.foo,key,value)


@when(u'result is foo["{key}"]')
def step_impl(context,key):
    """[trying to get {key=} out of foo
        {yes_or_no('Does foo exist?',context.foo)}
        {yes_or_no(f'is {key=} in foo',key in context.foo)}]
    """
    context.result = context.foo[key]


@given(u'foo["{key}"] = {value} as {type_}')
def step_impl(context, key, value, type_):
    """[given foo[{key=}] = {value=} as {type_=}]

    Args:
        context ([context]): [context I don't know ask behave?]
        key ([str probably]): [key being set]
        value ([any]): [the object]
        type_ ([type]): [gives the type for behave to check]
    """
    value = value_as_type(value,type_) 
    context.foo[key] = value
    questions = f"""given foo[{key=}] = {value=} as {type_=}
                    what context.foo[key]?\n{context.foo[key]=}
                    what context.foo.key?\n{getattr(context.foo,key)=}
                    what context.foo.key?\n{ context.foo.bar =}
                    what is type of value?\n{type(value)=}"""
    logging.debug(questions)

@given(u'{key} not in foo')
def step_impl(context,key:str):
    """[{key} not in foo]
    """
    msg = f"""
            What is key?
            {key=}
            whats dir context?
            {dir(context)=}
            {yes_or_no('does contex have foo', hasattr(context,'foo'))}
            {yes_or_no('is key in foo?',key in context.foo)}"""
    assert key not in context.foo, msg

@when(u'result is foo.{key}')
def step_impl(context,key):
    context.result = getattr(context.foo,key)