class Person(object):
    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name
    def familyName(self):
        return self.family_name
    def firstName(self):
        return self.first_name
    def __cmp__(self, other):
        return cmp((self.family_name, self.first_name),
                   (other.family_name, other.first_name))
    def __str__(self):
        return '{} {}'.format(self.first_name, self.family_name)
    def say(self,toWhom,something):
        return '{0} {1} says to {2} {3}: {4}'.format(self.first_name, self.family_name,\
                                                toWhom.firstName(),toWhom.familyName(),\
                                                something)
    def sing(self,toWhom,something):
        return self.say(toWhom,something + ' tra la la')

per = Person('foobar', 'frank')
print per.familyName()
print per.say(per,'why are you not in class')


class MITPerson(Person):
    nextIDNum = 0
    def __init__(self, familyName, firstName):
        Person.__init__(self, familyName, firstName)
        self.idNum = MITPerson.nextIDNum
        MITPerson.nextIDNum += 1
    def getIDNum(self):
        return self.idNum
    def __str__(self):
        return 'MIT Person {} {}'.format(self.first_name, self.family_name)
    def __cmp__(self, other):
        return cmp(self.idNum, other.idNum)

p1 = MITPerson('Duan', 'Stefan')
p2 = MITPerson('Wong', 'Mike')
print p1.getIDNum()
print p2.getIDNum()

class UG(MITPerson):
    def __init__(self, familyName, firstName):
        MITPerson.__init__(self, familyName, firstName)
        self.year = None
    def setYear(self, year):
        if year > 5:
            raise OverflowError('too many')
        self.year = year
    def getYear(self):
        return self.year
    def say(self, toWhom, something):
        return MITPerson.say(self, toWhom, 'Excuse me, but ' + something)

ug = UG('Doe', 'Jane')
print ug.familyName()

class Prof(MITPerson):
    def __init__(self,familyName, firstName, rank):
        MITPerson.__init__(self, familyName, firstName)
        self.rank = rank
        self.teaching = {}
    def addTeaching(self,term,subj):
        try:
            self.teaching[term].append(subj)
        except KeyError:
            self.teaching[term] = [subj]
    def getTeaching(self, term):
        try:
            return self.teaching[term]
        except KeyError:
            return None
    def lecture(self, toWhom, something):
        return MITPerson.say(self, toWhom, something + 'as it is ...')
    def say(self,toWhom,something):
        if type(toWhom) == UG:
            return MITPerson.say(self, toWhom, 'I do not understand why you say ' + something )
        elif type(toWhom) == Prof:
            return MITPerson.say(self, toWhom, 'I really liked your paper on ' + something)
        else:
            return MITPerson.say(self, toWhom, something)

me = Prof('Grimpson', 'Eric', 'Full')
guttag = Prof('Guttag', 'John', 'Full')
print me
print guttag
print me.say(ug, 'you are enjoying 6.00')
print me.say(guttag, 'the sky is blue')
print me.say(per, 'Thank you')

class Faculty(object):
    def __init__(self):
        self.names = []
        self.IDs = []
        self.members = []
        self.place = None
    def add(self,who):
        if type(who) != Prof:
            raise TypeError('not a professor')
        if who.getIDNum() in self.IDs:
            raise ValueError('duplicate ID')
        self.names.append(who.familyName())
        self.IDs.append(who.getIDNum())
        self.members.append(who)
    def __iter__(self):
        self.place = 0
        return self
    def next(self):
        if self.place >= len(self.members):
            raise StopIteration
        self.place += 1
        return self.members[self.place - 1]
