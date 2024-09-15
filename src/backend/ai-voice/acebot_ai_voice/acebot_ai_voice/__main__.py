import uvicorn

from acebot_ai_voice.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "acebot_ai_voice.web.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()
