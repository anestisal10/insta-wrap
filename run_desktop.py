import os
import sys
import streamlit.web.cli as stcli

def resolve_path(path):
    """
    Resolve path to support PyInstaller's _MEIPASS temporary directory.
    When running as an executable, files are extracted to sys._MEIPASS.
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath("."), path)

if __name__ == "__main__":
    # Point to the app.py inside the bundled executable
    app_path = resolve_path(os.path.join("src", "app.py"))
    
    # Overwrite arguments to simulate `streamlit run`
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--server.headless=false",
        "--global.developmentMode=false",
    ]
    
    print("Starting InstaWrap...")
    sys.exit(stcli.main())
