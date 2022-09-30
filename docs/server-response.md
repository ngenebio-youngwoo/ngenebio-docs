---
template: overrides/main.html
---

# Server response

The MyVariant.info server returns a variety of query responses, and response status codes. They are listed here.

!!! info "Note"

    These examples show query responses using the python requests package.

## Status code 200

A `200` status code indicates a successful query, and is accompanied by the query response payload.

## Status code 400

A `400` status code indicates an improperly formed query, and is accompanied by a response payload describing the source of ther error.

## Status code 404

A `404` status code indicates either an unrecognized URL, as in (/query is misspelled /query resulting in an unrecognized URL):

## Status code 5xx

Any `5xx` statyus codes are the result of uncaught query errors.