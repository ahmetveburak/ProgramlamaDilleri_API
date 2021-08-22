class ResourceChoices:
    BOOK = "BK"
    DOCUMENT = "DC"
    LINK = "LN"
    RESOURCE_CHOICE = ((BOOK, "Book"), (DOCUMENT, "Document"), (LINK, "Link"))

    TURKISH = "TR"
    ENGLISH = "EN"
    LOCAL_CHOICE = ((TURKISH, "Turkish"), (ENGLISH, "English"))

    BEGINNER = "BGN"
    EXPERIENCED = "EXP"
    PROFESSIONAL = "PRO"
    LEVEL_CHOICE = (
        (BEGINNER, "Beginner"),
        (EXPERIENCED, "Experinced"),
        (PROFESSIONAL, "Professional"),
    )
