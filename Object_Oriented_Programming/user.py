class User:
    def __init__(self, user_email, name, password, current_job):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job = current_job

    def change_password(self, new_password):
        self.password = new_password

    def change_jobtitle(self, new_jobtitile):
        self.current_job = new_jobtitile

    def get_user_info(self):
        print(f"User {self.name} currently work as {self.current_job} and email address is {self.email} ")


