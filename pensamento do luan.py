'''
CRUD

Açaiteria

Permitir que o cliente escolha, personalize e pague seu açaí pelo celular, 
com opção de entrega ou retirada.
LUAN
'''

print("\n=== AÇAÍTERIA ===")
print("1. Mais procurados")
print("2. Opções a deriva")
print("3. Montagem do proprio pedido")
print("4. Descontos e promoções")
print("5. Entregas (delivery)")
print("6. Redes sociais da empresa (meio de contato)")
print("0. Sair")




while True: 
    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
        print("Mais procurados...")
        # Código para mais procurados 
    
    elif escolha == '2':
        print("Opções a deriva")
    elif escolha == '3':
        print("Montagem do proprio pedido")
    elif escolha == '4':
        print("Descontos e promoções")
    elif escolha == '5':
        print("Entregas e delivery")
    elif escolha == '6': 
        print("Redes sociais da empresa")
    elif escolha == '0': 
        print("Saindo do sistema")
    elif escolha == '0':
        print ("Saindo do sistemas. Até logo!")
        break




else: 
    print( "Opção invalida. Por favor, tente novamente.")