import os
import json
import pandas as pd

def _extract_users(json_data, key1, key2):
    """
    Helper to extract usernames from the nested IG JSON structure
    """
    users = set()
    
    # Try multiple known structures
    if isinstance(json_data, list):
        items = json_data
    elif key1 in json_data:
        items = json_data[key1]
    elif key2 in json_data:
        items = json_data[key2]
    else:
        return users
        
    for item in items:
        # Standard format
        if "string_list_data" in item:
            for str_data in item["string_list_data"]:
                users.add(str_data.get("value"))
    
    return {u for u in users if u} # Remove None/empty

def parse_network(base_path):
    """
    Parses followers and following JSON files to find network stats.
    """
    connections_path = os.path.join(base_path, "connections", "followers_and_following")
    if not os.path.exists(connections_path):
        return None, None, None
        
    followers_file = os.path.join(connections_path, "followers_1.json")
    following_file = os.path.join(connections_path, "following.json")
    
    followers = set()
    following = set()
    
    if os.path.exists(followers_file):
        with open(followers_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                followers = _extract_users(data, "relationships_followers", "followers")
            except:
                pass
                
    if os.path.exists(following_file):
        with open(following_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                following = _extract_users(data, "relationships_following", "following")
            except:
                pass
                
    # Analysis
    mutuals = following.intersection(followers)
    dont_follow_back = following - followers
    fans = followers - following
    
    return mutuals, dont_follow_back, fans
