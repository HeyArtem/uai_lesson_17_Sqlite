from datetime import datetime


def test_time():
    current_data = datetime.now().strftime("%Y-%m-%d")
    print(current_data)

    return current_data

test_time()
