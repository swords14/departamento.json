import json

# Ler os dados dos funcionários a partir do JSON
with open('funcionarios.json', 'r') as f:
    funcionarios_json = json.load(f)

# Ler os dados dos departamentos a partir do JSON
with open('departamentos.json', 'r') as f:
    departamentos_json = json.load(f)

# Criar um dicionário de departamentos com os nomes como chave
departamentos = {}
for departamento in departamentos_json['Departamentos']:
    departamentos[departamento['nome'].lower()] = []

# Adicionar os funcionários a seus respectivos departamentos
for funcionario in funcionarios_json['Funcionarios']:
    departamento = funcionario['departamento'].lower()
    if departamento in departamentos:
        departamentos[departamento].append(funcionario)

# Imprimir a lista de funcionários
print("Lista de funcionários:")
for funcionario in funcionarios_json['Funcionarios']:
    print(f"{funcionario['nome']} ({funcionario['cpf']}) - {funcionario['cargo']}")

# Imprimir a lista de departamentos e seus funcionários
print("\nLista de departamentos e seus funcionários:")
for departamento, funcionarios in departamentos.items():
    print(f"{departamento.title()}:")
    for funcionario in funcionarios:
        print(f"- {funcionario['nome']} ({funcionario['cpf']}) - {funcionario['cargo']}")

# Imprimir informações específicas de um funcionário
cpf = input("\nDigite o CPF do funcionário que deseja consultar: ")
for funcionario in funcionarios_json['Funcionarios']:
    if funcionario['cpf'] == cpf:
        print(f"\nInformações do funcionário {funcionario['nome']} ({funcionario['cpf']}):")
        print(f"Cargo: {funcionario['cargo']}")
        print(f"Salário: R$ {funcionario['salario']:.2f}")
        print(f"Departamento: {funcionario['departamento'].title()}")
        break
else:
    print("Funcionário não encontrado.")

# Imprimir os funcionários de um departamento específico
departamento = input("\nDigite o nome do departamento que deseja consultar: ").lower()
if departamento in departamentos:
    print(f"\nFuncionários do departamento {departamento.title()}:")
    for funcionario in departamentos[departamento]:
        print(f"- {funcionario['nome']} ({funcionario['cpf']}) - {funcionario['cargo']}")
else:
    print("Departamento não encontrado.")