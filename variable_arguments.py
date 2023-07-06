def membership_assignment(
        user_name, user_phone, user_id, user_credit_card,
        *favorite_movie_kind, **other_user_infromation
    ):
    print(f"user_name: {user_name}")
    print(f"user_phone: {user_phone}")
    print(f"user_id: {user_id}")
    print(f"user_credit_card: {user_credit_card}")

    for kind in favorite_movie_kind:
        print("Movie Kind: ", kind)

    for key, value in other_user_infromation.items():
        print(f"Key:{key}, Value:{value}")

if __name__ == '__main__':

    membership_assignment(
        'Chung Yi',
        '09123456789',
        'A123456789',
        '123456789',
        'Horror Movie', 'Comedy', 'DC', 'Cartoon', #  *favorite_movie_kind
        user_address='Taipei', user_hometown='Taichung'
    )

