from datetime import datetime

# Base class for a post
class Post:
    def init(self, text):
        self.text = text
        self.timestamp = datetime.now()
        self.user = None  # Starts without a user

    def str(self):
        return f"{self.user.first_name} {self.user.last_name}: \"{self.text}\"\n  {self.timestamp.strftime('%A, %b %d, %Y')}"

# Different types of posts
class TextPost(Post):
    def init(self, text):
        super().init(text)

class PicturePost(Post):
    def init(self, text, image_url):
        super().init(text)
        self.image_url = image_url

    def str(self):
        return f"{super().str()}\n  Pic URL: {self.image_url}"

class CheckInPost(Post):
    def init(self, text, latitude, longitude):
        super().init(text)
        self.latitude = latitude
        self.longitude = longitude

    def str(self):
        return f"{self.user.first_name} Checked In: \"{self.text}\"\n  {self.latitude}, {self.longitude}\n  {self.timestamp.strftime('%A, %b %d, %Y')}"

# User class
class User:
    def init(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        post.user = self  # Assign the user to the post
        self.posts.append(post)  # Add the post to the user's list of posts

    def follow(self, user):
        if user not in self.following:
            self.following.append(user)

    def get_timeline(self):
        timeline = []
        for user in self.following:
            timeline.extend(user.posts)
        return sorted(timeline, key=lambda p: p.timestamp, reverse=True)

# Example usage
if name == "main":
    # Create users
    john = User("John", "Lennon", "john@rmotr.com")
    paul = User("Paul", "McCartney", "paul@rmotr.com")
    george = User("George", "Harrison", "george@rmotr.com")

    # Follow users
    john.follow(paul)
    john.follow(george)

    # Create posts
    paul.add_post(TextPost("Post 1"))
    george.add_post(TextPost("Post 2"))
    paul.add_post(TextPost("Post 3"))

    # Display timeline for John
    print("Timeline for John Lennon:")
    for post in john.get_timeline():
        print(post)

    # Display different types of posts
    text_post = TextPost("All you need is love!")
    picture_post = PicturePost("Check my new guitar.", image_url='imgur.com/guitar.png')
    checkin_post = CheckInPost("At Abbey Road Studios", latitude="19.111", longitude="-9.2222")

    john.add_post(text_post)
    john.add_post(picture_post)
    john.add_post(checkin_post)

    print("\nPosts by John Lennon:")
    print(text_post)
    print(picture_post)
    print(checkin_post)