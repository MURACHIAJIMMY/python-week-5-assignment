class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def get_info(self):
        return f"{self.brand} {self.model} costs ${self.price}"


# Inheritance: A specialized class for Gaming Smartphones
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu, cooling_system):
        super().__init__(brand, model, price)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        return f"Playing {game_name} on {self.brand} {self.model} with {self.gpu} GPU."

    # Overriding the get_info method to include gaming-specific details
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}. Equipped with {self.gpu} GPU and {self.cooling_system} cooling system."


# Example usage
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 999)
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1299, "Adreno 730", "Vapor Chamber")

    print(phone.get_info())
    print(phone.make_call("123-456-7890"))
    print(gaming_phone.get_info())
    print(gaming_phone.play_game("Genshin Impact"))