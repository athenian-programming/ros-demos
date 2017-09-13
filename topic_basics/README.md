# Topics Demo

## Non-latched Topics

Run *topic_publisher.py* with:
```bash
$ ./topic_publisher.py
```

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

Inspect the topic *counter* from *rqt* with:
```bash
$ rqt
# Select Plugins-->Topics-->Topic Monitor
```

Run *topic_subscriber.py* with:
```bash
$ ./topic_subscriber.py
```

## Latched Topics

Run *latched_topic_publisher.py* with:
```bash
$ ./latched_topic_publisher.py
```

Run *topic_subscriber.py* with:
```bash
$ ./topic_subscriber.py
```




