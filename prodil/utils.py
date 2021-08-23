class ResourceChoices:
    BOOK = "BK"
    DOCUMENT = "DC"
    LINK = "LN"

    TURKISH = "TR"
    ENGLISH = "EN"

    BEGINNER = "BGN"
    EXPERIENCED = "EXP"
    PROFESSIONAL = "PRO"

    @classmethod
    def get_level_choice(cls):
        return (
            (cls.BEGINNER, "Beginner"),
            (cls.EXPERIENCED, "Experinced"),
            (cls.PROFESSIONAL, "Professional"),
        )

    @classmethod
    def get_resource_choice(cls):
        return (
            (cls.BOOK, "Book"),
            (cls.DOCUMENT, "Document"),
            (cls.LINK, "Link"),
        )

    @classmethod
    def get_local_choice(cls):
        return (
            (cls.TURKISH, "Turkish"),
            (cls.ENGLISH, "English"),
        )
