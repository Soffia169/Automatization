from elements.ManyWebElements import ManyWebElements


class ListWebElements(ManyWebElements):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_text(self):
        return super()._get_text()

    def get_attribute(self, attr):
        return super()._get_attribute(attr)