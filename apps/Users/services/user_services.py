from ...Program.models import Program,ProgramData

class UserService:

    def get_user_programs(self,user) :
        program_count = Program.objects.filter(user=user).count()
        return program_count
    
    

"""
user_view : to filter and count programs and programs data
program_data[] => ProgramData
program[] =>  Program

NB: use preftech_related
"""