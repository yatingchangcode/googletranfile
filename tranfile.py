#import googletrans
import argparse                                                        
from googletrans import Translator
import yaml

def get_config(yamlConfigFile):
    with open(yamlConfigFile) as file:
        config = yaml.safe_load(file)
        return config

def main():
    config = get_config("trans.conf")                         
    src_lang = config['source_lang']
    dst_lang = config['dest_lang']

    translator = Translator()
    f = open('original.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        #print(contents)

    result = translator.translate(contents, src=src_lang, dest=dst_lang)
    #print(result.text)
    
    out = open("result.txt", "w")
    out.write(result.text)

    



if __name__ == '__main__':
    main()
