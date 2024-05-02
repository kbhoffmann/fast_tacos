from models.taco import engine as db
from settings import settings
import time

ATTEMPTS = 5

print("CONNECTING TO {}".format(settings.DATABASE.SQLALCHEMY_DATABASE_URL))


def try_connection(attempts=0):
    print("TRYING TO CONNECT")
    if attempts > 10:
        return False
    try:
        db.connect()
    except Exception as e:
        print("FAILED, TRYING AGAIN IN 5 SECONDS...")
        print(e)
        time.sleep(5)
        return try_connection(attempts + 1)

    print("CONNECTED")

    # Connected
    return False


not_connected = True
while not_connected:
    not_connected = try_connection()
