import joblib


class ClassifierModel:
    """Get or open a model instance"""
    _instances = {}

    def __new__(cls, *args, **kwargs) -> None:
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def __init__(self, model: str) -> None:
        self.model = joblib.load(model)

    def get_model(self):
        return self.model


clf_model = ClassifierModel("clf.zahoree")
