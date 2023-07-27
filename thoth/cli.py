import argparse
from thoth import backup, restore, config
from thoth.utils import get_version


def main():
    parser = argparse.ArgumentParser(
        description="Thoth - your backup and restore utility.")

    subparsers = parser.add_subparsers(dest="command")

    # TODO: Move text to separate file and implement localisaiton

    # Subparser for 'config' command
    config_parser = subparsers.add_parser(
        "config", help="Configure backup settings.")
    config_parser.add_argument(
        "-a, --archive", choices=["lzma", "lz4", "zip"], help="Choose archiving method.")
    config_parser.add_argument(
        "-e, --encryption", choices=["chachapoly", "aes"], help="Choose encryption method.")

    # Subparser for 'backup' command
    backup_parser = subparsers.add_parser(
        "backup", help="Create a backup of the specified file or directory.")
    backup_parser.add_argument(
        "path", type=str, help="Path to the file or directory to backup.")
    backup_parser.add_argument(
        "--archive", choices=["lzma", "lz4", "zip"], help="Override the default archiving method.")
    backup_parser.add_argument(
        "--encryption", choices=["chachapoly", "aes"], help="Override the default encryption method.")
    backup_parser.add_argument(
        "--armor", action="store_true", help="Encrypt the backup.")
    parser.add_argument('-v, --version', action='version', version=get_version())

    # Subparser for 'restore' command
    restore_parser = subparsers.add_parser(
        "restore", help="Restore a backup of the specified file or directory.")
    restore_parser.add_argument(
        "path", type=str, help="Path to the file or directory to restore.")
    restore_parser.add_argument("-i", "--interactive", action="store_true",
                                help="Interactive mode. Choose which backup version to restore.")
    restore_parser.add_argument("backup_id", type=str, nargs="?",
                                help="Specific version of the backup (SHA-256 sum or fragment) to restore. Optional.")

    # Parse args
    args = parser.parse_args()

    # Handling commands in the main function
    if args.command == "config":
        config.ensure_config_exists()
        config.handle_args(args)
    elif args.command == "backup":
        # Assuming you'll have a function like `backup.handle_args(args)` to handle this
        pass  # Replace with actual logic or function call
    elif args.command == "restore":
        # Assuming you'll have a function like `restore.handle_args(args)` to handle this
        pass  # Replace with actual logic or function call
    else:
        parser.print_help()

    # ... Handle other commands like 'backup', 'restore', etc.


if __name__ == "__main__":
    main()
