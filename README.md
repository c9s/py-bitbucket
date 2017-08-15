# BitBucket Client

This BitBucket client library is written in Python.

## Install

    python setup.py install

## Usage
    
```python
bitbucket = BitBucketClient(client_id, client_secret=client_secret, token=token, scope=scope)
webhooks = bitbucket.hooks("foo", "reop")
```
