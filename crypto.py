# Example Python code for declaring a cryptocurrency

class Cryptocurrency:
    def __init__(self, name, symbol, total_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balance = 0

    def __str__(self):
        return f"{self.name} ({self.symbol}) - Total Supply: {self.total_supply} - Current Balance: {self.balance}"

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred {amount} {self.symbol} to {recipient.name}")
        else:
            print("Insufficient balance")

# Creating instances of cryptocurrencies
bitcoin = Cryptocurrency("Bitcoin", "BTC", 21000000)
ethereum = Cryptocurrency("Ethereum", "ETH", 115000000)

# Performing transfers
bitcoin.balance = 2
ethereum.balance = 5

alice = Cryptocurrency("Alice", "ALC", 0)
bob = Cryptocurrency("Bob", "BOB", 0)

print(bitcoin)
print(ethereum)

bitcoin.transfer(alice, 1)
ethereum.transfer(bob, 3)

print(bitcoin)
print(ethereum)
print(alice)
print(bob)
