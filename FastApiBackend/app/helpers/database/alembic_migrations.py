from alembic.config import Config
from alembic import command


class AlembicMigrations:
    def __init__(self, config_path: str) -> None:
        self.alembic_config = Config(config_path)
        self.head = "head"

    def upgrade_to_alembic_head(self):
        command.upgrade(config=self.alembic_config, revision=self.head)
