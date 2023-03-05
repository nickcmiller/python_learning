import requests
import secrets
import asyncio
import base64

API_BASE_URL = 'https://otter.ai/forward/api/v1'
CSRF_COOKIE_NAME = 'csrftoken'


print(secrets.USERNAME)

def getCookieValueAndHeader(cookieString, cookieName):
        """
        This function returns the value of a cookie in a cookie string
        and the full cookie header.
        """
    
        cookieValue = ''
        cookieHeader = ''
    
        # Split cookie string into separate cookies
        cookies = cookieString.split(';')
    
        # Find cookie with the specified name
        for cookie in cookies:
            if cookie.strip().startswith(cookieName):
                cookieValue = cookie.split('=')[1]
                cookieHeader = f"{cookieName}={cookieValue}"
                break
    
        return cookieValue, cookieHeader

class OtterApi:
    def __init__(self, options={}):
        self.options = options
        self.user = {}
        self.csrfToken = ''
        self.session = requests.Session() # create a session object

    async def init(self):
        await self._login()
    
    

    async def _login(self):
        email = self.options.get('email')
        password = self.options.get('password')
        
        if not email or not password:
            raise Exception("Email and/or password were not given. Can't perform authentication to otter.ai")
        
        csrf_response = requests.get(f'{API_BASE_URL}/login_csrf')
        csrf_token, csrf_cookie = getCookieValueAndHeader(csrf_response.headers['set-cookie'][0], CSRF_COOKIE_NAME)
        
        headers = {
            'authorization': 'Basic ' + base64.b64encode(f"{email}:{password}".encode()).decode(),
            'x-csrftoken': csrf_token,
            'cookie': csrf_cookie,
        }
        
        response = requests.get(
            f'{API_BASE_URL}/login',
            headers=headers,
            params={'username': email},
            cookies=csrf_response.cookies,
        )
        
        cookie_header = ';'.join(response.headers["set-cookie"].split(',')[:2])
        self.csrfToken = response.headers["set-cookie"].split('csrftoken=')[1].split(';')[0]
        self.user = response.json()['user']
        self.session.headers.update({'cookie': cookie_header})

        print('Successfully logged in to Otter.ai')
        return response

    async def getSpeeches(self):
        print(self)
        print(self.session.headers)
        
        print(self.user['id'])
        response = self.session.get(
            f'{API_BASE_URL}/speeches',
            params={'userid': self.user['id']}
        )
        print(response.request.headers)
        response.raise_for_status()
        speeches = response.json().get('speeches', [])
        return speeches

    async def getSpeech(self, speech_id):
        response = await axios({
            'method': 'GET',
            'url': f'{API_BASE_URL}/speech',
            'params': {
                'speech_id': speech_id,
                'userid': self.user['id']
            }
        })

        return response.data['speech']

    async def speechSearch(self, query):
        response = await axios({
            'method': 'GET',
            'url': f'{API_BASE_URL}/speech_search',
            'params': {
                'query': query,
                'userid': self.user['id']
            }
        })

        return response.data['hits']

    def validateUploadService(self):
        return axios({
            'method': 'OPTIONS',
            'url': f'{AWS_S3_URL}/speech-upload-prod',
            'headers': {
                'Accept': '*/*',
                'Access-Control-Request-Method': 'POST',
                'Origin': 'https://otter.ai',
                'Referer': 'https://otter.ai/'
            }
        })
    async def uploadSpeech(self, file):
        uploadOptionsResponse = await axios({
            'method': 'GET',
            'url': f'{API_BASE_URL}/speech_upload_params',
            'params': {
                'userid': self.user['id']
            },
            'headers': {
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Origin': 'https://otter.ai',
                'Referer': 'https://otter.ai/'
            }
        })
    
        del uploadOptionsResponse.data['data']['form_action']
    
        xmlResponse = await request.post(f'{AWS_S3_URL}/speech-upload-prod', data={
            **uploadOptionsResponse.data['data'],
            'file': file
        })
    
        result = self.parseXml(xmlResponse)
        Bucket = result['Bucket']
        Key = result['Key']
    
        finishResponse = await axios({
            'method': 'POST',
            'url': f'{API_BASE_URL}/finish_speech_upload',
            'params': {
                'bucket': Bucket,
                'key': Key,
                'language': 'en',
                'country': 'us',
                'userid': self.user['id']
            },
            'headers': {
                'x-csrftoken': self.csrfToken
            }
        })
    
        return finishResponse.json()

async def main():
    # Create an instance of OtterApi
    otter_api = OtterApi(options={
        'email': secrets.email,
        'password': secrets.password
    })

    # Call the init method to log in
    await otter_api.init()
    
    # Call getSpeeches
    speeches = await otter_api.getSpeeches()
    
    # Print the list of speeches
    # print(speeches)

if __name__ == '__main__':
    asyncio.run(main())