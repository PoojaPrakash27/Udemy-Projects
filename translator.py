from translate import Translator


try:
    with open('original.txt', mode='r') as fp:
        text = fp.read()
        translator = Translator(to_lang="ja")
        print(translator.translate(text))
except FileNotFoundError as e:
    print('Check your path!')
    raise err


##just adding some comments
##try again

##now this is after creating the littlefeature