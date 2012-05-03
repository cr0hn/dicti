dicti
=======
`dicti` is a dictionary with case-insensitive keys.

It works like the normal `dict` except that key matching
is case-insensitive.

### Installing

    pip install dicti

### Creating
Import `dicti`.

    from dicti import dicti

Then instantiate `dicti` like you would a normal dict;
for example, these work.

    dict(foo = 'bar', answer = 42)
    dicti(foo = 'bar', answer = 42)
    
    dict({'foo': 'bar', 'answer': 42})
    dicti({'foo': 'bar', 'answer': 42})

### Retrieving keys
You can retrieve an item with a case-insensitive match.

    di = dicti()
    di['cAsE'] = 1
    di['case'] == di['CASE']

Methods that record keys record the original case,
just as a normal dictionary does.

    di = dicti()
    di['cAsE'] = 1
    di.keys() == ['cAsE']
    di['Case'] = 1
    di.keys() == ['Case']
    di['caSE'] == 1

Keys are still stored in their original case, however;
the original keys are presented when you request them
with methods like `dicti.keys`.
