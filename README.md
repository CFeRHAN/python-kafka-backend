# python-kafka decoupled backend

**Handling Tasks Decoupled using kafka-python**

A project that demonstrates how to decouple tasks and achieve real-time processing using Kafka and Python.

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Components](#components)
  - [analytics.py](#analyticspy)
  - [consumer.py](#consumerpy)
  - [email.py](#emailpy)
  - [producer.py](#producerpy)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting Up Kafka](#setting-up-kafka)
  - [Running the Project](#running-the-project)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project demonstrates how to handle tasks in a decoupled manner using the kafka-python library. By leveraging Apache Kafka, a distributed streaming platform, and Python, the project achieves real-time event processing and asynchronous communication between components.

## Project Overview

The project consists of multiple Python scripts that interact with a Kafka cluster. Each script serves a specific purpose and demonstrates a unique aspect of task decoupling using Kafka.

## Components

### analytics.py

A Python script that listens to the "order_confirmed" Kafka topic, processes incoming order details, and updates analytics related to the total number of orders and total revenue generated.

### consumer.py

A Python script that acts as a Kafka consumer for the "order_details" topic. It continuously listens for incoming messages and prints them.

### email.py

A Python script that listens to the "order_confirmed" Kafka topic and sends email notifications to customers whenever an order is confirmed. It keeps track of unique email addresses to avoid duplicate emails.

### producer.py

A Python script that acts as a Kafka producer. It generates synthetic order details and sends them to the "order_details" topic for processing by other components.

## Getting Started

### Prerequisites

- Python (>= 3.6)
- Docker (if running the project in a containerized environment)

### Setting Up Kafka

1. Clone the repository and navigate to the project directory.

2. Run the following command to start the Kafka and Zookeeper services using Docker Compose:


[docker-compose up -d]


### Running the Project

1. Open a terminal and navigate to the project directory.

2. To run the `producer.py` script:


[python producer.py]


This script will generate synthetic order details and publish them to the "order_details" Kafka topic.

3. To run any of the consumer scripts (e.g., `consumer.py`):

[python consumer.py]


The consumer script will listen to the specified Kafka topic and print the incoming messages.

4. To run the `email.py` script:

[python email.py]


This script will listen to the "order_confirmed" Kafka topic and send email notifications to customers whenever an order is confirmed.

5. To run the `analytics.py` script:

[python analytics.py]


The analytics script will listen to the "order_confirmed" Kafka topic, process incoming order details, and update the total number of orders and revenue.

## Contributing

Contributions to the project are welcome. If you find any issues or have suggestions for improvement, please feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

