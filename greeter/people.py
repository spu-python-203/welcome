"""
A list of students partipating to the class.
"""
from dataclasses import dataclass
from datetime import date
from typing import Dict, List


@dataclass
class Person:
    """
    A representation of a person.
    """
    name: str
    lastname: str
    date_of_birth: date
    educational_history: List[str]
    skills: Dict[str, str]

    def __repr__(self) -> str:
        return '{}, {}'.format(self.lastname.capitalize(), self.name.capitalize())


def get_metin_senturk() -> Person:
    """
    Information on instructor. 
    """
    return Person(
        name='metin',
        lastname='senturk',
        date_of_birth=date(1989, 9, 6),
        educational_history=['Bilkent University', "Saint Peter's University"],
        skills=dict(python='*****', sql='**')
    )


def get_Aekyung_Lee() -> Person:
    """
    Information on student. 
    """
    return Person(
        name='Aekyung',
        lastname='Lee',
        date_of_birth=date(1993, 8, 30),
        educational_history='University of Texas',
        skills=dict(python='', sql='', laufter='')
    )
