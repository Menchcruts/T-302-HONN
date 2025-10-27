class TwilioGatewayFake:
    def send_sms(self, phone_number: str, message: str):
        print(f'Email to {phone_number} sent with message: {message}')
