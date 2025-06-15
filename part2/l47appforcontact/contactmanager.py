import json, os

class ContactManager:
    def __init__(self,jsonfileurl='contacts.json'):
        self.jsonfileurl = jsonfileurl

    def loadcontacts(self):
        if not os.path.exists(self.jsonfileurl):
            return []
        
        with open(self.josnfileurl,'r') as file:
            return json.load(file)
        
    def savecontact(self, excontacts):
        with open(self.jsonfileurl, 'w') as file:
            json.dump(excontacts,file,indent=4)
    
    def createcontact(self, name, phone, email):
        existingcontacts = self.loadcontacts()
        newcontact = {
            "id": len(existingcontacts)+1,
            "name": name,
            "phone": phone,
            "email": email
        }
        existingcontacts.append(newcontact)
        self.savecontact(existingcontacts)
        print("New contact created successfully.")

    def readcontact(self):
        existingcontacts = self.loadcontacts()

        for contact in existingcontacts:
            print(f"{contact['id']}. {contact['name']} {contact['phone']} - {contact['email']}")

    def updatecontact(self, contactid, name = None, phone = None,email=None):
        return

    def deletecontact(self, contactid):
        return

    def importcontacts(self, impjsonfile):
        return    

    def exportcontacts(self,expfilename):
        existingcontacts = self.loadcontacts()

        with open(self.jsonfileurl, 'w') as file:
            json.dump(expfilename,file,indent=4)
        print(f"Exported to {expfilename}.")


# 15CT