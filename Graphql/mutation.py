import strawberry
from service.course import CourseService
from schema import CourseType, CourseInput


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_course(self, course_data: CourseInput) -> CourseType:
        return await CourseService.add_course(course_data)

    @strawberry.mutation
    async def delete_course(self, course_id: int) -> str:
        return await CourseService.delete(course_id)

    @strawberry.mutation
    async def update_course(self, course_id: int, course_data: CourseInput) -> str:
        return await CourseService.update(course_id, course_data)