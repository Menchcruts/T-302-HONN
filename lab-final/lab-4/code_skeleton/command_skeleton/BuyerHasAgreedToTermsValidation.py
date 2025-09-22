from Validation import Validation
from models.Buyer import Buyer

class BuyerHasAgreedToTermsValidation(Validation):
    def __init__(self, buyer: Buyer):
        super().__init__()
        self.buyer = buyer

    def validate(self):
        return self.buyer.has_agreed_to_terms