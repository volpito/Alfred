import requests
from requests.auth import HTTPBasicAuth

class WeatherRequest:
    def Get_posts(self):
        self.city = input("What city do you want to know the weather of ?\n-> ").strip().capitalize()
        key = 'c91d3fdea9f3478989a92153211810'
        url = 'http://api.weatherapi.com/v1'
        headers = {'Accept': 'application/json'}
        auth = HTTPBasicAuth('apikey', key)
        #files = {'file': open('filename', 'rb')}

        try:
            response = requests.get(f"{url}/current.json?key={key}&q={self.city}", headers=headers, auth=auth)#, files=files)

            if response.status_code == 200:
                posts = response.json()
                return posts
            else:
                print('Error :', response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print('Error :', e)
            return None

    def Run(self):
        posts = self.Get_posts()

        if posts:
            print(f"In {posts['location']['country']}, {posts['location']['name']}'s temp in C is :", posts['current']['temp_c'])
            print('Should feel like :', posts['current']['feelslike_c'], "with", posts['current']['condition']['text'].casefold(), "skies.")
        else:
            print('Failed to fetch posts from API.\nCity name might be wrong')

if __name__ == '__main__':
    WeatherRequest().Run()