def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-c', type=bool, default=False, help='Whether to create the database or not')
    args = parser.parse_args()
    from local_driver import LocalDriver
    LocalDriver(args.c).start()


if __name__ == "__main__":
    main()
