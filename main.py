# -*- coding: utf-8 -*-
import sys
import json
import base64
from googletrans import Translator

try:
    g = Translator()
    args = json.loads(base64.b64decode(sys.argv[1]))
    if 'text' not in args or 'des' not in args:
        raise ValueError('Input mismatch')
    if 'src' not in args:
        args['src'] = 'auto'
    translated = g.translate(args['text'], args['des'], args['src'])
    if translated:
        print(json.dumps({'result': 200, 'response': translated.text}))
except:
    print(json.dumps({'result': 400}))
