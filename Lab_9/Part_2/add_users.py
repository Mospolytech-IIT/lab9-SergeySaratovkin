from database import SessionLocal
from models import User

def add_users():
    session = SessionLocal()
    try:
        users = [
            User(username='Сергей_Саратовкин', email='Sergey@example.com', password='sergeypass'),
            User(username='Анастасия_Алфёрова', email='Nastya@example.com', password='nastyapass'),
            User(username='Варвара_Чернова', email='Varya@example.com', password='varyapass')
        ]
        session.add_all(users)
        session.commit()
        print("Пользователи добавлены успешно.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении пользователей: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    add_users()



