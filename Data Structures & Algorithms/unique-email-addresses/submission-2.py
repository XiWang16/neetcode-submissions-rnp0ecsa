class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # use hash map for constant lookup time
        unique_addresses = defaultdict(list)

        for email in emails:
            # split into local and domain names
            l = email.split('@') # where l[0] is the local name and l[1] the domain name
            local = l[0]
            domain = l[1]


            # process local name
            # check if '+' is present
            split_local = local.split('+')
            if len(split_local) > 1: local = split_local[0] # only keep the part before the "+"

            # remove all '.' 
            local = local.replace('.', '')

            if domain not in unique_addresses[local]: 
                unique_addresses[local].append(domain)

        print(unique_addresses)
        tot_num = 0
        for addr in unique_addresses.keys():
            tot_num += len(unique_addresses[addr])
        
        return tot_num



        