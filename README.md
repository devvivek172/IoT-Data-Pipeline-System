# IoT Data Pipeline System

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)  
![License](https://img.shields.io/badge/license-MIT-blue)  
![Dockerized](https://img.shields.io/badge/docker-ready-blue)  

---

## Project Overview

This project implements a **real-time IoT data pipeline** built with **Python**, **MQTT**, **AWS IoT Core**, and **Docker**. It securely transmits device data to the cloud, validates it, and prepares it for further processing. 

This pipeline can be used for any real-time data processing scenario, from IoT devices in industrial setups to smart home systems.

---

## Features
- 🛰️ **Real-Time Data Streaming**: Devices send data to AWS IoT using MQTT.
- 🛡️ **Automated Data Validation**: Ensures data integrity and accuracy.
- 🐳 **Dockerized**: Fully containerized for easy deployment anywhere.
- ☁️ **AWS IoT Core Integration**: Leverages AWS IoT for secure device communication.
- ⚙️ **CI/CD Ready**: Built with GitHub Actions for continuous integration.

---

## Tech Stack
- **Python 3.11**
- **paho-mqtt** (for MQTT client)
- **boto3** (AWS SDK for Python)
- **AWS IoT Core**
- **Docker**
- **GitHub Actions** (for CI/CD)

---

## Architecture

```plaintext
[ IoT Devices ]
       |
    (MQTT Publish)
       ↓
[ AWS IoT Core Broker ]
       |
    (Subscribe)
       ↓
[ Python MQTT Client ]
       |
    (Validation)
       ↓
[ Processed Data ]
