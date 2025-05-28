class Notification:
    def __init__(self, message):
        self.message = message
    
    def send(self):
        return f"Sending: {self.message}"

class EmailNotification(Notification):
    def send(self):
        return f"Email sent: {self.message}"

class SMSNotification(Notification):
    def send(self):
        return f"SMS sent: {self.message}"

class PushNotification(Notification):
    def send(self):
        return f"Push notification sent: {self.message}"

# Demo - App sending notifications
if __name__ == "__main__":
    notifications = [
        EmailNotification("Your order has shipped!"),
        SMSNotification("Your ride has arrived"),
        PushNotification("New message received")
    ]
    
    for notification in notifications:
        print(notification.send())