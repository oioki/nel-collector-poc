#!/usr/bin/env python3

from flask import Flask, request, make_response
import sentry_sdk


app = Flask(__name__)

sentry_sdk.init()


@app.route('/', methods = ['OPTIONS', 'POST'])
def home():
    if request.method == "OPTIONS":
        resp = make_response('ok', 200)
        resp.headers["Access-Control-Allow-Headers"] = "accept, x-requested-with, content-type"
        resp.headers["Access-Control-Allow-Methods"] = "post"
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp

    for payload in request.json:
        with sentry_sdk.push_scope() as scope:
            for field in ["age", "type", "url", "user_agent"]:
                if field in payload:
                    scope.set_tag(field, payload[field])
            if 'body' in payload:
                for field in payload['body']:
                    scope.set_tag(field, payload['body'][field])

            message = payload['type'] + ' / ' + payload['body']['type']
            scope.set_extra("your_advertisement", "vote for NEL project on Hackweek awards")
            sentry_sdk.capture_message(message)

    resp = make_response('ok', 200)
    return resp


if __name__ == '__main__':
    app.run(host='127.0.0.8', port=8000, threaded=True)

