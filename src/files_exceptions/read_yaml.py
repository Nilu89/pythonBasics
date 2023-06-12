import yaml


config_file = "../../data/config.yaml"
with open('config_file') as file:
    credentials = yaml.safe_load(file)

print(credentials)
uname = credentials['username']
pword = credentials['password']
url = credentials['host']

print(f'Open the website: {url}')
print(f'Enter the user name: {uname}')
print(f'Enter the password: {pword}')
print(f'Click on Login button')
print('......')
print(f"Main page opened!!!")


