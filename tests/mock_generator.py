import os
import json
import random
import time
from datetime import datetime, timedelta

def generate_mock_data(base_path="mock_instagram_data"):
    """
    Generates a folder structure and JSON files that mimic an Instagram data export.
    """
    os.makedirs(base_path, exist_ok=True)
    
    # 1. Generate Followers and Following
    connections_path = os.path.join(base_path, "connections", "followers_and_following")
    os.makedirs(connections_path, exist_ok=True)
    
    # Fake users
    my_username = "test_user_wrapped"
    friends = [f"friend_{i}" for i in range(1, 51)]
    
    # Let's say we follow 40, 30 follow us back.
    following = [{"string_list_data": [{"href": f"https://www.instagram.com/{f}", "value": f, "timestamp": int(time.time()) - random.randint(10000, 10000000)}]} for f in friends[:40]]
    followers = [{"string_list_data": [{"href": f"https://www.instagram.com/{f}", "value": f, "timestamp": int(time.time()) - random.randint(10000, 10000000)}]} for f in friends[:30]]
    
    with open(os.path.join(connections_path, "following.json"), "w") as f:
        # Some versions wrap it in a key, some are raw lists. Let's use the object wrapper format seen in recent exports
        json.dump({"relationships_following": following}, f, indent=2)
        
    with open(os.path.join(connections_path, "followers_1.json"), "w") as f:
        json.dump({"relationships_followers": followers}, f, indent=2)

    # 2. Generate Messages
    messages_path = os.path.join(base_path, "messages", "inbox")
    os.makedirs(messages_path, exist_ok=True)
    
    # Pick a few top friends to have long conversations with
    top_friends = friends[:5]
    other_friends = friends[5:15]
    
    for friend in top_friends + other_friends:
        thread_path = os.path.join(messages_path, f"{friend}_{random.randint(1000, 9999)}")
        os.makedirs(thread_path, exist_ok=True)
        
        # Decide how many messages this thread has
        num_msgs = random.randint(500, 2000) if friend in top_friends else random.randint(5, 100)
        
        messages = []
        # Simulate back and forth over the past year
        current_time_ms = int(time.time() * 1000) - (365 * 24 * 60 * 60 * 1000)
        
        for _ in range(num_msgs):
            # Advance time by a few hours or minutes
            current_time_ms += random.randint(60_000, 86_400_000) 
            sender = random.choice([my_username, friend])
            messages.append({
                "sender_name": sender,
                "timestamp_ms": current_time_ms,
                "content": "This is a mock message " + str(random.randint(1, 100)),
                "is_unsent": False
            })
            
        messages.reverse() # chronological order is usually newest first in the JSON
            
        thread_data = {
            "participants": [{"name": friend}, {"name": my_username}],
            "messages": messages,
            "title": friend,
            "is_still_participant": True,
            "thread_path": f"inbox/{friend}"
        }
        
        with open(os.path.join(thread_path, "message_1.json"), "w") as f:
            json.dump(thread_data, f, indent=2)
            
    # 3. Generate Likes
    likes_path = os.path.join(base_path, "likes")
    os.makedirs(likes_path, exist_ok=True)
    
    liked_posts = []
    for _ in range(500):
        friend = random.choice(friends)
        liked_posts.append({
            "title": friend,
            "string_list_data": [{
                "href": "https://www.instagram.com/p/MOCKPOST/",
                "value": "❤️",
                "timestamp": int(time.time()) - random.randint(1000, 31536000)
            }]
        })
        
    with open(os.path.join(likes_path, "liked_posts.json"), "w") as f:
        json.dump({"likes_media_likes": liked_posts}, f, indent=2)
        
    print(f"✅ Mock Instagram data successfully generated at '{base_path}/'")

if __name__ == "__main__":
    generate_mock_data()
