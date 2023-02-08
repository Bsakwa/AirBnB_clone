# AirBnB clone - The console

This Group Project is part of our portfolio project at ALX x Holberton. The first part of the project required us to create a command interpreter that will manage our AirBnB objects.

Our command Interpreter should be able to perform the following operations:

	* Create a new Object(ex: a new User or a New Place)
	* Retrieve an object from a file, database etc
	* Do operations on objects
	* Update attributes of an object
	* Destroy an object

## Learning Objectives
```
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
```

### Execution

Our shell should be able to work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
