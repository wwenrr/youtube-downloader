if __name__ == "__main__":
    try:
        from src.view.ui import start_ui

        start_ui()
    except Exception as e:
        print(str(e))
        import time
        time.sleep(10)