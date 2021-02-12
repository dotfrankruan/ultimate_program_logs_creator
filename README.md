# Introduce
This is the ULTIMATE PROGRAM LOGS CREATOR made by ORWTMC Inc.
<br/>
The world's most friendly logs made by program(yet)!
# Show time XD
```
[21:5:44] [INFO] Program is running...
[21:6:5] [WARNING] User doesn't provided the value, using default!
[21:6:24] [FATAL] User terminated this program, shutting down...
[21:6:43] [INFO] System shutted down.
```

# How to use
**It's pretty simple, just add a line in your program**
```python
import uplc
```
_Never change 'uplc' to something else._
<br/>

# Examples
Now I'll give you a sample.
```python
import uplc
logs = uplc.LogsCreator() # Default name is DefaultLog, the extension is ".ulog", you can't change it. You can add a string inside of it. e.g. logs = uplc.LogsCreator("MyAwesomeLogs")
logs.write("Program is running normally.", "info", 3)
# The result is: [xx:xx:xx] [INFO] Program is running normally.
logs.close() # VERY IMPORTANT!!! OTHERWISE THE LOG WILL NOT BE SAVED!!!
```

## Usage
1. You have to import it and define a variable(e.g. logs), point to `LogsCreator` class.
<br/>
2. You can use `logs.write` to create a row.
<br/>
```python
logs.write(LOGS_TEXT, TYPE(DEBUG/INFO/WARNING/FATAL), TIME_ACCURACY)
```
Time Accuracy:
<br/>
0: YYYYMMDDHHMMSS
<br/>
1: MMDDHHMMSS
<br/>
2: DDHHMMSS
<br/>
3: HHMMSS
## Important
**Do not forget to use `logs.close()` to close the file, otherwise you will lose everything you created.**
