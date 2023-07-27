## Thoth Backup Utility

Simple and powerful: Thoth makes backing up and restoring your files a breeze.

### Prerequisites

- Python 3.11 or higher

### Setup

1. **Clone the repository**:

```
git clone git@github.com:devlysh/thoth.git
cd thoth
```

2. **Setup a virtual environment**:

```
./create_venv
source venv/bin/activate  # On Windows, use: venv\\Scripts\\activate
```

3. **Install the required packages**:

```
pip install -r requirements.txt
```

4. **Setup Thoth in current session**:

```
./setup.sh
```

### Usage

To configure the backup settings:

```
thoth config
```

This will prompt you to choose the archiving and encryption methods.

For other commands and more detailed options, consult the built-in help:

```
thoth --help
```

### License

🔓 Thoth is proud to be open-source and free. It's licensed under the GPL-3.0 license, which means you're free to use, modify, and distribute it as long as you preserve these freedoms for others.

So, go ahead, dive into the code, and make it even better! 🚀

> For the details, please check out the [full text of the license.](https://github.com/devlysh/thoth/blob/master/LICENCE)

### Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.
