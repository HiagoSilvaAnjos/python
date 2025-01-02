import os

def menu():
    print("\nEscolha uma opção:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Exibir itens no carrinho")
    print("4 - Aplicar desconto")
    print("5 - Finalizar compra")
    print("6 - Sair")

class Product: 
    def __init__ (self, name, price): 
        self.name = name
        self.price = price

class SupermarketCashier: 
    def __init__ (self):
        self.itens = []
        self.total = 0

    # Methods

    # Adiconar item no caixa
    def add_item(self, product, quantity): 
        self.itens.append((product, quantity))
        self.total += product.price * quantity
        print(f"{quantity}x {product.name} adicionado(s) ao caixa")

    # Remover item no carrinho
    def remove_item(self, name_product, quantity): 

        if not self.itens:
            return print("Caixa vazio...")

        for item, qtd in self.itens:
            if item.name == name_product:
                if quantity >= qtd:
                    self.itens.remove((item, quantity))
                    self.total -= item.price * qtd
                    print(f"{quantity}x {item.name} removido(s) do caixa")
                else:
                    self.total -= item.price * quantity
                    new_quantity = qtd - quantity

                    print(f"Nova quantidade: {new_quantity}")

                    index = self.itens.index((item, qtd))
                    self.itens[index] = (item, new_quantity)
                    print(f"{quantity}x {item.name} removido(s) do caixa")
                return
     
            print(f"Produto {name_product} não encontrado no caixa")

    # Exibir itens do caixa
    def show_itens(self):
        if not self.itens:
            return print("Carrinho Vazio!")
        
        print("Itens no caixa:")
        for item, quantity in self.itens:
            print(f"{quantity}x {item.name} - R${item.price: .2f} cada")
        print(f"Total: R${self.total: .2f}")

    def discount_item(self, desconto):
        if 0 < desconto < 100:
            desconto_valor = self.total * (desconto / 100)
            self.total -= desconto_valor
            print(f"Desconto de {desconto}% aplicado! Total com desconto: R${self.total:.2f}")
        else:
            print("Desconto inválido.")

    def finish(self):
         if not self.itens:
            print("\nNão há itens no carrinho para finalizar a compra!")
         else:
            print("\nCompra finalizada!")
            print(f"Total a pagar: R${self.total:.2f}\n")
            self.itens = []
            self.total = 0

caixa = SupermarketCashier()

while True:
    menu()
    option = input("Digite o número da opção desejada: ")

    if option == '1':
        os.system("clear")
        name = input("Digite o nome do produto: ")
        price = float(input("Digite o preço do produto: "))
        quantity = int(input("Digite a quantidade: "))
        product = Product(name, price)
        caixa.add_item(product, quantity)

    elif option == '2':
        os.system("clear")        
        name = input("Digite o nome do produto a remover: ")
        quantity = int(input("Digite a quantidade a remover: "))
        caixa.remove_item(name, quantity)

    elif option == '3':
        os.system("clear")
        caixa.show_itens()

    elif option == '4':
        os.system("clear")
        discount = float(input("Digite o percentual de desconto (0-100): "))
        caixa.discount_item(discount)

    elif option == '5':
        os.system("clear")
        caixa.finish()

    elif option == '6':
        os.system("clear")
        print("Encerrando o sistema...")
        break

    else:
        os.system("clear")
        print("Opção inválida. Tente novamente.")
