#!/usr/bin/env python

import sys
import openai
import argparse

from datetime import datetime


def access_key():
    with open("key.txt") as key:  
        key = key.read()
    return key

def writefile(msg):
    with open("chat.log", "a+", encoding='utf-8') as log:
        log.writelines(msg)

def gpt35Turbo(prompt):
    
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": prompt}
      ],
      temperature=0.7 # 0-strict ; 1-creative
    )

    res = " [gpt35Turbo]$ " + completion.choices[0].message["content"]
    return res


def main():
    
    if len(sys.argv) == 1:
        print("You must provide an argument.")
        sys.exit(1)
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('prompt', help='Text prompt')
        args = parser.parse_args()

        now = datetime.now()
        msg = "\n\n" + str(now) + " [Me]$ " + args.prompt
        writefile(msg)
        print(msg)

        openai.api_key = access_key()
        response = gpt35Turbo(args.prompt)

        now = datetime.now()
        msg = "\n" + str(now) + response
        writefile(msg)
        print(msg)


if __name__ == '__main__':
    main()


