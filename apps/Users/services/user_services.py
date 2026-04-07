from ...Program.models import Program,ProgramData

class UserService:

    def get_user_programs(self,user) :
        program_count = Program.objects.filter(user=user).count()
        return program_count
    
    def get_user_program_data(self,user) :
        program_data = ProgramData.objects.filter(user=user)
        return program_data

