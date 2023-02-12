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
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
```

To use the AirBnB console in interactive mode run the executable:
```
$ ./console.py
```

To quit the command interpreter use the `quit` or `EOF` commands
```
$ ./console.py
(hbnb) quit
$
```
```
$ ./console.py
(hbnb) EOF
$
```
## Console Commands

Our AirBnB command interpreter supports the following commands as outlined below

* **create**
	* Usage: `create <class>` : Creates a new instance of the given class, prints outs it's ID and saves it to the file `file.json`
```
(hbnb) create BaseModel
4c0f4d59-d30d-4a92-a9fb-aac6815fe2da
(hbnb) quit

$ cat file.json ; echo ""
{"BaseModel.4c0f4d59-d30d-4a92-a9fb-aac6815fe2da": {"id": "4c0f4d59-d30d-4a92-a9fb-aac6815fe2da", "created_at": "2023-02-12T13:14:24.854589", "updated_at": "2023-02-12T13:14:24.854621", "__class__": "BaseModel"}}
```


