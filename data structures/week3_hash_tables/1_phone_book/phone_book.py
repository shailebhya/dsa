# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    # return [Query(input().split()) for _ in range(n)]
    return [input().split() for _ in range(n)]


def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


def phone_book_manage(queries):
    phone_nos={}
    for query in queries:
        if query[0] == "add":
            phone_nos[query[1]]=query[2]
        elif query[0] == "del":
            # if  query[1] in phone_nos.keys():operation are same O(1) uses hashes 
                # del phone_nos[query[1]]
            phone_nos.pop(query[1],None)
            # else:
            #     print( "not found")
        elif query[0] == "find":
            if  query[1] in phone_nos.keys():
                print( phone_nos[query[1]])
            else:
                print( "not found")                
        else:
            print( "operation not supported")

if __name__ == '__main__':
    # write_responses(process_queries(read_queries()))
    phone_book_manage(read_queries())

