def connect():
    raise NotImplementedError("Connect() is not implemented yet") # its give error when we call this function if we write pass it doesnot show any error

#connect()


#always write return type of funtion if we user type the code editor also help to suggest related functions

def get_Users() -> dict[int , str]:
    users:dict[int , str] = {1:"Piyush", 2:"Kumar",3:"Singh"}
    return users



print(get_Users())


