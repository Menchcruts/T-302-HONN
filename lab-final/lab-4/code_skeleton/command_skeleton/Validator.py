from Validation import Validation

class Validator(Validation):
    def __init__(self):
        self.__validations: list[Validation] = []
    
    def add_validation(self, validation: Validation) -> None:
        self.__validations.append(validation)

    def validate(self) -> bool:
        correct = True
        for validation in self.__validations:
            if not validation.validate():
                correct = False
                break
        return correct