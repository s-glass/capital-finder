from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # parse the query from path
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # response code
        self.send_response(200)

        # headers
        self.headers.add_header("Content-type", "text/plain")
        self.end_headers()

        country = dic.get('country')
        capital = dic.get('capital')

        if country:
            url = "https://restcountries.com/v3.1/name"
            country_response = requests.get(url + country)
            country_data = country_response.json()
            capital_message = country_data[0]['capital'][0]
            output_capital = str(f'The capital of {country} is {capital_message}')
            display_capital_message = str(output_capital)
            self.wfile.write(display_capital_message.encode())
            return
        
        elif capital:
            url ='https://restcountries.com/v3.1/capital'
            capital_response = requests.get(url + capital)
            capital_data = capital_response.json()
            country_message = capital_data[0]['name']['common']
            output_country = str(f'{capital} is the capital of {country_message}')
            display_country_message = str{output_country}
            self.wfile.write(display_country_message.encode())
            return