from database import SessionLocal
from models import User, Post

def add_posts():
    session = SessionLocal()
    try:
        # Предполагается, что пользователи уже добавлены
        users = session.query(User).all()
        if not users:
            print("Нет пользователей для добавления постов.")
            return
        
        posts = [
            Post(title='Первый пост Сергея', content='Это первый пост Сергея', user_id=users[0].id),
            Post(title='Второй пост Сергея', content='Это второй пост Сергея', user_id=users[0].id),
            Post(title='Пост Анастасии', content='Это пост Анастасии', user_id=users[1].id),
            Post(title='Пост Варвары', content='Это пост Вари', user_id=users[2].id)
        ]
        session.add_all(posts)
        session.commit()
        print("Посты добавлены успешно.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении постов: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    add_posts()
