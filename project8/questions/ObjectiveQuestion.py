from .BaseQuestion import BaseQuestion

class ObjectiveQuestion(BaseQuestion):

    def __init__(self, subject, chapter, question):
        super().__init__(subject,chapter,question)
        self.option1 = ""
        self.option2 = ""
        self.option3 = ""
        self.option4 = ""
        self.correct_option  = ""

    def add_option(self, option_num, option_value):
        match option_num :
            case 1:
                self.option1 = option_value
                
            case 2:
                self.option2 = option_value

            case 3:
                self.option3 = option_value if not None else ""
            case 4:
                self.option4 = option_value  if not None else ""

    def add_answser(self,correct_option):
        self.correct_option = correct_option

    def get_answer(self):
        return self.correct_option