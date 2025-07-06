def countbyrole(self,role):
    return reduce(lambda x,y: x+(1 if y.getrole()== role else 0),self.people,0)

rolemanagerObj = RoleManager()
rolemanagerObj.addperson(Student("Nilar",20,"ST1002","Physics"))
rolemanagerObj.addperson(Teacher)