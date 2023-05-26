import json

class UserExtractor:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_json()
        self.users = self.data['users']
        
        self.communities = self.data['communities']

    def load_json(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        return data

    def get_user_by_name(self, name):
        for user in self.users:
            if user['name'] == name:
                return user
        return None

    def get_friends_names(self, user):
        friends = self.get_user_friends(user)
        friend_names = [self.get_user_name(friend) for friend in friends]
        return friend_names
    
    def get_user_name(self, user):
        return user['name']

    def get_user_email(self, user):
        return user['email']

    def get_user_birthdate(self, user):
        return user['birthdate']

    def get_user_profile_image_url(self, user):
        return user['profile_image_url']

    def get_user_liked_photos(self, user):
        return user['liked_photos']

    def get_user_family_members(self, user):
        return user['family']

    def get_user_groups(self, user):
        return user['groups']

    def get_user_communities(self, user):
        return user['communities']

    def get_user_friends(self, user):
        user_id = user['id']
        relationships = self.data['relationships']
        for relationship in relationships:
            if relationship['user_id'] == user_id:
                friend_ids = relationship['friends']
                friends = [self.get_user_by_id(friend_id) for friend_id in friend_ids]
                return friends
        return []

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None
    
    def get_community_by_name(self, name):
        for community in self.communities:
            if community['name'] == name:
                return community
        return None
    
    def get_user_friends_samecommunity(self, community, user):
        user_id = user['id']
        relationships = self.data['relationships']
        friends_same_community = []

        for relationship in relationships:
            if relationship['user_id'] == user_id:
                friend_ids = relationship['friends']
                friends = [self.get_user_by_id(friend_id) for friend_id in friend_ids]
                
                for friend in friends:
                    if community in friend['communities']:
                        friends_same_community.append(friend)

        return friends_same_community


user_extractor = UserExtractor(r'C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\project\\facebook_data.json')
user = user_extractor.get_user_by_name('Mr. Devin Gomez')

if user:
    name = user_extractor.get_user_name(user)
    email = user_extractor.get_user_email(user)
    birthdate = user_extractor.get_user_birthdate(user)
    profile_image_url = user_extractor.get_user_profile_image_url(user)
    liked_photos = user_extractor.get_user_liked_photos(user)
    family_members = user_extractor.get_user_family_members(user)
    groups = user_extractor.get_user_groups(user)
    communities = user_extractor.get_user_communities(user)
    friends = user_extractor.get_user_friends(user)

    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Birthdate: {birthdate}")
    print(f"Profile Image URL: {profile_image_url}")
    print(f"Liked Photos: {liked_photos}")
    print(f"Family Members: {family_members}")
    print(f"Groups: {groups}")
    print(f"Communities: {communities}")
    print(f"Friends: {friends}")
else:
    print("User not found.")
