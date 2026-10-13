def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run E2E browser tests in headed (non-headless) mode.",
    )
