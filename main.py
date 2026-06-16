contatos = []

def adicionar_contato():
    print("\n===== Adicionar Contato =====")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    
    contatos.append(contato)
    
    print(f"\nContato '{nome}' adicionado com sucesso!")

def listar_contatos():
    print("\n===== Lista de Contatos =====")
    
    if not contatos:
        print("Nenhum contato encontrado")
        return
    
    for indice, contato in enumerate(contatos, start=1):
        favorito = "★" if contato["favorito"] else " "
        
        print(
            f"{indice}. [{favorito}] "
            f"Nome: {contato['nome']} | "
            f"Telefone: {contato['telefone']} | "
            f"E-mail: {contato['email']}"
        )
        
def editar_contato():
    print("\n===== Editar Contato =====")
    
    if not contatos:
        print("Nenhum contato encontrado")
        return
    
    listar_contatos()
    
    try:
        indice = int(input("\nDigite o número do contato que deseja editar: ")) - 1
        
        if indice < 0 or indice >= len(contatos):
            print("Contato inválido.")
            return
        
        contato = contatos[indice]
        
        novo_nome = input(f"Novo nome ({contato['nome']}): ")
        if novo_nome:
            contato["nome"] = novo_nome
            
        novo_telefone = input(f"Novo telefone ({contato['telefone']}): ")
        if novo_telefone:
            contato["telefone"] = novo_telefone
            
        novo_email = input(f"Novo e-mail ({contato['email']}): ")
        if novo_email:
            contato["email"] = novo_email
        
        print("\nContato atualizado com sucesso!")
        
    except ValueError:
        print("Digite um número válido.")
        
def favoritar_contato():
    print("\n===== Favoritar/Desfavoritar Contato =====")
    
    if not contatos:
        print("Nenhum contato encontrado")
        return
    
    listar_contatos()
    
    try:
        indice = int(input("\nDigite o número do contato: ")) - 1
        
        if indice < 0 or indice >= len(contatos):
            print("Contato inválido.")
            return
        
        contatos[indice]["favorito"] = not contatos[indice]["favorito"]
        
        if contatos[indice]["favorito"]:
            print(f"\nContato '{contatos[indice]['nome']}' marcado como favorito!")
        else:
            print(f"\nContato '{contatos[indice]['nome']}' removido dos favoritos!")
        
    except ValueError:
        print("Digite um número válido.")

def main():
    while True:
        print("\n===== Agenda de Contatos =====")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Editar contato")
        print("4 - Favoritar/Desfavoritar contato")
        print("5 - Listar contatos favoritos")
        print("6 - Apagar contato")
        print("0 - Sair do Programa")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato()
            
        elif opcao == "2":
            listar_contatos()
            
        elif opcao == "3":
            editar_contato()
            
        elif opcao == "4":
            favoritar_contato()
            
        elif opcao == "5":
            print("\nFunção de listar contatos favoritos em breve...")
            
        elif opcao == "6":
            print("\nFunção de deletar contato em breve...")
            
        elif opcao == "0":
            print("\nEncerrando programa...")
            break
        
        else:
            print("\nOpção inválida. Por favor, tente novamente.")

            
main()