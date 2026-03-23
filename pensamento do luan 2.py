'''
CRUD

Açaiteria

Permitir que o cliente escolha e persionalize seu pedido e pague seu açaí
pelo celular, com opção de entrega ou retirada.
'''

print("\n=== AÇAÍTERIA ===")
print("1. Mais procurados")
print("2. Opções a deriva")
print("3. Montagem do propio pedido")
print("4. Descontos e promoções")
print("5. Entregas (Delivery)")
print("6. Redes socias da empresa")
print("7. preços")
print("8. Opções de pagamento")
print("9. suporte ao cliente")
print("10. feedbeck da loja")
print("0. Sair")
while True:
    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
        print("Mais procurados...")
        print(" Açaí de 1L, Açaí de 300Ml, Açaí de 700Ml ")

    elif escolha == '2':
        print("Opções a deriva")
        print(" Açaí de copo, Marmita de açaí, Barca açaí ")

    elif escolha == '3':
        print("Montagem do propio pedido")
        print(" Escolher tamanho do açaí, Escolher extra, Escolher complementos ")

    elif escolha == '4':
        print("descontos e promoções ")

        print(" Segunda do Açaí 20% de desconto em qualquer tamanho de açaí ")
        print(" Combo Amigos Compre 2 açaís grandes e ganhe 10% de desconto ")
        print("Monte Seu Açaí Na compra de um açaí médio ou grande, ganhe 1 adicional grátis")


    elif escolha == '5':
        print("Entregas (delivery)")
        print(" Ifood, 99, Keeta ")
        print("Entrega gratis para pedidos acima de R$30,00")
        print("local de saida, Rua Amaca 243")

    elif escolha == '6':
        print("Redes sociais da empresa")
        print(" WhatsApp, TikTok, Instagram ")

    elif escolha == '7':
        print("preços")
        print(" Açai de 1L: R$ 12,00")
        print(" Açai de 300ml: R$8,00")
        print(" Açai de 700ml: R$10,00")
   
    elif escolha == '8':
        print("Opções de pagamento")
        print("Pix")
        print("QRCODE")
        print("Cartão de credito/debito")
        print("Dinheiro no final da entrega")

    elif escolha =='9':
        print(" Telefone (11) 1234-5678")
        print(" Suporteaçaiteria@gmail.com")
        print(" Pedido errado")
        print(" Reembolso")
        print(" Duvidas sobre o pedido")

    elif escolha =='10':
        print("Feedback")
        print(" Bom atendimento")
        print(" Pessimo atendimento")
        print(" Atendimento regular")    
        print(" Entrega rapida")
        print(" Entrega atrasada")


    elif escolha == '0':
        print("Saindo do sístema")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")






else:
    print("Opção inválida. Por favor, tente novamente.")

 