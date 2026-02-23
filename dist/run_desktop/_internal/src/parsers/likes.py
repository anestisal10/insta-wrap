import os
import json
import pandas as pd
from datetime import datetime

def parse_likes(base_path):
    """
    Parses the liked_posts.json file.
    Returns a DataFrame of liked posts stats.
    """
    likes_file = os.path.join(base_path, "likes", "liked_posts.json")
    if not os.path.exists(likes_file):
        return None
        
    likes_data = []
    
    with open(likes_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return None
            
        likes_list = data.get("likes_media_likes", [])
        
        for item in likes_list:
            # The account whose post was liked
            account_name = item.get("title", "Unknown")
            
            # Get timestamp if available
            string_list_data = item.get("string_list_data", [])
            timestamp = None
            if string_list_data:
                timestamp = string_list_data[0].get("timestamp")
                
            dt = datetime.fromtimestamp(timestamp) if timestamp else None
            
            likes_data.append({
                "Account": account_name,
                "YearMonth": dt.strftime("%Y-%m") if dt else "Unknown"
            })
            
    return pd.DataFrame(likes_data)

def get_top_liked_accounts(df_likes, top_n=10):
    if df_likes is None or df_likes.empty:
        return pd.DataFrame()
    return df_likes['Account'].value_counts().reset_index().rename(columns={'count': 'Likes', 'Account': 'Account'}).head(top_n)
