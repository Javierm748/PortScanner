# PortScanner
An application that lets the user input an IP address and parameters of ports and will allow the user to see if those ports are either open or closed.
# Overview

As for this program I am trying to accomplish a code that functions as a port scanner, the port scanner code will examine the give IP address that the user inputs and will determine if the port is open or closed. 

The program is written so that the user can input an IP address of their desire and from there it will iterate through ports (however many ports the user input) The code will give options to start from a given port and end on a given port and will scan all of them in between. There is also a nice touch added which provides live progress through percentages of each port and its progress before the user gets the notice of wether the port is open or closed.

The purpose of writting this software is so that people can not only check if ports are open withing a certain IP address. But to teach people why are ports closed, why are they open, and the layers of the TCP/IP networking protocol, understanding the layers from the application (HTTP), to transport (TCP), Internet (IP), to LINK (MAC).

Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the sofware

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

Architecture used is client/server

In this code I am using a TCP protocol in which through the IP it will scan trough transport (TCP) all the way to the applications which those ports are located in and then come back with the results.


# Development Environment

1. Integrated Development Environment (IDE)
Tool Examples: Visual Studio Code

2. Programming Language
Tool Example: Python

3. Version Control System
Tool Example: Git

4. Package Management System
Tool Example: pip (Python package installer), sys, socket

5. Networking Tools
Tool Examples: Wireshark

6. Testing Framework
Tool Example: unittest (or pytest) in Python

7. Documentation Tools
Tool Examples: Markdown editors

8. Debugging Tools
Tool Examples: Built-in debuggers in IDEs

9. Command Line Interface (CLI)
Tool Examples: Terminal


Programming language I used was Python

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python.org](https://docs.python.org/3/library/socket.html)
* [W3 Schools](https://www.w3schools.com/cybersecurity/cybersecurity_networking.php)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Time management.
* Interactiveness.
* More detailed comments.
