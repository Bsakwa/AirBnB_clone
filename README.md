# AirBnB :house: clone - The console :computer:

This Group Project is part of our portfolio project at ALX x Holberton. The first part of the project required us to create a command interpreter that will manage our AirBnB objects.

Our command Interpreter should be able to perform the following operations:

	* Create a new Object(ex: a new User or a New Place)
	* Retrieve an object from a file, database etc
	* Do operations on objects
	* Update attributes of an object
	* Destroy an object

## Learning Objectives :heavy_check_mark:
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

* **show**
	* Usage: `show <class> <id>`: Shows the ID of the class created
```
(hbnb) show amenities id
** class doesn't exist **
(hbnb) create User
759bd23a-bfd1-40d9-bb8e-8dce547cc439
(hbnb) show User 759bd23a-bfd1-40d9-bb8e-8dce547cc439
[User] (759bd23a-bfd1-40d9-bb8e-8dce547cc439) {'id': '759bd23a-bfd1-40d9-bb8e-8dce547cc439', 'created_at': datetime.datetime(2023, 2, 21, 11, 54, 28, 620364), 'updated_at': datetime.datetime(2023, 2, 21, 11, 54, 28, 620739)}
(hbnb)
```

* **destroy**
	* Usage: `destroy <class> id`: Deletes an a created instance of a ckass
```
hbnb) destroy User 759bd23a-bfd1-40d9-bb8e-8dce547cc439

vagrant@ubuntu-focal:/home/AirBnB_clone$  cat file.json ; echo ""
{}
```

* **all** 
	* Usage: `all` or `all <class>` : Prints all the instances created of a class or instances of every class
```
(hbnb) create BaseModel
97c28b24-eb5f-448e-bbcc-89ca40dc9284
(hbnb) create User
616a992e-6872-492a-a1cd-7d04626dde9f
(hbnb) all
["[BaseModel] (97c28b24-eb5f-448e-bbcc-89ca40dc9284) {'id': '97c28b24-eb5f-448e-bbcc-89ca40dc9284', 'created_at': datetime.datetime(2023, 2, 21, 12, 0, 50, 681903), 'updated_at': datetime.datetime(2023, 2, 21, 12, 0, 50, 681937)}", "[User] (616a992e-6872-492a-a1cd-7d04626dde9f) {'id': '616a992e-6872-492a-a1cd-7d04626dde9f', 'created_at': datetime.datetime(2023, 2, 21, 12, 0, 59, 676801), 'updated_at': datetime.datetime(2023, 2, 21, 12, 0, 59, 676834)}"]
(hbnb)hbnb) all User
["[User] (616a992e-6872-492a-a1cd-7d04626dde9f) {'id': '616a992e-6872-492a-a1cd-7d04626dde9f', 'created_at': datetime.datetime(2023, 2, 21, 12, 0, 59, 676801), 'updated_at': datetime.datetime(2023, 2, 21, 12, 0, 59, 676834)}"]
(hbnb)
```
* **count**
	* Usage: `count <class>`: Retrieved the number of instances of a class
```
(hbnb) count User
1
(hbnb) count BaseModel
1
(hbnb) create User
a8a90d63-af98-49bb-a678-8950e26bff8a
(hbnb) count User
2
(hbnb)
```
* **update**
	* Usage: update `<class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>)`
```
(hbnb) create User
ee57c380-165a-476d-912f-573dcbb6c859
(hbnb) update User ee57c380-165a-476d-912f-573dcbb6c859 first_name "Sakwa"
(hbnb) show User ee57c380-165a-476d-912f-573dcbb6c859
[User] (ee57c380-165a-476d-912f-573dcbb6c859) {'id': 'ee57c380-165a-476d-912f-573dcbb6c859', 'created_at': datetime.datetime(2023, 2, 21, 12, 6, 46, 971633), 'updated_at': datetime.datetime(2023, 2, 21, 12, 6, 46, 971683), 'first_name': 'Sakwa'}
(hbnb)
```

## Testing
A set of Tests were used for the project. Simultaneously run them using this command
```
$ python3 unittest -m discover tests
```
Or run a single test;
```
$ python3 unittest -m tests/test_console.py
```


