def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--is_create_database', type=bool, default=False,
                        help='Whether to create the database or not')
    args = parser.parse_args()
    from driver import Driver
    Driver(args.is_create_database).start()


if __name__ == "__main__":
    main()
