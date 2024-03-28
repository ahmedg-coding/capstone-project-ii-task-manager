# Capstone Project II - Task Manager

## Description
The Capstone Project II - Task Manager is a Python-based task management system designed to facilitate task organization, assignment, and tracking. Users can register, log in, add tasks, view tasks, mark tasks as complete, edit tasks, generate reports, and display statistics. The system includes user authentication and file storage for user and task data. This project is important as it provides a simple yet effective solution for managing tasks within a team or individual setting. With the features mentioned, this task manager enhances productivity and organization in various environments.

## Files
1. `task_manager.py`: The main Python script implementing the task manager functionality.
2. `tasks.txt`: A text file storing task data.
3. `user.txt`: A text file storing user authentication data.


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Author](#author)
- [License](#license)


## Installation
To install this project locally, follow these steps:  

1. Ensure you have Python installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/).
2. Download or clone the repository to your local machine.
3. Navigate to the project directory in your terminal or command prompt.


## Usage
Once you've installed the project and navigated to the project directory, follow these steps to use it:  

1. Open the entire project folder in a text editor or Python IDE of your choice.

2. Run the `task_manager.py` script by executing the following command:  
   python task_manager.py

3. Follow the on-screen instructions to interact with the task manager system. You can register new users, log in, add tasks, view tasks, mark tasks as complete, edit tasks, generate reports, and display statistics.


## Example
```python
LOGIN  
Username: admin  
Password: password  
Login Successful!  

Select one of the following Options below:  
    r - Registering a user  
    a - Adding a task  
    va - View all tasks  
    vm - View my task  
    gr - Generate reports  
    ds - Display statistics  
    e - Exit  
    : r  
New Username: Alex  
New Password: 123  
Confirm Password: 123  
New user added  

Select one of the following Options below:  
    r - Registering a user  
    a - Adding a task  
    va - View all tasks  
    vm - View my task  
    gr - Generate reports  
    ds - Display statistics  
    e - Exit  
    : a  
Name of person assigned to task: Alex  
Title of Task: Project 1.  
Description of Task: Create a chatbot.  
Due date of task (YYYY-MM-DD): 2025-08-15  
Task successfully added.  

Select one of the following Options below:  
    r - Registering a user  
    a - Adding a task  
    va - View all tasks  
    vm - View my task  
    gr - Generate reports  
    ds - Display statistics  
    e - Exit  
    : gr  

Select one of the following Options below:  
    r - Registering a user  
    a - Adding a task  
    va - View all tasks  
    vm - View my task  
    gr - Generate reports  
    ds - Display statistics  
    e - Exit  
    : ds  
Task Overview:  

Total Number of Tasks: 2  
Total Number of Completed Tasks: 0  
Total Number of Incomplete Tasks: 2  
Overdue Tasks: 1  
Percentage of Incomplete Tasks: 100.00%  
Percentage of Overdue Tasks: 50.00%  


User Overview:  

Total Users: 2  
Total Tasks: 2  

User: admin  
Total Number of Tasks Assigned: 1  
Percentage of Total Number of Tasks: 50.00%  
Percentage of Completed Tasks: 0.00%  
Percentage of Incomplete Tasks: 100.00%  
Percentage of Overdue Tasks: 100.00%  

User: Alex  
Total Number of Tasks Assigned: 1  
Percentage of Total Number of Tasks: 50.00%  
Percentage of Completed Tasks: 0.00%  
Percentage of Incomplete Tasks: 100.00%  
Percentage of Overdue Tasks: 0.00%  


Select one of the following Options below:  
    r - Registering a user  
    a - Adding a task  
    va - View all tasks  
    vm - View my task  
    gr - Generate reports  
    ds - Display statistics  
    e - Exit  
    : va  
Task:            Add functionality to task manager  
Assigned to:     admin  
Date Assigned:   2022-11-22  
Due Date:        2022-12-01  
Task Description:    
 Add additional options and refactor the code.  

Task:            Project 1.  
Assigned to:     Alex  
Date Assigned:   2024-03-26  
Due Date:        2025-08-15  
Task Description:   
 Create a chatbot.  


Select one of the following Options below:  
    r - Registering a user  
    a - Adding a task  
    va - View all tasks  
    vm - View my task  
    gr - Generate reports  
    ds - Display statistics  
    e - Exit  
    : e  
Goodbye!!!  
```


## Author
Ahmed G.


## License
This project is licensed under the [MIT License](LICENSE).
