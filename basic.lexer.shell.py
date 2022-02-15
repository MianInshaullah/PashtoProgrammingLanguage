import simplelexer

while True:
    text = input('simple lexer > ')
    result, error = simplelexer.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)