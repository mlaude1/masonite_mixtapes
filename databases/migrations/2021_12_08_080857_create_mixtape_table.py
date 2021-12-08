"""CreateMixtapeTable Migration."""

from masoniteorm.migrations import Migration


class CreateMixtapeTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("mixtape") as table:
            table.increments("id")
            table.string("title")
            table.string("verse")
            table.string("audio")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("mixtape")
