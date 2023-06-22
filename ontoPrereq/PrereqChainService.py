from owlready2 import *


class PrereqChainService:
    def __init__(self):
        self.onto_url = 'https://raw.githubusercontent.com/APGDiamond/ShakirovAA_diplom/main/ontology/ontomathedu.rdf'
        self.onto = get_ontology(self.onto_url).load()
        self.chain = []

    def get_prereq_name(self, iri):
        if len(iri.hasPrerequisite) == 0:
            if len(iri.hasPrerequisiteRu) == 0:
                return None
            else:
                return iri.hasPrerequisiteRu[0]
        else:
            return iri.hasPrerequisite[0]

    def chain_add(self, name):
        self.chain.append(name)
        return

    def search_label(self, name):
        iri = self.onto.search_one(label=name)
        return iri

    def print_chain(self):
        res = ""
        for i in range(len(self.chain)):
            res += self.chain[i]
            if i != len(self.chain) - 1:
                res += " → "
        print(res)
        return

    def search_education_level(self, iri):
        try:
            level = iri.belongsToEducationalLevel[0]
        except IndexError:
            level = None
        return level
    def chain_build(self, name):
        if name is None:
            return
        a = self.search_label(name)
        if a is not None:
            try:
                x = str(self.search_education_level(a).label[1])
            except AttributeError:
                x = 'Данные об уровне отсутствуют'
            self.chain_add(name + ' (' + x + ')')
        else:
            print("В онтологии отсутствует данный концепт")
            return
        prereq = self.get_prereq_name(a)
        self.chain_build(prereq)

    def prereq_count(self):
        onto_results = self.onto.search(hasPrerequisite='*')
        return len(onto_results)


