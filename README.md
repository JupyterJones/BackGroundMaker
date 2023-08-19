# BackGroundMaker
Flask that makes background videos from Thumbnails in the cache directory
# Setting up a Basic Flask App with Virtual Environment

This guide will walk you through the process of setting up a basic Flask application using a virtual environment on a Linux system. This approach helps isolate your project's dependencies from the system-wide Python environment.

## Prerequisites

- Linux computer
- Python 3.9 or higher installed (recommended)
- Pip package manager installed

## Steps

1. Open a Terminal Window:
   Open a terminal on your Linux computer.

2. Update Pip (Optional but Recommended):
   Run the following command to update `pip` to the latest version:

pip install --upgrade pip

3. Install Virtualenv:
Install the `virtualenv` package using pip:

pip install virtualenv

4. Create a Virtual Environment:
Navigate to your project directory and create a virtual environment:

virtualenv -p /usr/bin/python3.9 venv


5. Activate the Virtual Environment:
Activate the virtual environment using:

source venv/bin/activate

6. Install Flask and Other Packages:
Inside the activated virtual environment, install Flask and other required packages:

pip install -r requirements.txt

7. Run Your Flask App:
Start your Flask app using the development server:

flask run

Access your app in a web browser at http://localhost:5000.

9. Deactivate the Virtual Environment:
When you're done, deactivate the virtual environment:

deactivate


## Additional Notes

- Remember to activate the virtual environment every time you work on your Flask app.
- This setup ensures that your project's dependencies don't conflict with system-wide packages.
- Feel free to customize your Flask app, add routes, templates, and more.

If you have any questions or need further assistance, don't hesitate to reach out.

