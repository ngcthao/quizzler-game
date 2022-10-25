class Question:

    def __init__(self, q_text, q_answer):
        """
        Separates the question data into two parts--the question and it's answer.''
        :param q_text:
        :param q_answer:
        """
        self.text = q_text
        self.answer = q_answer
