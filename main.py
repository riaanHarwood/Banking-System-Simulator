from gui.app import BankApp

if __name__ == "__main__":
    try:
        app = BankApp()
        app.run()
    except Exception as e:
        print(f"An error occurred: {e}")