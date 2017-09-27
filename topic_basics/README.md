# Topic Basics


## Command Line

Subscribe to a topic with:
```bash
$ rostopic echo intval  
```

Publish to a topic with:
```bash
# Publish once
$ rostopic pub intval std_msgs/Int32 999 -1
# Publish at 10 hz
$ rostopic pub intval std_msgs/Int32 999 -r 10
```

## Programmatic 

Run *topic_publisher.py* with:
```bash
$ rosrun topic_basics topic_publisher.py
```

Run *topic_subscriber.py* with:
```bash
$ rosrun topic_basics topic_subscriber.py
```

## Examine Topics 

Inspect the topic *counter* from the CLI with:
```bash
$ rostopic list
$ rostopic echo counter
$ rostopic echo counter -n 10
$ rostopic info counter
$ rostopic find std_msgs/Int32
$ rostopic bw counter
$ rostopic hz counter
```

Inspect the **counter** topic sfrom *rqt* with:
```bash
$ rqt
# Select Plugins-->Topics-->Topic Monitor
```


## Latched Topics

Run *latched_topic_publisher.py* with:
```bash
$ rosrun topic_basics latched_topic_publisher.py
```

Run *topic_subscriber.py* with:
```bash
$ rosrun topic_basics topic_subscriber.py
```




