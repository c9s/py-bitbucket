import requests
import socketserver
import webbrowser
from threading import Event
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler

redirect_uri = callback_baseurl + "/cb"

callback_baseurl = 'http://localhost:8181'
callback_baseurl = 'http://127.0.0.1:' + str(callback_port)

callback_port = 8810

redirect_path = None

"""
def main():
    if os.path.exists(".access_token"):
        token = pickle.load(open(".access_token", 'rb'))
        bitbucket = BitBucketClient(client_key,
                client_secret=client_secret,
                resource_owner_key=token['oauth_token'],
                resource_owner_secret=token['oauth_token_secret'])
    else:
        bitbucket = BitBucketClient(client_key, client_secret=client_secret)
        token = bitbucket.login()
        pickle.dump(token, open(".access_token", 'wb'))
        print(token)
"""

class CallbackRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()


        global redirect_path
        redirect_path = self.path
        print("Received redirect_path", self.path)

        # Send message back to client
        message = "<html><body>\
        Success!\
        <script>\
        setTimeout(function() {\
            window.close();\
        }, 2000);\
        </script></body></html>"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

class BitBucketOAuth1Client:

    # request_token_url = 'https://bitbucket.org/!api/1.0/oauth/request_token'
    # authorization_base_url = 'https://bitbucket.org/!api/1.0/oauth/authenticate'
    # access_token_url = 'https://bitbucket.org/!api/1.0/oauth/access_token'

    def __init__(self,client_key,
            client_secret,
            resource_owner_key = None,
            resource_owner_secret = None):

        callback_uri = callback_baseurl + '/cb'
        client = BackendApplicationClient(client_id=client_id)
        self.client = OAuth2Session(client=client, redirect_uri=callback_uri, token=resource_owner_key)

        """
        self.client = OAuth1Session(client_key,
                client_secret=client_secret,
                resource_owner_key=resource_owner_key,
                resource_owner_secret=resource_owner_secret,
                callback_uri=callback_uri)
        """

    def login(self):
        self.client.fetch_request_token(request_token_url)

        # 3. Redirect user to Bitbucket for authorization
        authorization_url = self.client.authorization_url(authorization_base_url)

        print("Please go here and authorize:\n%s" % authorization_url)

        with socketserver.TCPServer(("", callback_port), CallbackRequestHandler) as httpd:
            print('Waiting for callback at', callback_port, '...')
            webbrowser.open(authorization_url)
            httpd.handle_request()
            req = httpd.get_request()
            print(req)

        # 4. Get the authorization verifier code from the callback url
        # redirect_response = input('Paste the full redirect URL here:')
        global redirect_path
        redirect_response = callback_baseurl + redirect_path
        # redirect_response = req.path
        self.client.parse_authorization_response(redirect_response)

        # 5. Fetch the access token
        return self.client.fetch_access_token(access_token_url)

    def hooks(self, user, repo):
        resp = self.client.get('https://api.bitbucket.org/2.0/repositories/%s/%s/hooks' % (user, repo))
        resp_data = json.loads(resp.content)
        return resp_data['values']

    def create_hook(self, user, repo, url, description, events):
        resp = self.client.post('https://api.bitbucket.org/2.0/repositories/%s/%s/hooks' % (user, repo), data = json.dumps({
            "url": url,
            "description": description,
            "active": True,
            "events": events
        }))
        print(resp.content)
        return resp

