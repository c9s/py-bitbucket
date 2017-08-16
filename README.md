# BitBucket Client

This BitBucket client library is written in Python.

## Install

    python setup.py install

## Usage

Create your own OAuth consumer app at `https://bitbucket.org/account/user/{YOUR_ID}/api`

Since this package uses OAuth2 API, please remember to setup the callback url.
(`http://localhost` is fine)
    
```python
scope = ["webhook", "repository", "issue", "pullrequest"]
bitbucket = BitBucketClient(client_id, client_secret=client_secret, scope=scope)
```

The bitbucket package uses `requests_oauthlib` as its core library for sending
API requests, therefore you can also pass your preferred client object to the
bitbucket client class:

```python
client = BackendApplicationClient(client_id=client_id)
bitbucket = BitBucketClient(client=client, client_id=client_id, client_secret=client_secret, scope=scope)
```

### Listing web hooks

```python
webhooks = bitbucket.hooks("foo", "reop")
```

### Creating new web hook

```python
slack_webhook = 'https://hooks.slack.com/services/AAA/BBB/CCC';
ret = bitbucket.create_hook(user, repo,
        url = slack_webhook,
        description = 'Commits to Slack',
        events = ["repo:push"])
print("Created %s" % (ret['uuid']))
```


## Command line script

```
bitbucket webhook list --user c9s --repo foo
```

## Status

The implementation right now is really rough and tiny (it only supports 2 web hook API).

Pull requests are welcomed.


## License

MIT License


## Author

Yo-An Lin <yoanlin93@gmail.com>
