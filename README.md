# butecos-data

Dados do app **Butecos Próximos** — gerados automaticamente pelo [butecos-scraper](https://github.com/rubenscurvello/butecos-scraper).

## Estrutura

```
butecos.csv        ← lista de todos os butecos com coords, horários e pratos
butecos.json       ← mesmo conteúdo em JSON (para debug)
fotos/
  2026/
    belo-horizonte/
      {bar}_{prato}.jpg
```

## Atualização

Os dados são atualizados pelo scraper. O app verifica o SHA do último commit para baixar atualizações automaticamente.
