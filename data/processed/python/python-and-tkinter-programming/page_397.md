---
source_image: page_397.png
page_number: 397
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.29
tokens: 8313
characters: 2043
timestamp: 2025-12-24T00:42:34.355609
finish_reason: stop
---

sys.exit(2)
if sys.argv[1] == '-s':
    server=Server()
elif sys.argv[1] == '-c':
    root = Tk()
    example = GUIClient(root)
    root.mainloop()

Code comments

① I’ve made very little mention of sockets in this book, and some readers may not be familiar with this facility. A brief mention here is warranted. Here we are setting up to send a message over a socket, which is a basic network facility available on most operating systems. Essentially, we connect to a numbered port on a particular host system, and then we send and receive messages using either the UDP (datagram) or TCP (stream) protocols. In this example we are using datagrams*.

② The client side of the example sets up a socket using the same port as the server, and then it registers the filehandler which will be called when one of three events occur on the socket. The possible values for the event mask are READABLE, which occurs when a socket receives data; WRITABLE, which occurs when a socket is written to and EXCEPTION, which occurs when any error occurs. We set up an after callback to write text to the window every five seconds.

③ The handler for the file event is very simple. The mask argument specifies the type of file operation that resulted in the call, so a single handler could act for all types of file operations.

To run the example, first start the server as a separate process:

% python client_server.py -s &

Then start the client process:

% python client_server.py -c

Figure 18.7 shows the screen you can see when the example is run.

* The UDP protocol is a connectionless protocol in which packets are sent into the network for delivery to a particular host with a specified port. No confirmation is sent to the sender that the packet has been received and no mechanism for automatic retransmission of messages exists if there are problems. Thus, there is no guarantee that a datagram will be delivered to it’s destination. Datagrams are normally used for noncritical messages, typically within a LAN to avoid costly connection overhead.