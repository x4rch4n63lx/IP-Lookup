# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 6/3/2019 - 1:00PM
# Script Purpose : IP Lookup Tool coded in Python
# Description    : This script performs IP address lookups, providing essential details:
#                  1. Displays continent.
#                  2. Displays country.
#                  3. Displays region.
#                  4. Displays city.
#                  5. Displays ISP.
# Features       :
#                  - IP address lookup.
#                  - Clear display of IP information.
# Requirements   :
#                  - Install the requests library using: pip install requests
# ===================================================================================
import requests

def lookup_ip():
    ip_address = input("Please enter the IP address you would like to look up: ")
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}?fields=continent,country,regionName,city,isp,status,message').json()
        
        if response['status'] == 'fail':
            print(f"Error: {response['message']}")
            return
        
        print(f"\nResults for IP: {ip_address}")
        print(f"{'Continent:':<15} {response['continent']}")
        print(f"{'Country:':<15} {response['country']}")
        print(f"{'Region:':<15} {response['regionName']}")
        print(f"{'City:':<15} {response['city']}")
        print(f"{'ISP:':<15} {response['isp']}")
        
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def main():
    while True:
        lookup_ip()
        choice = input("\nType 'exit' to close the tool: ")
        if choice.lower() == 'exit':
            break

if __name__ == "__main__":
    main()
