---
template: overrides/main.html
---

# Variant query service

Welcome to the NGeneBio API! You can use our API to access NGeneBio API endpoints,
which can get information on various database query results.

This page describes the reference for variant query web service. 
It’s also recommended to try it live on our [interactive API page].

  [interactive API page]: http://192.168.1.14:9000/


## Service endpoint

  ``` GET httpe://example.com/hg19/all-database ```

## Authentication

Kitten expects for the API key to be included in all API requests to the server
in a header that look like the following: `Authorization: meowmeowmeow`

!!! info "You must replace meowmeowmeow with your personal API key."

  [developer portal]: http://example.com/developers

To authorize, use this code:

=== "shell"

    ``` sh
    # With shell, you can just pass the correct header with each request
    curl "api_endpoint_here" \
    -H "Authorization: meowmeowmeow"
    ```

=== "python"

    ``` python
    import kittn

    api = kittn.authorize('meowmeowmeow') 
    ```

Make sure to replace meowmeowmeow with your API key.

## Query parameters

| Parameter        | Required       | Type     | Description                                                                    |
| :--------------- | :--------------| :------- | :----------------------------------------------------------------------------- |
| hgvsg            | true           | String   | HGVS.g nomemclature   ex) chr17:g.41244936G>A                                  |

The above command returns JSON structred like this:

## Query syntax

## Returned object

=== "Example"

    ``` json

    {
      "hg19Chr": "chr17",
      "hg19Pos": 41244936,
      "hg38Chr": null,
      "hg38Pos": null,
      "ref": "G",
      "alt": "A",
      "cytoBand": "17q21.31",
      "hg19Key": "chr17:g.41244936G>A",
      "hg38Key": null,
    }
    ```