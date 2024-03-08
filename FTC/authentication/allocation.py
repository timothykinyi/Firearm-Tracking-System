import sqlite3

class allocation:
    
    def available(gunserialnumber):
        conn = sqlite3.connect("gun.db")
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT gunstatus, asigned FROM guns WHERE gunserialnumber = ?;',(gunserialnumber))
        except:
            print("There was an error while getting data from the database. ")
        details = cursor.fetchall()
        conn.commit()
        conn.close()
        if details[0][0] is "Active" and details[0][1] is "notasigned":
            return True
        else:
            return False

    def allocate(algunserialnumber, policeID, numberofbullets):
        gunconn = sqlite3.connect("gun.db")
        guncursor = gunconn.cursor()
        guncursor.execute("update the asignment status")
        gunconn.commit()
        gunconn.close()
        
        policeconn = sqlite3.connect("police.db")
        policecursor = policeconn.cursor()
        policecursor.execute(" check if there is a police with that id the allocate a gun to them collect info eg rank")
        policedetails = policecursor.fetchall()
        policeconn.commit()
        policeconn.close()
        policerank =policedetails[0][4]
        
        allocationconn = sqlite3.connect("gun.db")
        allocationcursor =allocationconn.cursor()
        try:
            allocationcursor.execute("INSERT INTO gunallocations (action, policeID, rank, gunserialnumber, numberofbullets) VALUES ('gun_allocation', ?, ?, ?, ?)", (policeID, policerank, algunserialnumber, numberofbullets))
        except:
            ...
        allocationconn.commit()
        allocationconn.close()
        
        
    def gunreturn(algunserialnumber, policeID, numberofbullets):
        gunconn = sqlite3.connect("gun.db")
        guncursor = gunconn.cursor()
        guncursor.execute("update the asignment status")
        gunconn.commit()
        gunconn.close()
        
        policeconn = sqlite3.connect("police.db")
        policecursor = policeconn.cursor()
        policecursor.execute(" check if there is a police with that id the allocate a gun to them collect info eg rank")
        policeconn.commit()
        policeconn.close()
        
        allocationconn = sqlite3.connect("gun.db")
        allocationcursor =allocationconn.cursor()
        allocationcursor.execute("SELECT * FROM WHERE gunserialnumber = ?",(algunserialnumber))
        allocationdetails = allocationcursor.fetchall()
        policerank = allocationdetails[0][1]
        try:
            allocationcursor.execute("INSERT INTO gunallocations (action, policeID, rank, gunserialnumber, numberofbullets ) VALUES ('gun_return', ?, ?, ?, ?)", (policeID, policerank, algunserialnumber, numberofbullets))
        except:
            ...
        allocationconn.commit()
        allocationconn.close()