class PropositionalLogic:
    def __init__(self):
        self.clauses = []

    def add_clause(self, clause):
        self.clauses.append(clause)

    def pl_resolution(self):
        while True:
            new = set()

            n = len(self.clauses)

            pairs = [
                (self.clauses[i], self.clauses[j])
                for i in range(n)
                for j in range(i + 1, n)
            ]

            for ci, cj in pairs:
                resolvents = self.pl_resolve(ci, cj)

                for res in resolvents:
                    if len(res) == 0:
                        return False

                    new.add(tuple(sorted(res)))

            if new.issubset(set(map(tuple, self.clauses))):
                return True

            for clause in new:
                clause = list(clause)

                if clause not in self.clauses:
                    self.clauses.append(clause)

    def pl_resolve(self, ci, cj):
        resolvents = []

        for di in ci:
            for dj in cj:
                if di == -dj:

                    resolvent = (
                        list(set(ci) - {di}) +
                        list(set(cj) - {dj})
                    )

                    resolvent = list(set(resolvent))

                    resolvents.append(resolvent)

        return resolvents


pl = PropositionalLogic()

pl.add_clause([1, 2])
pl.add_clause([-1, 3])
pl.add_clause([-2, -3])

is_satisfiable = pl.pl_resolution()

if is_satisfiable:
    print("The knowledge base is satisfiable.")
else:
    print("The knowledge base is not satisfiable.")
