# Code in python that decides randomly, whether an account needs to be created, 
# or credit/debit operation needs to be performed.
# Based on the choice, create an appropriate KafkaProducer that writes the data to the specifed topic and close it gracefully.

from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime
import string


from faker import Faker


options = ["Create", "Debit", "Credit"]
transactions = []

# Calculate the number of occurrences for each option based on probabilities
total_outcomes = 50
create_count = int(total_outcomes * 0.1)
debit_count = credit_count = int(total_outcomes * 0.45)

# Add elements to the outcomes list with the desired probabilities

transactions = ["Create"] * create_count + ["Debit"] * debit_count + ["Credit"] * credit_count
print(transactions)

# Shuffle the outcomes list to randomize the order
random.shuffle(transactions)
ACC_NO_FILENAME = "account_numbers.txt"
print(transactions)
for transaction in transactions:
    if transaction in ["Debit", "Credit"]:
        try:
            acc_nos = retrieve_strings_from_file(ACC_NO_FILENAME)
        except:
            acc_nos = []
            continue
        transaction = debitCreditProducerSimulation(random.choice(acc_nos), transaction)
    else:
        newCustomer = newCustProducerSimulation()
        acc = newCustomer['account_number']
        try:
            acc_nos = retrieve_strings_from_file(ACC_NO_FILENAME)
        except:
            acc_nos = []
        acc_nos.append(acc)
        save_strings_to_file(acc_nos, ACC_NO_FILENAME)
        



def save_strings_to_file(strings, filename):
    with open(filename, 'w') as file:
        for string in strings:
            file.write(string + '\n')

def retrieve_strings_from_file(filename):
    strings = []
    with open(filename, 'r') as file:
        for line in file:
            strings.append(line.strip())
    return strings

def debitCreditProducerSimulation(account_number, transaction_type):
    balance = getBalance(account_number)
    transaction_amount = round(random.uniform(1, balance), 2)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        "account_number": account_number,
        "transaction_type": transaction_type,
        "transaction_amount": transaction_amount,
        "timestamp": timestamp
    }
    pass


    



def newCustProducerSimulation():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    timestamp = datetime.now()
    account_creation_date = datetime.now().strftime('%Y-%m-%d')
    account_number = timestamp.strftime('%d%m%Y%H%M%S%f')   # Includes miliseconds too
    gender = random.choice('MF')
    dateofbirth = str(random.choice(list(range(1, 31)))) + '-'\
        + str(random.choice(list(range(1, 13)))) + '-'\
        + str(random.choice(list(range(1960, 2010))))
    
    bloodgroup = random.choice(['O', 'A', 'B', 'AB']) + random.choice(['+', '-'])
    aadhaar = ''.join([random.choice(string.digits) for _ in range(12)])
    pan = ''.join([random.choice(string.ascii_uppercase) for _ in range(5)])\
        + ''.join([random.choice(string.digits) for _ in range(4)])\
        + random.choice(string.ascii_uppercase)

    balance = 0
    newCust = {
        'first_name': first_name,
        'last_name': last_name,
        'acc_created_timestamp': timestamp,
        'acc_created_date': account_creation_date,
        'account_number': account_number,
        'gender': gender,
        'dateofbirth': dateofbirth,
        'bloodgroup': bloodgroup,
        'aadhaarID': aadhaar,
        'panID': pan,
        'account_balance': balance

    }
    return newCust


# Kafka broker address
bootstrap_servers = 'localhost:9092'

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# List of account numbers and customer IDs for simulation
account_numbers = ["123456789", "987654321", "555555555", "111111111"]
customer_ids = ["C123", "C456", "C789", "C012"]

# Simulate transactions
def simulate_transaction():
    account_number = random.choice(account_numbers)
    transaction_type = random.choice(["debit", "credit"])
    transaction_amount = round(random.uniform(1, 1000), 2)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        "account_number": account_number,
        "transaction_type": transaction_type,
        "transaction_amount": transaction_amount,
        "timestamp": timestamp
    }

# Simulate customer details
def simulate_customer_details():
    customer_id = random.choice(customer_ids)
    first_name = random.choice(["Alice", "Bob", "Charlie"])
    last_name = random.choice(["Smith", "Johnson", "Brown"])
    account_creation_date = datetime.now().strftime('%Y-%m-%d')
    return {
        "customer_id": customer_id,
        "first_name": first_name,
        "last_name": last_name,
        "account_creation_date": account_creation_date
    }

# Generate and send data to Kafka topics
while True:
    transaction_data = simulate_transaction()
    customer_data = simulate_customer_details()
    
    producer.send('banking-transactions', value=transaction_data)
    producer.send('customer-details', value=customer_data)
    
    print("Sent Transaction Data:", transaction_data)
    print("Sent Customer Data:", customer_data)
    
    time.sleep(random.uniform(0.5, 2))  # Simulate variable time between data generation

# Close the producer gracefully
producer.close()



newGrid[i][j] = grid[i][j] + min([grid[i-1][j] + d2arr[grid[i-1][j]] for j in range(columns)])



from kafka import KafkaConsumer
import json

# Kafka broker address
bootstrap_servers = 'localhost:9092'

# Kafka topic to consume from
topic = 'banking-transactions'

# Create Kafka consumer
consumer = KafkaConsumer(topic,
                         bootstrap_servers=bootstrap_servers,
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')))

# Consume and print messages
for message in consumer:
    print("Received message:", message.value)

# Close the consumer gracefully
consumer.close()










import random
import time
from datetime import datetime

# List of account numbers for simulation
account_numbers = ["123456789", "987654321", "555555555", "111111111"]

# Simulate transactions
def simulate_transaction():
    account_number = random.choice(account_numbers)
    transaction_type = random.choice(["debit", "credit"])
    transaction_amount = round(random.uniform(1, 1000), 2)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        "account_number": account_number,
        "transaction_type": transaction_type,
        "transaction_amount": transaction_amount,
        "timestamp": timestamp
    }

# Generate continuous stream of transactions
def generate_transaction_stream():
    while True:
        transaction = simulate_transaction()
        print(transaction)
        time.sleep(random.uniform(0.5, 2))  # Simulate variable time between transactions

if __name__ == "__main__":
    generate_transaction_stream()




import random
import time
from datetime import datetime

# List of account numbers for simulation
account_numbers = ["123456789", "987654321", "555555555", "111111111"]

# Simulate transactions
def simulate_transaction():
    account_number = random.choice(account_numbers)
    transaction_type = random.choice(["debit", "credit"])
    transaction_amount = round(random.uniform(1, 1000), 2)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        "account_number": account_number,
        "transaction_type": transaction_type,
        "transaction_amount": transaction_amount,
        "timestamp": timestamp
    }

# Generate continuous stream of transactions
def generate_transaction_stream():
    while True:
        transaction = simulate_transaction()
        print(transaction)
        time.sleep(random.uniform(0.5, 2))  # Simulate variable time between transactions

if __name__ == "__main__":
    generate_transaction_stream()
