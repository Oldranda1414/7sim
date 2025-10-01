from enum import Enum

class Science(str, Enum):
    WRITING = "Writing"
    ENGINEERING = "Engineering"
    MATHEMATICS = "Mathematics"

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)
