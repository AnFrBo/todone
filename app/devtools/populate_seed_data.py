from datetime import datetime

from app.database.model.user import User
from app.database.model.task import Task
from app.database.model.action import Action
from app.database.db import get_session, init_db


def seed_users():
    with get_session() as session:
        user1 = User(user_name="Anna", user_mail="anbothe-huang@gmx.de")
        user2 = User(user_name="Boris", user_mail="bohubo@hotmail.com")
        session.add_all([user1, user2])


def seed_tasks():
    with get_session() as session:
        task1 = Task(
            title="Washing clothes",
            description="Includes washing, drying and/or hanging",
            solution_time=10,
            color="green",
        )
        task2 = Task(
            title="Cooking",
            description="Includes cooking a meal for at least the two of us, needs to be selfmade, going to a neighboring Dönnermann does not count",
            solution_time=45,
            color="blue",
        )
        task3 = Task(
            title="Clean bathroom",
            description="Includes changing towls, cleaning floor, taking out the trash etc.",
            solution_time=45,
            color="red",
        )
        session.add_all([task1, task2, task3])


def seed_actions():
    with get_session() as session:
        action = Action(user_uid=1, task_uid=1, started_at=datetime.now())
        session.add(action)


def seed_all():
    seed_users()
    seed_tasks()
    seed_actions()
    print("Seeding done.")


if __name__ == "__main__":
    init_db()
    seed_all()
