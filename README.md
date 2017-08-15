# BitBucket Client

## Install

    python setup.py install

## Usage
    
    bitbucket = BitBucketClient(client_id, client_secret=client_secret, token=token, scope=scope)
    webhooks = bitbucket.hooks("foo", "reop")
