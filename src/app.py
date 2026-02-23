import streamlit as st
import os

from parsers.messages import parse_messages, get_top_chatters, get_messages_over_time
from parsers.likes import parse_likes, get_top_liked_accounts
from parsers.network import parse_network
from visualizations import charts

st.set_page_config(page_title="InstaWrap", page_icon="🎁", layout="wide")

# Custom CSS for a Wrapped aesthetic
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1f1c2c, #928DAB); 
        color: white;
    }
    h1, h2, h3 {
        color: #FFD700;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .metric-card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .metric-value {
        font-size: 2.5em;
        font-weight: bold;
        color: #ff4b4b;
    }
    .metric-label {
        font-size: 1.2em;
        color: #eeeeee;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎁 Your Local Instagram Wrapped")

st.sidebar.header("Data Settings")
st.sidebar.markdown("Enter the absolute path to your exported Instagram data folder.")
data_dir = st.sidebar.text_input("Folder Path (e.g., C:/Users/Me/Downloads/instagram_export)", value="")

if not data_dir or not os.path.exists(data_dir):
    st.info("👋 Welcome! Please provide the path to your extracted Instagram JSON data folder in the sidebar to begin.")
else:
    # ------------------
    # Data Loading
    # ------------------
    with st.spinner("Analyzing your Instagram life..."):
        df_threads, df_msgs = parse_messages(data_dir)
        df_likes = parse_likes(data_dir)
        mutuals, dont_follow_back, fans = parse_network(data_dir)

    st.success("Analysis Complete!")

    # ------------------
    # Top-Level Metrics
    # ------------------
    st.header("Overview")
    col1, col2, col3 = st.columns(3)
    
    total_msgs = df_msgs.shape[0] if df_msgs is not None else 0
    total_likes = df_likes.shape[0] if df_likes is not None else 0
    total_mutuals = len(mutuals) if mutuals is not None else 0

    with col1:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{total_msgs:,}</div><div class='metric-label'>Total Messages Sent/Received</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{total_likes:,}</div><div class='metric-label'>Posts Liked</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{total_mutuals:,}</div><div class='metric-label'>Mutual Connections</div></div>", unsafe_allow_html=True)
        
    st.markdown("---")

    # ------------------
    # Messages Section
    # ------------------
    if df_threads is not None and not df_threads.empty:
        st.header("💬 Direct Messages")
        top_chatters = get_top_chatters(df_threads, 10)
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Top Chatters")
            fig = charts.plot_bar_chart(top_chatters, 'Thread Name', 'Total Messages', 'Most active message threads', ["#ff4b4b"])
            st.plotly_chart(fig, use_container_width=True)
            
        with c2:
            st.subheader("Message Volume Over Time")
            msg_timeline = get_messages_over_time(df_msgs)
            fig2 = charts.plot_line_chart(msg_timeline, 'YearMonth', 'Message Count', 'Messages per month')
            st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
            
    # ------------------
    # Likes Section
    # ------------------
    if df_likes is not None and not df_likes.empty:
        st.header("❤️ Likes")
        top_liked = get_top_liked_accounts(df_likes, 10)
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Your Favorite Accounts")
            st.markdown("Based on whose posts you like the most.")
            fig = charts.plot_bar_chart(top_liked, 'Account', 'Likes', 'Most liked accounts', ["#1DB954"])
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ------------------
    # Network Section
    # ------------------
    if mutuals is not None:
        st.header("🕸️ Network & Following")
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Connections Breakdown")
            labels = ['Mutuals', 'Fans (Follow You Only)', "You Follow (Don't Follow Back)"]
            values = [len(mutuals), len(fans), len(dont_follow_back)]
            fig = charts.plot_pie_chart(labels, values, "Follower Ratio")
            st.plotly_chart(fig, use_container_width=True)
            
        with c2:
            st.subheader("The 'Don't Follow Back' List")
            if dont_follow_back:
                st.dataframe(sorted(list(dont_follow_back)))
            else:
                st.success("Wow! Everyone you follow follows you back.")
