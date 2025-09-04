# How To Export Project and Environment to Other Server Isolated from Internet

To export your project and environment to another server that is isolated from the internet, follow these steps:

1. **Prepare the Project:**
    - Make sure your project is properly configured and all dependencies are installed.
    - Clean up unnecessary files and folders to reduce the size of the project.

        ~~~python
        pip freeze > requirements.txt
        ~~~




2. **Create a Package:**
    - Use a build tool or package manager to create a package of your project.
    - Include all necessary files and dependencies in the package.

        ~~~cmd
        mkdir packages
        ~~~
        
        ~~~python
        pip download -r requirements.txt -d packages
        ~~~


3. **Transfer the Package:**
    - Copy the package to a portable storage device, such as a USB drive.
    - Physically transport the storage device to the isolated server.



4. **Set Up the Environment:**
    - Install the required software and dependencies on the isolated server.
    - Configure the server to match the environment of your original project.

        ~~~cmd
        python -m venv venv
        venv\Scripts\activate
        ~~~


5. **Import the Project:**
    - Copy the package from the storage device to the isolated server.
    - Extract the package and place it in the desired location on the server.

        ~~~python
        pip install --no-index --find-links=packages -r requirements.txt
        ~~~


6. **Test and Verify:**
    - Run tests and verify that the project works correctly on the isolated server.
    - Make any necessary adjustments or configurations to ensure proper functionality.

    ~~~cmd
    python main.py
    ~~~


By following these steps, you can successfully export your project and environment to another server that is isolated from the internet.
