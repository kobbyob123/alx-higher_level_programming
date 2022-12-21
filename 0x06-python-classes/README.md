# Classes & Object Oriented Programming (OOP)

A class is a representation of an entire object or simply the generalization of an entire "thing".

* An example :

```text
There is a general type of animal called Dogs. But then there are classes of dogs based on their differences

Some dogs are big, others are small, they vary by color and their purpose.
```

In the same way, classes represent a generalization and objects represent a specialization

A class is defined as :

```Python
class Robot():
    """This is a Robot Class"""
    
    def __init__(self, model, color):
        """This is where the classes updates itself with the info given"""
        self.model = model
        self.color = color

    def talk(self):
        """Introduces itself"""
        print("Hello human, my name is {} and I'm {} in color.".format(self.name, self.color))

 a = Robot("DX-149-T", "Green")
 a.talk()
```