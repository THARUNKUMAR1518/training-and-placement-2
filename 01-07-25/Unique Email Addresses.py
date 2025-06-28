class Solution:
    def numUniqueEmails(self, emails):
        expression, emails_set = r'([a-z0-9.]+)\+?.*@(\S+)', set()
        
        for email in emails:
            matches = re.findall(expression, email)
            email = re.sub(r'\.', '', matches[0][0]) + '@' + matches[0][1]
            emails_set.add(email)

        return len(emails_set)
