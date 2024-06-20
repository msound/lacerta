from diagrams import Diagram
from diagrams.c4 import Person, Relationship, System
from diagrams import Node

def main():
    graph_attr = {
        "splines": "curves",
    }
    with Diagram("Context diagram for Lacerta", filename="context", direction="TB", graph_attr=graph_attr):

        user = Person("User", description="A user of Lacerta")
        emerg = Person("Emergency Contact", "A friend or family member of the User")
        sys = System("Lacerta System", description="")
        
        user >> Relationship("1. configures emergency contacts, and periodically checks-in") >> sys
        user << Relationship("2. reminds if a check-in is missed") << sys
        emerg << Relationship("3. alerts if user has missed a check-in despite reminders") << sys
        user << Relationship("4. manually confirms that the User is ok") << emerg

if __name__ == "__main__":
    main()
