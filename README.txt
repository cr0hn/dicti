dicti
=======
`dicti` is a dictionary with case-insensitive keys.

It works like the normal `dict` except that key matching
is case-insensitive.

Instantiate like you would instantiate a normal dict;
for example, these work.

    dict(foo = 'bar', answer = 42)
    dicti(foo = 'bar', answer = 42)
    
    dict({'foo': 'bar', 'answer': 42})
    dicti({'foo': 'bar', 'answer': 42})

Methods that accept keys and have side-effects record
the original case, just as a normal dictionary does.

    di = dicti()
    di['cAsE'] = 1
    di.keys() == ['cAsE']
    di['Case'] = 1
    di.keys() == ['Case']
    di['caSE'] == 1

Methods that accept keys do the same thing regardless
of what case you pass the key in.

Keys are still stored in their original case, however;
the original keys are presented when you request them
with methods like `dicti.keys`.
