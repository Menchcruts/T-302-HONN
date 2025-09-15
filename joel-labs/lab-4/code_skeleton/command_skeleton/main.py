from BuyerHasAgreedToTermsValidation import BuyerHasAgreedToTermsValidation
from MerchantAllowsModificationsValidation import MerchantAllowsModificationsValidation
from OrderIsUnpaidValidation import OrderIsUnpaidValidation
from Validator import Validator
from models.Buyer import Buyer
from models.Merchant import Merchant
from models.Order import Order, OrderStatus


def is_order_valid_for_modification(order: Order):
        validator = Validator()
        validator.add_validation(MerchantAllowsModificationsValidation(order.merchant))
        validator.add_validation(BuyerHasAgreedToTermsValidation(order.buyer))
        validator.add_validation(OrderIsUnpaidValidation(order))
        return validator.validate()


if __name__ == '__main__':
    order = Order(merchant=Merchant(allow_modifications=False),
                  buyer=Buyer(has_agreed_to_terms=False),
                  status=OrderStatus.Cancelled)

    print(is_order_valid_for_modification(order))

    order.merchant.allow_modifications = True

    print(is_order_valid_for_modification(order))

    order.buyer.has_agreed_to_terms = True
    print(is_order_valid_for_modification(order))

    order.status = OrderStatus.Unpaid
    print(is_order_valid_for_modification(order))