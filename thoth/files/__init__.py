# thoth/files/__init__.py

from .backup import backup_file_or_directory
from .restore import restore_file_or_directory
from .utils import list_backups


def handle_args(args):
    if args.action == 'backup':
        pass
    elif args.action == 'restore':
        pass
    elif args.action == 'list':
        pass

    # For debugging
    print(args)
