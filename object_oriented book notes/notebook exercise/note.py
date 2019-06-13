import datetime

# store the next available id for all new notes
last_id = 0

class Note :
    """repressent a note in the notebook match against a string in searches and store tags
    for each note
    """
    def __init__ (self,memo,tags =""):
        """initialize a note with memo and optional space-separated tags.automatically
        set the notes creation date and unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    def match(self,filter):
        """ determine true if it matches the filter text return true if it matches, false otherwise"""

        """
        case sensitive
        """
        return filter in self.memo or filter in self.tags

note1 = Note("hello there")
note2 = Note("General Kenobi")
print(note1.id)
print(note2.id)
print(note1.match("hello"))
print(note2.match("bold one"))