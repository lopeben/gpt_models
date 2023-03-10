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

def davinci(prompt):
    
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.5, # 0-strict ; 1-creative
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    res = " [DaVinci003]$ " + response["choices"][0]["text"]

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
        response = davinci(args.prompt)

        now = datetime.now()
        msg = "\n" + str(now) + response
        writefile(msg)
        print(msg)

if __name__ == '__main__':
    main()