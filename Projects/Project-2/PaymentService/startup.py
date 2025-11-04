from app.database import Base, engine
from app.consumer import start_consumer

Base.metadata.create_all(bind=engine)

def main():
    start_consumer()

if __name__ == "__main__":
    main()