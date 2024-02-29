import re

class EmailAddressParser():
    def __init__(self, emails):
        self.emails = emails

    @property
    def emails(self):
        return self._emails
    
    @emails.setter
    def emails(self, emails):
        if isinstance(emails, str):
            self._emails = emails
        else:
            raise TypeError("Emails should be a string")
    
    def parse(self):
        pattern = r'[A-z]+[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}'
        regex = re.compile(pattern)
        return sorted(regex.findall(self._emails))