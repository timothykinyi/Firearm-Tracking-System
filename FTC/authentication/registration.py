import sqlite3

class policeofficer:
    def __init__(self, firstname, secondname, policeID, rank, email, phoneno):
        if not firstname:
            raise ValueError("First name not entered.")
        elif not secondname:
            raise ValueError("Second name not entered.")
        elif not policeID:
            raise ValueError("policeID not entered.")
        elif not rank:
            raise ValueError("rank not entered.")
        elif not email:
            raise ValueError("email not entered.")
        elif not phoneno:
            raise ValueError("phone number not entered.")
        self.firstname = firstname
        self.secondname = secondname
        self.policeID = policeID
        self.rank = rank
        self.email = email
        self.phoneno = phoneno

    @classmethod
    def createpolice(cls):
        infirstname = input("Enter your first name")
        insecondname = input("Enter your second name")
        inpoliceID = input("Enter your police ID")
        inrank = input("Enter your rank")
        inemail = input("Enter your email")
        inphoneno = input("Enter your phone number ")
        return cls(infirstname, insecondname, inpoliceID, inrank, inemail, inphoneno)
        
    def registerofficer(self):
        conn = sqlite3.connect("police.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO police (firstname, secondname, policeID, rank, email, phoneno) VALUES (?, ?, ?, ?, ?, ?)", (self.firstname, self.secondname, self.policeID, self.rank, self.email, self.phoneno))
        except:
            print("There was an error while updating the police database.")
        conn.commit()
        conn.close()
        
class gun:
    def __init__(self, guntype, gunserialnumber, manufacturedate, trackercode, gunstatus, asigned):
        if not guntype:
            raise ValueError("Gun type not entered.")
        elif not gunserialnumber:
            raise ValueError("Gun serial number not entered.")
        elif not manufacturedate:
            raise ValueError("Manufacture date not entered.")
        elif not trackercode:
            raise ValueError("Tracker code not entered.")
        elif not gunstatus:
            raise ValueError("Gun status not entered.")
        elif not asigned:
            raise ValueError("Gun asignment not entered.")
        self.guntype = guntype
        self.gunserialnumber = gunserialnumber
        self.manufacturedate = manufacturedate
        self.trackercode = trackercode
        self.gunstatus = gunstatus
        self.asigned = asigned
        
    @classmethod
    def creategun(cls):
        inguntype = input("Enter the gun ")
        ingunserialnumber = input("Enter the gun ")
        inmanufacturedate = input("Enter the gun ")
        intrackercode = input("Enter the gun tracker code ")
        ingunstatus = input("Enter the gun ")
        inasigned = input("Enter the gun ")
        return cls(inguntype, ingunserialnumber, inmanufacturedate, intrackercode, ingunstatus, inasigned)
    
    def registergun (self):
        conn = sqlite3.connect("gun.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO guns (guntype, gunserialnumber, manufacturedate, trackercode, gunstatus, asigned) VALUES (?, ?, ?, ?, ?, ?)", (self.guntype, self.gunserialnumber, self.manufacturedate, self.trackercode, self.gunstatus, self.asigned))
        except:
            print("There was an error updating the db ")
        conn.commit()
        conn.close()
        
def main():
    newgun = gun.creategun()
    newgun.registergun()
    
if __name__ =="__main__":
    main()