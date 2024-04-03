import database
from faker import Faker

from entity.account import Account


def main():
    conn = database.create_connect()
    cursor = conn.cursor()

    fake = Faker("ru_RU")
    account = Account()
    account.login = fake.profile()['username']
    account.password = fake.password()
    account.security_question = fake.company_suffix()
    account.security_answer = fake.company()
    account.is_moder = fake.pybool()
    account.family_name = fake.last_name()

    print(account.__dict__)

    cursor.execute(
        """
            insert into unity.account(login, password, security_question, security_answer, is_moder, family_name)
            values('{login}','{password}', '{security_question}', '{security_answer}', {is_moder}, '{family_name}')
        """.format(
            login=account.login,
            password=account.password,
            security_question=account.security_question,
            security_answer=account.security_answer,
            is_moder=account.is_moder,
            family_name=account.family_name
        )
    )
    conn.commit()


if __name__ == '__main__':
    main()
