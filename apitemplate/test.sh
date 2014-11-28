#!/usr/bin/env bash

echo "(API) GET"
curl http://localhost:5000/api/rest/400/

echo "(API) Test PUT"
curl -H 'Content-Type: application/json' -X PUT http://localhost:5000/api/rest/400/ -d '{"username":"xyz","password":"xyz"}'

echo "(API) Test POST"
curl -H 'Content-Type: application/json' -X POST http://localhost:5000/api/rest/400/ -d '{"username":"xyz","password":"xyz"}'

echo "(UI) GET"
curl http://localhost:5000/ui/300/

echo "(UI) GET w/QS arg"
curl http://localhost:5000/ui/300/?qsarg=qqq
