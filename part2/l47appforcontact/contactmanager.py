# import json
# import os

# class ContactManager:
#     def __init__(self,jsonfileurl='contacts.json'):
#         self.jsonfileurl = jsonfileurl

#     def loadcontacts(self):
#         if not os.path.exists(self.jsonfileurl):
#             return []
        
#         with open(self.josnfileurl,'r') as file:
#             return json.load(file)
        
#     def savecontact(self, excontacts):
#         with open(self.jsonfileurl, 'w') as file:
#             json.dump(excontacts,file,indent=4)
    
#     def createcontact(self, name, phone, email):
#         existingcontacts = self.loadcontacts()
#         newcontact = {
#             "id": len(existingcontacts)+1,
#             "name": name,
#             "phone": phone,
#             "email": email
#         }
#         existingcontacts.append(newcontact)
#         self.savecontact(existingcontacts)
#         print("New contact created successfully.")

#     def readcontact(self):
#         existingcontacts = self.loadcontacts()

#         for contact in existingcontacts:
#             print(f"{contact['id']}. {contact['name']} {contact['phone']} - {contact['email']}")

#     def updatecontact(self, contactid, name = None, phone = None,email=None):
#         contacts = self.loadcontacts()
#         found = False
#         for contact in contacts:
#             if contact["id"] == contactid:
#                 # if name: contact["name"] = name
#                 # if phone: contact["phone"] = phone
#                 # if email: contact["email"] = email

#                 if name is not None:
#                     contact["name"] = name
#                 if phone is not None:
#                     contact["phone"] = phone
#                 if email is not None:
#                     contact["email"] = email
#                 self.savecontact(contacts)
#                 print("Contact Successfully Updated.")
#                 found = True
#                 return
            
#         if not found:
#             print("Contact Not Found.")

#     def deletecontact(self, contactid):
#         contacts = self.loadcontacts()
#         newcontacts = [x for x in contacts if x["id"] != contactid]

#         if len(contacts) == len(newcontacts):
#             print("Contact Not Found")
#         else:
#             self.savecontact(newcontacts)
#             print("Contact Successfully Deleted.")


#     def importcontacts(self, impjsonfile):
#         contacts = self.loadcontacts()

#         with open(impjsonfile,'r') as file:
#             imported = json.load(file)

#         lastid = contacts[-1]["id"] if contacts else 0

#         for key,value in enumerate(imported):
#             value["id"] = lastid + key + 1
#             contacts.append(value)

#         self.savecontact(contacts)
#         print(f"Imported {len(imported)} contacts.")


#     def exportcontacts(self,expfilename):
#         existingcontacts = self.loadcontacts()

#         with open(expfilename, 'w') as file:
#             json.dump(existingcontacts,file,indent=4)
#         print(f"Exported to {expfilename}.")


# 15CT

import json
import os

class ContactManager:
    def __init__(self, jsonfileurl='contacts.json'):
        self.jsonfileurl = jsonfileurl
        # Initialize contacts file if it doesn't exist
        if not os.path.exists(self.jsonfileurl):
            with open(self.jsonfileurl, 'w') as file:
                json.dump([], file)

    def loadcontacts(self):
        try:
            with open(self.jsonfileurl, 'r') as file:
                contacts = json.load(file)
                return contacts if isinstance(contacts, list) else []
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def savecontact(self, contacts):
        with open(self.jsonfileurl, 'w') as file:
            json.dump(contacts, file, indent=4)
    
    def createcontact(self, name, phone, email):
        existingcontacts = self.loadcontacts()
        new_id = max([c['id'] for c in existingcontacts], default=0) + 1
        newcontact = {
            "id": new_id,
            "name": name,
            "phone": phone,
            "email": email
        }
        existingcontacts.append(newcontact)
        self.savecontact(existingcontacts)
        print("New contact created successfully.")

    def readcontact(self):
        existingcontacts = self.loadcontacts()
        if not existingcontacts:
            print("No contacts found.")
            return
            
        print("\nContact List:")
        for contact in existingcontacts:
            print(f"{contact['id']}. {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")

    def updatecontact(self, contactid, name=None, phone=None, email=None):
        contacts = self.loadcontacts()
        for contact in contacts:
            if contact["id"] == contactid:
                if name is not None:
                    contact["name"] = name
                if phone is not None:
                    contact["phone"] = phone
                if email is not None:
                    contact["email"] = email
                self.savecontact(contacts)
                print("Contact successfully updated.")
                return
        print("Contact not found.")

    def deletecontact(self, contactid):
        contacts = self.loadcontacts()
        newcontacts = [x for x in contacts if x["id"] != contactid]
        
        if len(contacts) == len(newcontacts):
            print("Contact not found.")
        else:
            self.savecontact(newcontacts)
            print("Contact successfully deleted.")

    def importcontacts(self, impjsonfile):
        try:
            existing = self.loadcontacts()
            with open(impjsonfile, 'r') as file:
                imported = json.load(file)
                
            if not isinstance(imported, list):
                print("Invalid import file format.")
                return
                
            last_id = max([c['id'] for c in existing], default=0) if existing else 0
            for contact in imported:
                last_id += 1
                contact['id'] = last_id
                existing.append(contact)
                
            self.savecontact(existing)
            print(f"Successfully imported {len(imported)} contacts.")
        except Exception as e:
            print(f"Error during import: {str(e)}")

    def exportcontacts(self, expfilename):
        try:
            contacts = self.loadcontacts()
            with open(expfilename, 'w') as file:
                json.dump(contacts, file, indent=4)
            print(f"Successfully exported {len(contacts)} contacts to {expfilename}.")
        except Exception as e:
            print(f"Error during export: {str(e)}")

# 22IM