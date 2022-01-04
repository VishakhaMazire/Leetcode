class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output_set = set()
        for email in emails:
            at_index = email.index("@")
            first_part_email = email[:at_index]
            second_part_email = email[at_index:]
            if "." in first_part_email:
                first_part_email = first_part_email.replace('.','')
            if "+" in first_part_email:
                plus_index = first_part_email.index("+")
                first_part_email = first_part_email[:plus_index]
            output_set.add(first_part_email+second_part_email)
        return len(output_set)