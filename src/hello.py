
class Hello():
    
    def __init__(self, name):
        self.name = name

    def __call__(self):
        if self.name:
            message = "Hello {0}".format(self.name)
        else: 
            message = 'Pass a name in the request body for a personalized response'
        return message