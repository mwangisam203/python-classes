****
This project demonstrates Object-Oriented Programming (OOP) in Python using geometric shapes. It focuses on inheritance, method overriding, and the use of the super() function to reuse parent class logic efficiently.

The program defines a base Shape class and extends it into specific shapes that can calculate their own area.

Key Concepts
Inheritance

Shape is the parent class.

Circle, Square, and Triangle are child classes.

Child classes inherit common attributes like color, filled, and unit.

super() Function

super() is used inside child classes to call the parent class’s __init__ method.

This avoids duplicating code and ensures shared attributes are initialized correctly.

*****Method Overriding

The area() method is defined in the parent class but implemented differently in each child class.

Each shape calculates its area using its own formula.