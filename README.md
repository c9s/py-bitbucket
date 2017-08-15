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
webhooks = bitbucket.hooks("foo", "reop")
```

```python
slack_webhook = 'https://hooks.slack.com/services/AAA/BBB/CCC';
ret = bitbucket.create_hook(user, repo,
        url = slack_webhook,
        description = 'Commits to Slack',
        events = ["repo:push"])
print("Created %s" % (ret['uuid']))
```

## Status

The implementation right now is really rough and tiny (it only supports 2 web hook API).

Pull requests are welcomed.


## License

MIT License


## Author

Yo-An Lin <yoanlin93@gmail.com>
