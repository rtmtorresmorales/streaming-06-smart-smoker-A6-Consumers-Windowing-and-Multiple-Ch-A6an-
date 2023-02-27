# streaming-06-smart-smoker-A6-Consumers-Windowing-and-Multiple-Ch-A6an-
Ramón Torres
February 27, 2023
# Github repository: https://github.com/rtmtorresmorales/streaming-06-smart-smoker-A6-Consumers-Windowing-and-Multiple-Ch-A6an-
# The Problem / Challenge To Solve: Smart Smoker System
•	Read about the Smart Smoker system here: Smart Smoker
•	We read one value every half minute. (sleep_secs = 30)
smoker-temps.csv has 4 columns:
•	[0] Time = Date-time stamp for the sensor reading
•	[1] Channel1 = Smoker Temp --> send to message queue "01-smoker"
•	[2] Channe2 = Food A Temp --> send to message queue "02-food-A"
•	[3] Channe3 = Food B Temp --> send to message queue "02-food-B"
We want know if:
1.	The smoker temperature decreases by more than 15 degrees F in 2.5 minutes (smoker alert!)
2.	Any food temperature changes less than 1 degree F in 10 minutes (food stall!)
Time Windows
•	Smoker time window is 2.5 minutes
•	Food time window is 10 minutes
Deque Max Length
•	At one reading every 1/2 minute, the smoker deque max length is 5 (2.5 min * 1 reading/0.5 min)
•	At one reading every 1/2 minute, the food deque max length is 20 (10 min * 1 reading/0.5 min) 
Condition To monitor
•	If smoker temp decreases by 15 F or more in 2.5 min (or 5 readings)  --> smoker alert!
•	If food temp change in temp is 1 F or less in 10 min (or 20 readings)  --> food stall alert!
Requirements
•	RabbitMQ server running
•	pika installed in your active environment
RabbitMQ Admin
•	See http://localhost:15672/Links to an external site.
General Design 
1.	How many producer processes do you need to read the temperatures: One producer, built last project.
2.	How many listening queues do we use: three queues, named as listed above.
3.	How many listening callback functions do we need (Hint: one per queue): Three callback functions are needed.
 General Instructions:
________________________________________
# Task 1. Open Your Existing Project
1.	On your machine, open your existing streaming-05-getting-started repo in VS Code.
2.	Create a file for your consumer (or 3 files if you'd like to use 3 consumers).
 
# Task 2. Design and Implement Each Consumer
1.	Design and implement each bbq consumer. You could have one. You could have 3.  More detailed help provided in links below. 
2.	Use the logic, approach, and structure from prior modules (use the recommended versions).
3.	Modifying them to serve your purpose IS part of the assignment.
4.	Do not start from scratch - do not search for code - do not use a notebook.
5.	Use comments in the code and repo to explain your work. 
6.	Use docstring comments and add your name and date to your README and your code files. 
 
# Task 3. Professionally Present your Project
1.	Explain your project in the README.
2.	Include your name, date.
3.	Include prerequisites and how to run your code. 
4.	Explain and show how your project works. 
5.	Tell us what commands are needed. Use code fencing in GitHub or backtics for inline code to share commands.
6.	Display screenshots of your console with the producer and consumer running.
7.	Display screenshots of at least one interesting part of the RabbitMQ console. 
Requirements
In your callback function, make sure you generate alerts - there will be a smoker alert and both Food A and Food B will stall. 
Your README.md screenshots must show 4 concurrent processes:
1.	Producer (getting the temperature readings)
2.	Smoker monitor
3.	Food A monitor
4.	Food B monitor
In addition, you must show at least 3 significant events.
Run each terminal long enough that you can show the significant events in your screenshots:
1.	Visible Smoker Alert with timestamp
2.	Visible Food A stall with timestamp
3.	Visible Food B stall with timestamp
# Data
Temperatures readings from a BBQ smoker, for Food A and Food B, time stamp temparature readings
# Output
String binary with time and temperature reading
# Programs
One csv data file, one smoker messages producer, convert and send messages, one somker consumer reads messages and prints alerts.
# General instructions
1. Open two terminals
2. csv file access
3. run smoker message generator on one terminal
4. run smoker consumer on the other terminal
5.Ctl-C will stop the process

# Part 1 - Project 
1.	Clickable link to your public GitHub repo(s) with custom README and displayed screenshots:  https://github.com/rtmtorresmorales/streaming-06-smart-smoker-A6-Consumers-Windowing-and-Multiple-Ch-A6an-
2.	About how long did you spend this module:  about five hours
3.	Did you use one consumer with 3 queues (or 3 consumers each with one queue): Actually, I looked for both options, but the option of one consumer is a more efficient manner to manage the process and computing resources.
4.	Why:  Actually, I looked for both options, but the option of one consumer is a more efficient manner to manage the process and computing resources.
5.	When did a Smoker Alert occur? Readings every 2.5mins
6.	When did a Food A stall occur: no message, some issues and limit operation.
7.	When did a Food B stall occur: no message, some issues and limit operation.
8.	What was most difficult about this module:   Certainly, some of the coding was tricky and the configuration issues mentioned before. Still having configuration issues with my laptop, some slow internet connection, cut off the connection.  I was running a duplicate Python scenarios creatin some issues in VS Code Editor.  Will reconfigure the entire laptop next week before next class starts.  Some issues debugging limit operation. 
9.	What was most interesting:  dealing with the concurrent process
10.	In a real system, you'd want to get alerts from your smart smoker - maybe a text message.
1.	Did you experiment with adding alerts to the project and getting an email or text when the smoker alerted? I started reviewing the process, did not test it.  But I strongly believe in early alerts of any processes to take early action of control and monitoring.
2.	Would you be able to add this feature if implementing a similar system in real life? This will certainly will a significant impact on society, families, and quality of life.  These alarms may monitor by the patient, family, doctors and even a health call center.  I could image having a call center to monitor this another vital signs. In addition, to financial applications, account balances, deposits, production stoppages, stock alerts, order processing.
3.	Optional bonus: Did you successfully implement an alert (and clearly show it in your README.md and repo)?  Like I mentioned before started looking at options but did not implement an option. 
# Part 2 - Self Assessment
From the Module 4: Overview, paste the numbered list of objectives and assess your ability on each as "Highly proficient", "Proficient", or "Not Proficient":
At the end of this module students will be able to:
1.	Present information about the state of the art in streaming data. (L07) Proficient.
2.	Discuss how tools and technologies can be used in conjunction with each other to work with streaming data. (L07) Proficient.


![image](https://user-images.githubusercontent.com/111456228/221131576-e2739cc6-1f94-4ea9-989a-e115d9735e98.png)

![image](https://user-images.githubusercontent.com/111456228/221131613-eae49360-d84d-4e95-8adc-02a74b16b42d.png)
