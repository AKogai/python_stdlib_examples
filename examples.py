import string

"""
1.1 string.functions.capwords
"""
def example_string():
    s = 'one two three'
    print(s)
    print(string.capwords(s))

"""
1.2 string.templates 
"""
def example_templates():
    values = {'var': 'foo'}
    t = string.Template("""
    Variable        :$var
    Escape          :$$
    Variable in text:${var}iable
    """)
    print('TEMPLATE:', t.substitute(values))

    s = """
    Variable        : %(var)s
    Escape          : %%
    Variable in text: %(var)siable
    """
    print('INTERPOLATION:', s % values)

    s = """
    Variable: {var}
    Escape: {{}}
    Variable in text: {var}iable
    """
    print('FORMAT:', s.format(**values))

    t = string.Template("$var is here but $missing is not provided")
    try:
        print('substitute() :', t.substitute(values))
    except KeyError as err:
        print('ERROR:', str(err))
    print('safe_substite():', t.safe_substitute(values))


if __name__ == "__main__":
    print('1.1 string - перевели все первые буквы в верхний регистр')
    example_string()
    print('1.2 форматирование строки через шаблон, %, str.format()')
    example_templates()
