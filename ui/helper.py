def get_input(field):
    while True:
        value = input(f"enter {field} .").strip()
        if not value:
            print(f"value {field} can not be empty")
            continue
        return value

