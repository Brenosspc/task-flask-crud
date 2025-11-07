class Task: # lista
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self): # dicionario 
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }