import menu

class Account:
    def __init__(self, username="default", userID = "1234"):
        self.__username = username
        self.__userID = userID

    def set_user(self):
        while True:
            temp_username = input("Choose a username: ")
            # check that username follows naming rules
            break
        self.__username = temp_username
        while True:    
            temp_userID = input("Choose a 4 digit userID number: ")
            # check that userID follows naming rules
            userID_len = len(temp_userID)
            if userID_len == 4 and all([char.isdigit() for char in temp_userID]):
                break
        self.__userID = int(temp_userID)

    def get_user(self):
        return self.__username, self.__userID
    def get_username(self):
        return self.__username