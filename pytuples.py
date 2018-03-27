from collections import namedtuple

user_detail = dict()
users = []


def create_named_tuple():
    user = namedtuple('users' , 'userid,name')
    return user


def get_user_detail(userid , name):
    user_detail['userid'] = userid
    user_detail['name'] = name
    return user_detail


def add_user(user , user_detail):
    if isinstance(user_detail , dict):
        users.append(user(**user_detail))
    elif isinstance(user_detail , tuple):
        users.append(user(*user_detail))


def main():
    user = create_named_tuple()

    user_detail = get_user_detail(1 , 'Krishna')
    add_user(user , user_detail)
    user_detail = get_user_detail(2 , 'Swathi')
    add_user(user , user_detail)
    user_detail = get_user_detail(3 , 'Geetha')
    add_user(user , user_detail)
    user_detail = 4 , 'Mohan'
    add_user(user , user_detail)

    for item in users:
        print(item)


if __name__ == '__main__':
    main()
