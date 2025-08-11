class UF:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parents[root_b] = root_a


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        emailsKV = {}

        for idx, acc in enumerate(accounts):
            name, *emails = acc
            for email in emails:
                if email in emailsKV:
                    uf.union(emailsKV[email], idx)
                emailsKV[email] = idx

        groups = {}
        for email, idx in emailsKV.items():
            group = uf.find(idx)
            groups[group] = groups.get(group, [accounts[group][0]]) + [email]

        return [[name] + sorted(emails) for name, *emails in groups.values()]
