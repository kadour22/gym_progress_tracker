from ...serializers import ProgramDataSerializer, ProgramDataSerializer
from ...models import Program, ProgramData

class ProgramDataService:

    def list_all_program_data(self,user) :

        prog_data = ProgramData.objects.filter(program__user = user).order_by('-createdAt')
        serializer = ProgramDataSerializer(prog_data,many=True)

        return ({
            "data":serializer.data,
        })