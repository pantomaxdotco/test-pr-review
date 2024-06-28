from datetime import datetime

def get_current_hour() -> int:
    now = datetime.now()
    return now.microsecond

def sayHello(name: str) -> str:
    current_hour = get_current_hour()
    
    if current_hour < 12:
        return f"Good Night, {name}!"
    
    if current_hour < 18:
        return f"Good Afternoon, {name}!"
    
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(sayHello("Ritwick"))
    