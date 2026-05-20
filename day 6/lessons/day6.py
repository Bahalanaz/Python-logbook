class Transaction:
    def __enter__(self):
        print("Starting transaction")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Error occurred → rollback")
        else:
            print("Success → commit")

        print("Connection closed")


# Successful flow
with Transaction() as t:
    print("Updating user balance")
    print("Adding transaction log")


# Error 
with Transaction() as t:
    try:
        print("Updating user balance")
        x = 10 / 0  # error
        print(x)

    except:
        print("Code is bugged")

    finally:
        print("Still cleaned")
