from Validation import Validation
from models.Merchant import Merchant

class MerchantAllowsModificationsValidation(Validation):
    def __init__(self, merchant: Merchant):
        super().__init__()
        self.merchant = merchant

    def validate(self):
        return self.merchant.allow_modifications
