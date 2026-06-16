contatos = []

def adicionar_contato():
    print("\n===== Adicionar Contato =====")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    
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
        
        print(f"{indice}. [{favorito}] Nome: {contato['nome']} Telefone: {contato['telefone']} E-mail: {contato['email']}")

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
            print("\nFunção de editar contato em breve...")
            
        elif opcao == "4":
            print("\nFunção de marcar/desmarcar contatos favoritos em breve...")
            
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