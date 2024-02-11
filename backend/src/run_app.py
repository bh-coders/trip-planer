if __name__ == "__main__":
    import uvicorn

    from src.core.configs import FAST_API_HOST, FAST_API_PORT

    uvicorn.run(
        "src.main:app",
        host=FAST_API_HOST,
        port=FAST_API_PORT,
        log_level="debug",
        reload=True,
    )
