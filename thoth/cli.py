import argparse
from thoth import config, files
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

    # Subparser for 'files' command
    files_parser = subparsers.add_parser(
        "files", help="Backup or restore files.")
    files_parser.add_argument("operation", choices=[
                              "backup", "restore", "list", "cp"], help="Specify the operation.")
    files_parser.add_argument(
        "path", type=str, help="Path to the file or directory for operation.")
    files_parser.add_argument(
        "--archive", choices=["lzma", "lz4", "zip"], help="Choose archiving method.")
    files_parser.add_argument(
        "--encryption", choices=["chachapoly", "aes"], help="Choose encryption method.")
    files_parser.add_argument(
        "--armor", action="store_true", help="Encrypt the backup.")
    files_parser.add_argument(
        "-i", "--interactive", action="store_true", help="Interactive mode for restore.")
    files_parser.add_argument(
        "backup_id", type=str, nargs="?", help="Specific backup ID for some operations.")
    files_parser.add_argument(
        "--cron", type=str, help="Set up a cron job for this command.")
    files_parser.add_argument(
        "--pack", action="store_true", help="Pack the backup when copying.")
    files_parser.add_argument(
        "--unpack", action="store_true", help="Unpack the backup when copying.")

    # Parse args
    args = parser.parse_args()

    # Handling commands in the main function
    if args.command == "config":
        config.ensure_config_exists()
        config.handle_args(args)
    elif args.command == "files":
        files.handle_args(args)
    else:
        parser.print_help()

    # ... Handle other commands like 'backup', 'restore', etc.


if __name__ == "__main__":
    main()
