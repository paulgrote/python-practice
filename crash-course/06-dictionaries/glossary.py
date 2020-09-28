# 6-3, 6-4
glossary = {
    "expression":"A piece of syntax which can be evaluated to some value.",
    "statement":"Either an expression or one of several constructs with a keyword, such as if, while, or for.",
    "method":"A function which is defined inside a class body.",
    "function":"A series of statements which returns some value to the caller.",
    "argument":"A value passed to a function or method when calling the function.",
}

for word, definition in glossary.items():
    print("{}:\n\t{}".format(word, definition))
