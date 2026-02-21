# LikelyChat

## Установка

Зависимости:
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [direnv](https://direnv.net/docs/installation.html) (потом придётся хукнуть, гайд [тут](https://direnv.net/docs/hook.html))
- [just](https://github.com/casey/just?tab=readme-ov-file#installation)
- [Docker](https://docs.docker.com/engine/install/)

```bash
# разрешить direnv (подтянет COMPOSE_FILE и прочие env)
direnv allow .

# синкануть зависимости — нужно для lsp и локального запуска без докера
uv sync

# скопировать конфиг и подставить актуальные значения
cp ./config/example.config.toml ./config/config.toml
```

## Запуск

**Локально**
```bash
just run
```

**Docker**
```bash
docker compose up
```