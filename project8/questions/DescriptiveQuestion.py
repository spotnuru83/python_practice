from .BaseQuestion import BaseQuestion

class DescriptiveQuestion(BaseQuestion):

    def __init__(self, subject, chapter, question):
        super().__init__(subject,chapter,question)
        self.descriptive_answer  = ""

    def add_answser(self,answer):
        self.descriptive_answer = answer

    def get_answer(self):
        return self.descriptive_answer        