# Backend Repo for Sweep Android Application
This is the backend repository for Sweep, an Android application that simplifies communication between general service firms and workers (cleaning, gardening, plumbing, etc.) and consumers.

## Getting Started
To set up the Flask Python project, follow the steps below:

1. Clone the repository locally using the command:

```
git clone https://github.com/username/sweep-backend.git
```

2. Install pyenv according to your operating system:

- **MacOS/Linux:** Install using Homebrew by running the command:

```
brew install pyenv
```

- **Windows:** Install using pyenv-win by downloading the installer from https://github.com/pyenv-win/pyenv-win/releases and following the instructions.

3. Install Python 3.9 through pyenv by running the command:

```
pyenv install 3.9.0
```

4. Configure a Python 3.9 interpreter:

- **PyCharm:** Open the project in PyCharm, go to File -> Settings -> Project: Sweep -> Python Interpreter. Click on the gear icon and select "Add...". Select "Existing environment" and navigate to the Python 3.9 interpreter installed through pyenv (e.g. ~/.pyenv/versions/3.9.0/bin/python3.9).

- **Visual Studio Code:** Open the project in Visual Studio Code, go to View -> Command Palette and type "Python: Select Interpreter". Select the Python 3.9 interpreter installed through pyenv (e.g. ~/.pyenv/versions/3.9.0/bin/python3.9).

5. Configure environment variables into IDE:

- **PyCharm:** Go to Run -> Edit Configurations. In the "Environment variables" section, add the corresponding environment variables.

- **Visual Studio Code:** Go to the Run view, click on the gear icon to create a launch.json file. In the "configurations" array, add the following configuration:

```
{
    "name": "Python: Flask",
    "type": "python",
    "request": "launch",
    "module": "flask",
    "env": {
        "ATLAS_MONGODB_PASSWORD": "",
        "AWS_ACCESS_KEY_ID": "",
        "AWS_CLOUDFRONT_DISTRIBUTION_ID": "",
        "AWS_CLOUDFRONT_DOMAIN_NAME": "",
        "AWS_S3_BUCKET": "",
        "AWS_SECRET_ACCESS_KEY": ""
    },
    "args": [
        "run",
        "--no-debugger",
        "--no-reload"
    ],
    "jinja": true
}
```
## Credits
This app was developed by Khaled Chehabeddine, Jamil Shoujah, Adam Harb, & Hashem Shibli.
