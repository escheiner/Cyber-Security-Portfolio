import re
#(?<date>.*?)EVID(?<vmid>\w+)\s(?<message>.*)$
regex_pattern = r'^([<date>\d\.]+\s+([<something>\w]+)\s+([<ip>\d\.]+)\s+([<port>\d]+)\s+([<ip>\d\.]+)\s+([<port>\d]+)\s+([<outcome>\w]+)\s+([<direction>\w]+)\s+([<version>\w\.]+)([<version>\w\.]+)([<os>\w\.]+))'
filename = "ssh.log"

def regex_and_parse(fromgroup):
    outcomes = {}
    with open(filename,'r') as f:
        line = f.readline().strip()
        while line:
            results = re.search(regex_pattern,line)
            if (results ):
                # This value determines which group to tally
                thisgroup = results.group(fromgroup)
                if thisgroup in outcomes.keys():
                    outcomes[thisgroup] += 1
                else:
                    outcomes[thisgroup] = 1
            line = f.readline()

    return sorted(outcomes.items(),key=lambda x: x[1],reverse=True)
#out_sorted = regex_and_parse(7)

if __name__ == '__main__':
    print("Most frequent IP address:\t", regex_and_parse(3)[0][0])
    print("Failure / Success Rate")
    for k,v in regex_and_parse(7):
        print(k, ":\t", v) 
    print("Inbound Rate")
    for k,v in regex_and_parse(8):
        print(k, ":\t", v)   
