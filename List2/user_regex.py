import re
def cpf_pattern(cpf):
 pattern = r"^(\d{3}.){2}\d{3}-\d{2}$"
 return bool(re.match(pattern, cpf))

print(cpf_pattern ('007.368.866-94' ))

