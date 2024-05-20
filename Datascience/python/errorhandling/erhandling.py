def errorhandling():
    try:
        kd
        raise ValueError("not defined")
    except ValueError:
        print(ValueError['id'])
    finally:
        print("block executed")
errorhandling()