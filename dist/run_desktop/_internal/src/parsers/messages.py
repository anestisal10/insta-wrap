import os
import json
import pandas as pd
from datetime import datetime

def parse_messages(base_path):
    """
    Parses all message_1.json files in the messages/inbox directory.
    Returns DataFrames for overall stats and message timeline.
    """
    inbox_path = os.path.join(base_path, "messages", "inbox")
    if not os.path.exists(inbox_path):
        return None, None
    
    all_messages = []
    thread_stats = []
    
    for thread_dir in os.listdir(inbox_path):
        thread_full_path = os.path.join(inbox_path, thread_dir)
        if not os.path.isdir(thread_full_path):
            continue
            
        json_path = os.path.join(thread_full_path, "message_1.json")
        if not os.path.exists(json_path):
            continue
            
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                continue
                
            title = data.get("title", "Unknown Thread")
            messages = data.get("messages", [])
            
            # Thread level stats
            thread_stats.append({
                "Thread Name": title,
                "Total Messages": len(messages)
            })
            
            # Message level stats
            for msg in messages:
                sender = msg.get("sender_name", "Unknown")
                timestamp = msg.get("timestamp_ms")
                if timestamp:
                    # Convert to datetime
                    dt = datetime.fromtimestamp(timestamp / 1000.0)
                    all_messages.append({
                        "Thread": title,
                        "Sender": sender,
                        "Date": dt.date(),
                        "Hour": dt.hour,
                        "YearMonth": dt.strftime("%Y-%m")
                    })
                    
    df_threads = pd.DataFrame(thread_stats)
    df_msgs = pd.DataFrame(all_messages)
    
    return df_threads, df_msgs

def get_top_chatters(df_threads, top_n=10):
    if df_threads is None or df_threads.empty:
        return pd.DataFrame()
    return df_threads.sort_values(by="Total Messages", ascending=False).head(top_n)

def get_messages_over_time(df_msgs):
    if df_msgs is None or df_msgs.empty:
        return pd.DataFrame()
    return df_msgs.groupby('YearMonth').size().reset_index(name='Message Count')
