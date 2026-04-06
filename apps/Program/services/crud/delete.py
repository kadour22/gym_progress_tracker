from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from ...models import Program

def delete_program(self, program_id) :

    prog = get_object_or_404(
        Program, id = program_id
    )
    prog.delete()
    return Response({"message":"program deleted.."})


