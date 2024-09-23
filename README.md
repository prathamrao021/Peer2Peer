# Peer-to-Peer Connection System

## Project Overview
This project implements a **multi-threaded peer-to-peer (P2P) communication system** that allows simultaneous connections between multiple clients. Using socket programming in Python, it enables peers to exchange messages and transfer files in a reliable and scalable manner. Each peer can connect to another and handle incoming requests concurrently, ensuring efficient data exchange in a networked environment.

## Features
- **Multiple Peer Handling**: Simultaneously manages connections from multiple peers using Python's multithreading.
- **File Transfer Capability**: Peers can send and receive files, with chunked file transmission and proper completion signaled by an 'END_OF_FILE' marker.
- **Message Exchange**: Peers can communicate via messages in real time.
- **Error Handling**: Robust mechanisms for managing connection errors, timeouts, and file availability.
- **Connection Timeout**: Ensures that peers handle unresponsive connections gracefully.

## Technologies Used
- Python (v3.x)
- Socket Programming (TCP/IP)
- Multithreading

## How It Works
1. **Listening for Connections**: Each peer starts by listening on a specified port, allowing other peers to connect.
2. **Connection to Another Peer**: A peer can connect to another peer by specifying its IP address and port.
3. **File Transfer**: The `transfer <filename>` command initiates file transfer, sending files in chunks until the transfer is completed.
4. **Message Exchange**: Peers can send regular text messages to each other during the connection.
5. **Simultaneous Connections**: Each connection is handled in a separate thread, ensuring multiple clients can connect without blocking.

## Prerequisites
- Python 3.x
- Basic knowledge of TCP/IP and socket programming.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/prathamrao021/Peer2Peer.git
2. Navigate to the project directory:
   ```bash
   cd Peer2Peer

## Usage
1. Run the Listener: Start the peer's listener on a specific port:
   ```bash
   python peer.py 8888
2. Connect to Another Peer: To connect to a different peer, enter the peer's IP address and port number when prompted:
   ```bash
   Enter the peer port number: 9999
3. Send a Message: Type a message to send it to the connected peer:
   ```bash
   Enter message to send: Hello, Peer!
4. Transfer a File: Use the transfer <filename> command to send a file:
   ```bash
   Enter message to send: transfer example.txt

## Example
- Peer A listens on port 8888.
- Peer B connects to Peer A on localhost:8888 and sends a message or transfers a file.
- Both peers can continue to send messages and transfer files concurrently.

## Error Handling
- Timeouts: If a peer is unreachable within a specified time, a timeout error is handled gracefully.
- Connection Refusal: The program handles cases where a peer connection is refused, ensuring a smooth user experience.


   
