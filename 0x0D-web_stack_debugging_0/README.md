###

This is my Webstack Debugging Project.

This project contains basic concept about Networking, Docker and how to use docker to debug.

This project contains one file called 0-give_me_a_page this file contains commands that was used to fix the issue.

The first command, echo "ServerName localhost" >> /etc/apache2/apache2.conf appends the line "ServerName localhost" to the end of the file located at /etc/apache2/apache2.conf while the second command sudo /etc/init.d/apache2 start invokes the Apache init script to start the service it uses the traditional SysV init system for service management.
