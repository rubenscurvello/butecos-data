# butecos-data

Dados do app **Butecos Próximos** — gerados automaticamente pelo scraper.

## Estrutura

```
butecos.csv              ← dados completos em CSV (fonte do app em produção)
butecos.json             ← mesmo conteúdo em JSON (dev/debug)
fotos/
  2026/
    belo-horizonte/
      {bar}_{prato}.jpg  ← foto do prato de cada buteco
server.py                ← servidor HTTP local com CORS para desenvolvimento
```

## Servir localmente (desenvolvimento)

Inicia um servidor HTTP com CORS para que o app web consiga carregar fotos:

```bash
python3 server.py
```

Acesse em `http://localhost:8888`. O servidor aceita múltiplas conexões simultâneas.

## Atualização dos dados

Os dados são gerados pelo scraper (`../scraper/`) e publicados neste repositório. O app verifica o SHA do último commit para detectar atualizações e baixar o CSV automaticamente.

Para atualizar manualmente após editar o JSON:

```bash
# No diretório scraper/
npm run geocode        # geocodifica coords ausentes
npm run push           # publica no GitHub
```

## Campos do CSV / JSON

| Campo | Descrição |
|---|---|
| `id` | ID sequencial |
| `slug` | Identificador único (vem da URL do site) |
| `nome` | Nome do buteco |
| `endereco` | Endereço completo |
| `bairro` | Bairro |
| `cidade` | Cidade |
| `cidade_slug` | Slug da cidade |
| `ano` | Ano do concurso |
| `lat` / `lng` | Coordenadas geográficas |
| `telefone` | Telefone de contato |
| `horarios` | Dias e horários separados por ` \| ` |
| `fotos` | Nomes dos arquivos separados por `\|` (CSV) ou array (JSON) |
| `pratos` | JSON com `nome`, `descricao` e `foto` |
| `url` | URL da página no site oficial |
