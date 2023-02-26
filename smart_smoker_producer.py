import pika
import sys
import time
import pickle
from collections import deque

# limit smoker readings to last 2.5 minuts/5 readings
smoker_deque = deque(maxlen=5)
# limit food a readings to last 10 minutes/20 readings
food_a_deque = deque(maxlen=20)
# limit food b readings to last 10 minutes/20 readings
food_b_deque = deque(maxlen=20)



# define a callback function to be called when a message is received from the smokder
def smoker_callback(ch, method, properties, body):
    """ Define behavior on getting a message."""
    # decode the binary message body to a string
    print(f" [x] Received {pickle.loads(body)} on 01-smoker")
    # acknowledge the message was received and processed 
    # (now it can be deleted from the queue)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # convert message from binary to tuple
    message = pickle.loads(body)
    # add message to deck only if a temp has been recorded
    if isinstance(message[1], float):
        smoker_deque.appendleft(message)

    # only perform checks and send readings when tempuratures are recorded
        # find first item in deque
        cur_smoker_deque_temp = smoker_deque[0]
        # get the current temperature of the smoker
        smoker_temp_current = cur_smoker_deque_temp[1]
   
        # find last item in deque
        last_smoker_deque_temp = smoker_deque[-1]
        # get the last temperature of the smoker
        smoker_temp_last = last_smoker_deque_temp[1]

        # compare first and last message if there has been at least 5 messages sent
        if len(smoker_deque) == 5:
            # find temp difference
            if smoker_temp_last - smoker_temp_current >= 15:
                # send alert if smoker has decreased 15 or more degrees
                print(f"Smoker Alert! Smoker temperature has decease by 15 or more degress in 2.5 minutes from {smoker_temp_last} to {smoker_temp_current}")
            else: # else print the current temp
                print(f"Current smoker tempurature is {smoker_temp_current}")
        else: # print current temp if there are less than 5 readings
            print(f"Current smoker tempurature is {smoker_temp_current}")

# define a callback function to be called when a message is received from food a
def food_a_callback(ch, method, properties, body):
    """ Define behavior on getting a message."""
    # decode the binary message body to a string
    print(f" [x] Received {pickle.loads(body)} on 02-food-A")
    # acknowledge the message was received and processed 
    # (now it can be deleted from the queue)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # convert message from binary to tuple
    message = pickle.loads(body)
    # add message to deck only if a temp has been recorded
    if isinstance(message[1], float):
        food_a_deque.appendleft(message)
        # only perform checks and send readings when tempuratures are recorded
        # find first item in deque
        cur_food_a_deque_temp = food_a_deque[0]
        # get the current temperature of food_a
        food_a_temp_current = cur_food_a_deque_temp[1]
   
        # find last item in deque
        last_food_a_deque_temp = food_a_deque[-1]
        # get the last temperature of food_a
        food_a_temp_last = last_food_a_deque_temp[1]

        # check if 20 messages have been sent to compare food a temps
        if len(food_a_deque) == 20:
            if food_a_temp_last - food_a_temp_current < 1:
                # send alert if food b temp has stalled
                print(f"Food Stall! Food A's temperature has increased less than 1 degree in the last 10 minutes from {food_a_temp_last} to {food_a_temp_current}")
            else: # else print the current temp
                print(f"Current food a tempurature is {food_a_temp_current}")
        else: # else print the current temp
            print(f"Current food a tempurature is {food_a_temp_current}")

# define a callback function to be called when a message is received from food b
def food_b_callback(ch, method, properties, body):
    """ Define behavior on getting a message."""
    # decode the binary message body to a string
    print(f" [x] Received {pickle.loads(body)} on 02-food-B")
    # acknowledge the message was received and processed 
    # (now it can be deleted from the queue)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # convert message from binary to tuple
    message = pickle.loads(body)
    # add message to deck only if a temp has been recorded
    if isinstance(message[1], float):
        food_b_deque.appendleft(message)
        # only perform checks and send readings when tempuratures are recorded
        # find first item in deque
        cur_food_b_deque_temp = food_b_deque[0]
        # get the current temperature of food b
        food_b_temp_current = cur_food_b_deque_temp[1]
   
        # find last item in deque
        last_food_b_deque_temp = food_b_deque[-1]
        # get the last temperature of food b
        food_b_temp_last = last_food_b_deque_temp[1]

        # check if 20 messages have been sent to compare food b temps
        if len(food_b_deque) == 20:
            if food_b_temp_last - food_b_temp_current < 1:
                # send alert if food b temp has stalled
                print(f"Food Stall! Food B's temperature has increased less than 1 degree in the last 10 minutes from {food_b_temp_last} to {food_b_temp_current}")
            else: # else print the current temp
                print(f"Current food b tempurature is {food_b_temp_current}")
        else: # else print the current temp
            print(f"Current food b tempurature is {food_b_temp_current}")




# define a main function to run the program for 3 queues
def main(hn: str):
    """ Continuously listen for task messages on a named queue."""

    # when a statement can go wrong, use a try-except block
    try:
        # try this code, if it works, keep going
        # create a blocking connection to the RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hn))

    # except, if there's an error, do this
    except Exception as e:
        print()
        print("ERROR: connection to RabbitMQ server failed.")
        print(f"Verify the server is running on host={hn}.")
        print(f"The error says: {e}")
        print()
        sys.exit(1)

    try:
        # use the connection to create a communication channel
        channel = connection.channel()

        # use the channel to declare a durable queues
        channel.queue_declare(queue="01-smoker", durable=True)
        channel.queue_declare(queue="02-food-A", durable=True)
        channel.queue_declare(queue="02-food-B", durable=True)

        # set the prefetch count    
        channel.basic_qos(prefetch_count=1) 

        # configure the channel to listen on a specific queue,  
        channel.basic_consume( queue="01-smoker", on_message_callback=smoker_callback)
        channel.basic_consume( queue="02-food-A", on_message_callback=food_a_callback)
        channel.basic_consume( queue="02-food-B", on_message_callback=food_b_callback)

        # print a message to the console for the user
        print(" [*] Ready for work. To exit press CTRL+C")

        # start consuming messages via the communication channel
        channel.start_consuming()

    # except, in the event of an error OR user stops the process, do this
    except Exception as e:
        print()
        print("ERROR: something went wrong.")
        print(f"The error says: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print(" User interrupted continuous listening process.")
        sys.exit(0)
    finally:
        print("\nClosing connection. Goodbye.\n")
        connection.close()


# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    # call the main function with the information needed
    main("localhost")