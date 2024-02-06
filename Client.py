# Name: Trent Adams
# Date: 2024-01-28


class Client:
    def __init__(self, client_id, first_name, last_name, phone, email):
        self.__client_id = client_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email

    def __lt__(self, other):
        this_full_name = self.__last_name + " " + self.__first_name
        other_full_name = other.__last_name + " " + other.__first_name
        if this_full_name == other_full_name:
            return self.__client_id < other.__client_id
        else:
            return this_full_name < other_full_name
        
    def __le__(self, other):
        return self.__client_id <= other.__client_id

    def __eq__(self, other):
        return (self.__client_id == other.__client_id and 
                self.__first_name == other.__first_name and 
                self.__last_name == other.__last_name and 
                self.__phone == other.__phone and 
                self.__email == other.__email)

    def __str__(self):
        return (self.__last_name + ", " + self.__first_name)
    
    def get_client_id(self):
        return self.__client_id
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email
    
    def set_client_id(self, client_id):
        self.__client_id = client_id
