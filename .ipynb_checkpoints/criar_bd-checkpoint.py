{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0a7ad7ea-a2de-40ed-b658-e0857551e917",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Banco de dados criado e preenchido com respostas padrão!\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "# Conectar ao banco de dados (cria o arquivo se não existir)\n",
    "conn = sqlite3.connect('respostas.db')\n",
    "cursor = conn.cursor()\n",
    "\n",
    "# Criar tabela para armazenar perguntas e respostas\n",
    "cursor.execute('''\n",
    "CREATE TABLE IF NOT EXISTS respostas (\n",
    "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
    "    palavra_chave TEXT UNIQUE,\n",
    "    resposta TEXT\n",
    ")\n",
    "''')\n",
    "\n",
    "# Inserir respostas padrão\n",
    "respostas_padrao = [\n",
    "    (\"preço, valor\", \"O valor dos nossos produtos variam. Consulte nosso site para mais detalhes.\"),\n",
    "    (\"entrega, entregar\", \"O prazo de entrega é de 5 a 7 dias úteis para a maioria das regiões.\"),\n",
    "    (\"garantia, garantias\", \"Todos os produtos possuem garantia de 1 ano contra defeitos de fabricação.\"),\n",
    "    (\"pagamento\", \"Aceitamos cartões de crédito, boleto e Pix.\"),\n",
    "    (\"estoque\", \"Verifique a disponibilidade do produto no nosso site.\"),\n",
    "]\n",
    "\n",
    "# Inserir dados na tabela\n",
    "cursor.executemany(\"INSERT OR IGNORE INTO respostas (palavra_chave, resposta) VALUES (?, ?)\", respostas_padrao)\n",
    "\n",
    "# Salvar e fechar conexão\n",
    "conn.commit()\n",
    "conn.close()\n",
    "\n",
    "\n",
    "print(\"Banco de dados criado e preenchido com respostas padrão!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eff82fc9-8602-4bd0-b348-ed5b87281212",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
