from typing import Tuple

from sqlalchemy.orm import Session

from company import Company
from employee import Employee
from address import Address
from session import engine


def main():
    acme_co = Company(name='ACME Company')
    widget_group = Company(name='Widget Group')

    print('INFO: creating objects')
    with Session(engine) as session:
        beth = Employee(name='Beth',
                        company=acme_co,
                        addresses=[Address(name='42 Bean Street')])
        carl = Employee(name='Carl',
                        company=widget_group,
                        addresses=[Address(name='123 Liberty Lane'),
                                   Address(name='1 Fish Drive')])
        maggie = Employee(name='Maggie',
                          company=acme_co,
                          addresses=[])
        session.add_all([beth, carl, maggie])
        session.commit()

    print('INFO: checking what I have')
    with Session(engine) as session:
        print(f'there are {session.query(Company).count()} companies')
        print(f'there are {session.query(Employee).count()} users')
        print(f'there are {session.query(Address).count()} addresses')
        addresses: list[Tuple[str]] = session.query(Address.name).join(Employee).filter(Employee.name == 'Carl')
        address_names: list[str] = list(map(lambda address: address[0], addresses))
        print(f'Addresses for Carl: {address_names}')
        session.delete(carl)
        print('deleted Carl')
        print(f'there are {session.query(Company).count()} companies')
        print(f'there are {session.query(Employee).count()} users')
        print(f'there are {session.query(Address).count()} addresses')


if __name__ == '__main__':
    main()
