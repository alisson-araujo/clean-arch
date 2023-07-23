from src.presentation.http_types.http_reponse import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


class UserFinderController(ControllerInterface):
    def __init__(self, use_case: UserFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.query_params["first_name"]

        response = self.__use_case.find(username)

        return HttpResponse(status_code=200, body={"data": response})
