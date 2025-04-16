# Amiguinho Macio
## ✅ Casos de Uso

1. **Criar Conta**  
   - Formulário: E-mail, CPF, Senha.  
   - Cadastro na tabela de usuários.

2. **Fazer Login**  
   - Verificação de e-mail e senha.
   - Se válido, manter login com sessão (`session` do Flask).

3. **Excluir Conta**  
   - Remover usuário da tabela.
   - Remover todos as compras ligadas a esse usuário.

4. **Criar Produtos**  
   - Formulário: nome do produto, imagem do produto, preço.

5. **Ver Produtos**  
   - Exibir em cards com capa, nome do produto, imagem do produto e preço.

6. **Cancelar Compra**  
   - Botão de cancelar compra.

## Tabelas: ##

- `usuarios`
  - email (primary key)
  - cpf
  - senha
  - administrador

- `produtos`
  - id (primary key)
  - nome produto
  - imagem (para o arquivo de imagem)
  - descricao
  - preco

- `vendas`
  - id (primary Key)
  - produto id
  - preco
  - pagamento
  - status
  - data e horario do pedido
  - data e horario de entrega
  

