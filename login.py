import menu
import os
import json

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
        return self.__username + str(self.__userID)
    
    def get_username(self):
        return self.__username
    
    def save_test_results(self, test_results):
        # create directory for user records
        directory = "test_records"
        os.makedirs(directory, exist_ok = True)

        # create the full pathname for this user
        file_path = os.path.join(directory, f"{self.get_user()}.json")

        # load existing or start a new history
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                history = json.load(f)
        else:
            history = []

        # tack the new results to the end and save
        history.extend(test_results)
        with open(file_path, "w") as f:
            json.dump(history, f, indent=4)

    def load_user_history(self):
        file_path = f"test_records/{self.get_user()}.json"

        try:
            with open(file_path, "r") as f:
                history = json.load(f)
                return history
        except FileNotFoundError:
            return []