from json import JSONDecodeError
import requests
import json

def fetch_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Extract json from the response
        json_str = response.text.strip()[4:-2] # Remove "res (" and " ); "
        data = json.loads(json_str)
        return data

    except requests.exceptions.RequestException as e:
        print(f"(Request error: {e} )")
    except JSONDecodeError as e:
        print(f"(json decoding error: {e} )")

def main():
    URL = "https://www.nogizaka46.com/s/n46/api/list/member"
    data = fetch_json(URL)
    print(data)


if __name__ == '__main__':
    main()