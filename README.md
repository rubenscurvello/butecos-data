# butecos-data

Dados do app **Butecos Próximos** — gerados automaticamente pelo scraper, organizados por cidade.

## Estrutura

```
butecos-data/
  {cidade_slug}/
    {ano}/
      dados/
        butecos.json          ← dados completos em JSON (carregado pelo app)
        butecos.csv           ← mesmo conteúdo em CSV
        geocode-pendente.csv  ← butecos sem coordenadas (se houver)
      fotos/
        {bar}_{prato}.jpg     ← foto do prato de cada buteco
  privacy-policy.html         ← política de privacidade (GitHub Pages)
  server.py                   ← servidor HTTP local para desenvolvimento
```

## Cidades disponíveis

| Cidade | Slug | Butecos |
|---|---|---|
| Belo Horizonte | `belo-horizonte` | 127 |
| Rio de Janeiro | `rio-de-janeiro` | 105 |

## Servir localmente (desenvolvimento)

Inicia um servidor HTTP com CORS para que o app web consiga carregar fotos e dados:

```bash
python3 server.py
# Acesse em http://localhost:8888
```

## Atualização dos dados

Os dados são gerados pelo scraper (`../scraper/`) e publicados neste repositório.
O app verifica o SHA do último commit por cidade para detectar atualizações e baixar os dados automaticamente.

Para geocodificar coords ausentes e publicar após editar manualmente:

```bash
# No diretório scraper/
CIDADE_SLUG=belo-horizonte npm run geocode   # geocodifica coords ausentes
npm run push                                  # publica no GitHub
```

## Campos do JSON / CSV

| Campo | Descrição |
|---|---|
| `id` | ID sequencial dentro da cidade |
| `slug` | Identificador único (vem da URL do site) |
| `nome` | Nome do buteco |
| `endereco` | Endereço completo |
| `bairro` | Bairro |
| `cidade` | Nome da cidade |
| `cidade_slug` | Slug da cidade (usado para carregar fotos e dados) |
| `ano` | Ano do concurso |
| `lat` / `lng` | Coordenadas geográficas |
| `telefone` | Telefone de contato |
| `horarios` | Dias e horários separados por ` \| ` |
| `fotos` | Nomes dos arquivos separados por `\|` (CSV) ou array (JSON) |
| `pratos` | JSON com `nome`, `descricao` e `foto` |
| `url` | URL da página no site oficial |

## Política de privacidade

Disponível em: `https://rubenscurvello.github.io/butecos-data/privacy-policy.html`
