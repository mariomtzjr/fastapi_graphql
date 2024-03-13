import strawberry


@strawberry.type
class CourseType:
    id: int
    name: str
    description: str


@strawberry.input
class CourseInput:
    name: str
    description: str