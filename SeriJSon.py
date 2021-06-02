import json

accounts_dict = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', 'balance': 345.67}
]}

# Serializing an Object to JSON
with open('accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)

# Deserializing the JSON Text
with open('accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)

print(accounts_json)

print()

print(accounts_json['accounts'])

print()

print(accounts_json['accounts'][0])

print()

with open('accounts.json', 'r') as accounts:
    print(json.dumps(json.load(accounts), indent=4))

    