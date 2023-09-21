from user import User
import post

app_user_one = User("Adam@abc.com", "Adam", "abc", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_jobtitle("Platform Engineer")
app_user_one.get_user_info()

post_user = post.Post("ABC", app_user_one.name)
post_user.get_post_info()