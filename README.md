# 🎁 InstaWrap: Your Local Instagram Data Analyzer

InstaWrap is an open-source, local-first Python application that parses your exported Instagram JSON data to provide a fun, private "Wrapped"-style dashboard. 

Unlike third-party websites that ask for your Instagram password (risking account bans or data theft), InstaWrap runs **entirely on your own computer**. Your data never leaves your machine.

## ✨ Features
- **💬 Direct Messages:** See who your top chatters are and track your message volume over time.
- **❤️ Likes:** Discover whose posts you like the most based on your engagement history.
- **🕸️ Network Insights:** Instantly find out who doesn't follow you back, see your mutual friends, and identify your "fans" (people who follow you, but you don't follow back).

---

## 🚀 Getting Started

### 1. Request Your Instagram Data
To use this tool, you must first request your data directly from Instagram.
1. Open the Instagram app or website and go to **Settings and Activity**.
2. Go to **Accounts Center** -> **Your information and permissions** -> **Download your information**.
3. Create a new download request.
4. **CRITICAL:** You must select **JSON** format! Do not select HTML. 
5. Select the types of information you want (ensure you include **Messages**, **Followers and following**, and **Likes**).
6. Wait for Instagram to email you the ZIP file.
7. Extract the downloaded ZIP file to any folder on your computer.

### 2. Run InstaWrap (No Installation Required)
If you just want to run the app without installing Python, you can simply download the pre-built desktop executable:
1. Go to the **[Releases](../../releases)** section on the right side of this GitHub repository page.
2. Download the latest `InstaWrap_Windows.zip` file.
3. Extract the ZIP file and double-click `run_desktop.exe`.
4. A terminal will briefly appear to start the local server, and then the app will launch in your browser automatically!

*Note: Windows Defender might flag this file as an "Unknown Publisher" since it is not digitally signed. You can safely click "More info" -> "Run anyway".*

### 2a. Run from Source Code (For Developers)
Make sure you have [Python](https://www.python.org/downloads/) installed (3.8 or higher is recommended).

1. Clone or download this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/InstaWrap.git
   cd InstaWrap
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the application:
   ```bash
   streamlit run src/app.py
   ```

5. The dashboard will automatically open in your web browser (usually at `http://localhost:8501`).
6. Paste the absolute path to your extracted Instagram data folder into the sidebar, and enjoy your Wrapped!

---

## 🛠️ Testing with Mock Data
If you want to see what the dashboard looks like before your Instagram data arrives, we have included a script to generate a fake dataset:
```bash
python tests/mock_generator.py
```
This will create a `mock_instagram_data/` folder. Paste the absolute path to this folder into the InstaWrap app to see the demo.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/YOUR_USERNAME/InstaWrap/issues) if you want to contribute.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# 🎁 InstaWrap: Your Local Instagram Data Analyzer

InstaWrap is an open-source, local-first Python application that parses your exported Instagram JSON data to provide a fun, private "Wrapped"-style dashboard. 

Unlike third-party websites that ask for your Instagram password (risking account bans or data theft), InstaWrap runs **entirely on your own computer**. Your data never leaves your machine.

## ✨ Features
- **💬 Direct Messages:** See who your top chatters are and track your message volume over time.
- **❤️ Likes:** Discover whose posts you like the most based on your engagement history.
- **🕸️ Network Insights:** Instantly find out who doesn't follow you back, see your mutual friends, and identify your "fans" (people who follow you, but you don't follow back).

---

## 🚀 Getting Started

### 1. Request Your Instagram Data
To use this tool, you must first request your data directly from Instagram.
1. Open the Instagram app or website and go to **Settings and Activity**.
2. Go to **Accounts Center** -> **Your information and permissions** -> **Download your information**.
3. Create a new download request.
4. **CRITICAL:** You must select **JSON** format! Do not select HTML. 
5. Select the types of information you want (ensure you include **Messages**, **Followers and following**, and **Likes**).
6. Wait for Instagram to email you the ZIP file.
7. Extract the downloaded ZIP file to any folder on your computer.

### 2. Run InstaWrap (No Installation Required)
If you just want to run the app without installing Python, you can simply download the pre-built desktop executable:
1. Go to the **[Releases](../../releases)** section on the right side of this GitHub repository page.
2. Download the latest `InstaWrap_Windows.zip` file.
3. Extract the ZIP file and double-click `run_desktop.exe`.
4. A terminal will briefly appear to start the local server, and then the app will launch in your browser automatically!

*Note: Windows Defender might flag this file as an "Unknown Publisher" since it is not digitally signed. You can safely click "More info" -> "Run anyway".*

### 2a. Run from Source Code (For Developers)
Make sure you have [Python](https://www.python.org/downloads/) installed (3.8 or higher is recommended).

1. Clone or download this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/InstaWrap.git
   cd InstaWrap
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the application:
   ```bash
   streamlit run src/app.py
   ```

5. The dashboard will automatically open in your web browser (usually at `http://localhost:8501`).
6. Paste the absolute path to your extracted Instagram data folder into the sidebar, and enjoy your Wrapped!

---

## 🛠️ Testing with Mock Data
If you want to see what the dashboard looks like before your Instagram data arrives, we have included a script to generate a fake dataset:
```bash
python tests/mock_generator.py
```
This will create a `mock_instagram_data/` folder. Paste the absolute path to this folder into the InstaWrap app to see the demo.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/YOUR_USERNAME/InstaWrap/issues) if you want to contribute.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
