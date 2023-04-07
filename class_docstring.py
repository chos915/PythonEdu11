# -*- coding: utf-8 -*-

class Person:
    """
    사람을 표현하는 클래스

    '''

    Attributes
    ----------
    name : str
        name of the person
    
    age : int
        age of the person

    Methods
    ----------
    info(extrainfo = ""):
        Print the person's name, age and etc
    """
    def __init__(self, name, age):
        """
        Constructs all the necessary attributes for the person object

        Parameters
        ----------
            name : str
                name of the person
            age : int
                age of the person
        """
        self.name = name # 외부에서 값이 입력, 클래스 내부의 변수로 저장
        self.age = age
    
    def info(self, extrainfo=None):
        """
        Print the person's name, age, and etc

        If the parameter extrainfo is passed, then it is appended to ...

        Parameters
        ----------
            name : str
                More info to be written (Default is None)

        Returns
        ----------
        None 
        """

        print(f'내 이름은 {self.name}. 내 나이는 {self.age}임.' + str(extrainfo))

if __name__ == "__main__":
    human1 = Person("Evan", age = 20)
    human1.info("나의 직장은 휴먼")
    print(Person.__doc__)
    help(Person)
