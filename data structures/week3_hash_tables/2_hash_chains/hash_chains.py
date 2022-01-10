# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())



def hash_func(s):
        ans = 0
        for c in reversed(s):
            ans = (ans * 263 + ord(c)) % 1000000007
        return ans % bucket_count

def hashChains(queries):
    hashChain = {}
    for query in queries:
        if query[0]=='add':
            if hash_func(query[1]) not in hashChain.keys():
                hashChain[hash_func(query[1])]=[query[1]]
            else:
                if query[1] not in hashChain[hash_func(query[1])]:
                    hashChain[hash_func(query[1])].insert(0,query[1])
            
        elif query[0]=="del":
            if hash_func(query[1]) not in hashChain.keys():
                pass
            else:
                if query[1]  in hashChain[hash_func(query[1])]:
                    hashChain[hash_func(query[1])].remove(query[1])

        elif query[0]=="find":
            if hash_func(query[1]) not in hashChain.keys():
                print("no")
            else:
                if query[1]  in hashChain[hash_func(query[1])]:
                    print("yes")
                else:
                    print("no")
        elif query[0]=="check":
            if int(query[1]) not in hashChain.keys():
                print("")
            else:   
                if len(hashChain[int(query[1])]) ==0:
                    print("")
                    
                # print(hashChain[hash_func(query[1])])
                else:
                    rhashChain = hashChain[int(query[1])]
                    # rhashChain.reverse()
                    print(' '.join(rhashChain))

if __name__ == '__main__':
    bucket_count = int(input())
    # proc = QueryProcessor(bucket_count)
    # proc.process_queries()
    m = int(input())
    hashChains([input().split() for _ in range(m)])
