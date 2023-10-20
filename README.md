# TA Scheduling Web Application

Project Description-

This web application was developed using Python to modernize and replace the outdated paper-based system for scheduling graduate student Teaching Assistants (TAs) in the Computer Science department. It introduced a digital platform for efficient scheduling, improved communication, and enhanced data reliability.
Key Features

    User Roles: The system includes three user roles: Supervisor/Administrator (department chair), Instructor, and TA.

    Supervisor/Administrator Responsibilities:
        Created and managed courses.
        Managed user accounts (create, delete, edit).
        Sent notifications to users via UWM email.
        Accessed all data in the system.
        Assigned instructors to courses.
        Assigned TAs to courses, specifying the number of labs or grader status.
        Assigned TAs to specific lab sections.

    Instructor Responsibilities:
        Edited their own contact information (excluding course assignments).
        Viewed course assignments.
        Viewed TA assignments for all TAs.
        Sent notifications to their TAs via UWM email.
        Assigned their TAs to specific lab sections.
        Read public contact information of all users.

    TA Responsibilities:
        Edited their own contact information (excluding course assignments).
        Viewed TA assignments for all TAs.
        Read public contact information of all users.

    Secure Data Privacy System:
        Personal phone numbers and home addresses of TAs and instructors were kept private.
        Access to this information was restricted to the administrator and supervisor only.

Benefits

    Efficiency: This system significantly improved efficiency and accuracy by eliminating paper forms and manual email assignments.

    Communication: Enhanced communication between department staff and TAs through the web application, making it easier to send notifications and updates.

    Streamlined Scheduling: The scheduling process was streamlined, allowing for easy updates and changes to the schedule of classes.

    Data Reliability: Increased data reliability and reduced errors by centralizing all scheduling information in a single system.

    Installation-
1. Apply Migrations

Apply the initial migrations:

python3 manage.py migrate
2. Create the Superuser

Create a superuser:

python3 manage.py createsuperuser
3. Populate the Database (Optional)

Add test data to the database using the populate.py script:

python3 manage.py shell

>>> exec(open('populate.py').read())

4. Run the Server

python3 manage.py runserver
