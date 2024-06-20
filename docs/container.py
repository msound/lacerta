from diagrams import Diagram
from diagrams.c4 import Container, Database, Person, Relationship, SystemBoundary, System
from diagrams import Node

def main():
    graph_attr = {
        "splines": "curves",
    }
    with Diagram("Container diagram for Lacerta System", filename="container", direction="TB", graph_attr=graph_attr):
        user = Person("User", description="A user of Lacerta")
        emerg = Person("Emergency Contact", "A friend or family member of the User")
        with SystemBoundary("Lacerta application"):
            mobile_app = Container("Mobile App",
                                   technology="Flutter",
                                   description="Provides ability for user to check-in periodically, and also to configure emergency contacts")
            backend = Container("Backend",
                                technology="Go",
                                description="Backend API application allows user to check-in, and configure emergency contacts")
            daemon = Container("Daemon",
                               technology="Go",
                               description="Constantly checks if any user has missed a check-in")
            db = Database("Database",
                          technology="MongoDB",
                          description="Database to store configuration and check-in times")

        email = System("Email", description="SendGrid Transactional Email Service", external=True)
        push = System("Push Notification", description="Firebase Cloud Messaging", external=True)

        user >> Relationship("checks-in and configures emergency contacts using") >> mobile_app
        mobile_app >> Relationship("make API calls to") >> backend
        backend >> Relationship("reads from and writes to", reverse=True) >> db
        daemon << Relationship("reads from") << db
        daemon >> Relationship("triggers email reminders or email alerts") >> email
        daemon >> Relationship("triggers push notification reminders to check-in") >> push
        user << Relationship("reminder emails to check-in") << email
        user << Relationship("reminder messages to check-in") << push
        emerg << Relationship("alert email about user") << email
        user << Relationship("manual check-in to verify if user is ok") << emerg

if __name__ == "__main__":
    main()
