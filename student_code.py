import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        #if fact is a fact
        if isinstance(fact, Fact):
            #see if fact is already in facts list
            for f in self.facts:
                #if fact is already in facts KB then dont add
                if f == fact:
                    return
            self.facts.append(fact)
        print("Asserting {!r}".format(fact))
        """elif fact.name == 'rule':
            #See if that rule is already in rules list
            for r in self.rules:
                #if fact already in rules KB then dont add
                if r == fact:
                    return
            self.rules.append(fact)
            fact.asserted = True;"""
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        
    def kb_ask(self, fact):
        found_bindings = ListOfBindings()
        for f in self.facts:
            matches = match(fact.statement, f.statement)
            if matches != False:
                found_bindings.add_bindings(matches, [f])
        print("Asking {!r}".format(fact))
        if len(found_bindings) == 0: #if not matches found for the fact --> return False
            return False
        else:
            return found_bindings
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
