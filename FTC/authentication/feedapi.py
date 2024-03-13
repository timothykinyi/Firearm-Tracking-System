def policedata():
    
    people = [
    {
        "firstname": "John",
        "secondname": "Doe",
        "policeID": "12345",
        "rank": "Sergeant",
        "email": "john.doe@example.com",
        "phoneno": "123-456-7890"
    },
    {
        "firstname": "Alice",
        "secondname": "Smith",
        "policeID": "67890",
        "rank": "Lieutenant",
        "email": "alice.smith@example.com",
        "phoneno": "987-654-3210"
    },
    {
        "firstname": "Bob",
        "secondname": "Johnson",
        "policeID": "54321",
        "rank": "Captain",
        "email": "bob.johnson@example.com",
        "phoneno": "555-555-5555"
    }
    # Add more dictionaries for additional people as needed
    ]

    return people


def gundata( ):
    guns = [
    {
        "guntype": "Pistol",
        "gunserialnumber": "P12345",
        "manufacturedate": "2023-05-15",
        "trackercode": "T98765",
        "gunstatus": "Active",
        "assigned": True
    },
    {
        "guntype": "Rifle",
        "gunserialnumber": "R67890",
        "manufacturedate": "2022-09-20",
        "trackercode": "T54321",
        "gunstatus": "Inactive",
        "assigned": False
    },
    {
        "guntype": "Shotgun",
        "gunserialnumber": "S54321",
        "manufacturedate": "2024-01-10",
        "trackercode": "T12345",
        "gunstatus": "Active",
        "assigned": True
    }
    # Add more dictionaries for additional guns as needed
    ]

    return guns
