#!/usr/bin/env python
# encoding= utf-8
#maintainer : alou

from datetime import datetime
from model import  ContactGroup, Operator, PhoneNumber, Contact, Transfer

list_ = []
group1 = ContactGroup(name=u"LIONS").save()
group2 = ContactGroup(name=u"LEO").save()

group1 = ContactGroup.get(id=1)
group2 = ContactGroup.get(id=2)

operator_o = Operator(id_='orange', name='Orange').save()
operator_m = Operator(id_='malitel', name='Malitel').save()

operator_o = Operator.get(id=1)
operator_m = Operator.get(id=2)

phone_o = PhoneNumber(number=76499055, operator=operator_o).save()
phone_m = PhoneNumber(number=69500451, operator=operator_m).save()

phone_o = PhoneNumber.get(id=1)
phone_m = PhoneNumber.get(id=2)

contact1 = Contact(name='alou', phone=phone_o, group=group1).save()
contact2 = Contact(name='fad', phone=phone_m, group=group2).save()

contact1 = Contact.get(id=1)
contact2 = Contact.get(id=2)

date1 = datetime(int(2012), int(11), int(21))
date2 = datetime(int(2012), int(1), int(21))

transfer1 = Transfer(amount='1000', contact=contact1,
                     date=date1, number=0).save()
transfer2 = Transfer(amount='1500', contact=contact2,
                     date=date2, number=0).save()


list_ = [group1, group2, operator_o, operator_m, phone_o, phone_m, contact1,
         contact2, transfer1, transfer2]

print list_

