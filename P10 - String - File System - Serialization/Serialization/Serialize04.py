# Serialisasi dengan Json

import json
from typing import Any

class ContactEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, Contact):
            return{
                "__class__": "Contact",
                "first": obj.first,
                "last": obj.last,
                "full_name": obj.full_name,
            }
        return super().default(obj)
        
class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def full_name(self):
        return("{} {}".format(self.first, self.last))    
        
def decode_contact(json_object: Any) -> Any:
    if json_object.get("__class__") == "Contact":
        return Contact(json_object["first"], json_object["last"])
    else:
        return json_object
def main():
    c = Contact("Noriko", "Hannah")
    text = json.dumps(c, cls=ContactEncoder)
    print(text)
    
    some_text = (
        '{"__class__": "Contact", "first": "Milli", "last": "Dale", '
        '"full_name": "Milli Dale"}')
    c2 = json.loads(some_text, object_hook=decode_contact)
    print("c2.full_name:", c2.full_name)
    
if __name__ == "__main__":
    main()