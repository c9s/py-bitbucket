# BitBucket Client

This BitBucket client library is written in Python.

## Install

    python setup.py install

## Usage

Create your own OAuth consumer app at `https://bitbucket.org/account/user/{YOUR_ID}/api`

Since this package uses OAuth2 API, please remember to setup the callback url.
(`http://localhost` is fine)
    
```python
bitbucket = BitBucketClient(client_id, client_secret=client_secret, token=token, scope=scope)
webhooks = bitbucket.hooks("foo", "reop")
```
