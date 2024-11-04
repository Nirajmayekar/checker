# from textblob import TextBlob
# # from gingerit.gingerit import GingerIt
# import language_tool_python

# class SpellCheckerModule:
#     def __init__(self):
#         self.spell_check = TextBlob("")
#         # self.grammar_check = GingerIt()
#         self.grammar_check = language_tool_python.LanguageTool('en-US')  # Specify the language
#     def correct_spell(self,text):
#         # Helo,World, subscribe, to my channel
#         words = text.split()
#         corrected_words = []
#         for word in words:
#             corrected_word = str(TextBlob(word).correct())
#             corrected_words.append(corrected_word)
#         return " ".join(corrected_words)

#     def correct_grammar(self,text):
#         matches = self.grammar_check.parse(text)

#         foundmistakes = []
#         for error in matches['corrections']:
#             foundmistakes.append(error['text'])
#         foundmistakes_count = len(foundmistakes)
#         return foundmistakes,foundmistakes_count


# if __name__  == "__main__":
#     obj = SpellCheckerModule()
#     message = "Hello world. I like mashine learning. appple. bananana"
#     print(obj.correct_spell(message))
#     print(obj.correct_grammar(message))
# from textblob import TextBlob
# # from  language_tool_python 
# import language_tool_python 
# # from language_tool_python import LanguageTool
# import spacy
# nlp = spacy.load("en_core_web_sm")

# from gramformer import Gramformer

# class SpellCheckerModule:
#     def __init__(self):
#         self.spell_check = TextBlob("")
#         self.grammar_check = language_tool_python.LanguageTool('en-US')  # Specify the language
 
#     def correct_spell(self, text):
#         words = text.split()
#         corrected_words = []
#         for word in words:
#             corrected_word = str(TextBlob(word).correct())
#             corrected_words.append(corrected_word)
#         return " ".join(corrected_words)

#     def correct_grammar(self, text):
#         matches = self.grammar_check.check(text)
     
#         foundmistakes = []
#         for match in matches:
#             foundmistakes.append(match.matchedText)
#         foundmistakes_count = len(foundmistakes)
     
#         return foundmistakes, foundmistakes_count

# if __name__ == "__main__":
#     obj = SpellCheckerModule()
#     message = "Hello world. I like mashine learning. appple. bananana"
#     print("Corrected Spelling:", obj.correct_spell(message))
#     print("Grammar Mistakes:", obj.correct_grammar(message))



from textblob import TextBlob
import language_tool_python

from language_tool_python import LanguageTool
from gramformer import Gramformer

class SpellCheckerModule:
    def __init__(self):
        self.spell_checker = TextBlob("")
        self.grammar_tool = language_tool_python.LanguageTool('en-US')  # Specify the language
        self.gramformer = Gramformer()  # Initialize Gramformer

    def correct_spell(self, text):
        # Spell checking using TextBlob
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    # def correct_grammar(self, text):
    #     # Grammar checking using Gramformer
    #     corrected_text = self.gramformer.correct(text)
    #     return corrected_text

    def correct_grammar(self, text):
    # Grammar checking using Gramformer
        corrected_text = self.gramformer.correct(text)
        return corrected_text  # Return just the corrected text


    def check_language_tool(self, text):
        # Additional grammar checking using LanguageTool
        matches = self.grammar_tool.check(text)
        found_mistakes = []
        for match in matches:
            found_mistakes.append(match.context)
        found_mistakes_count = len(found_mistakes)
        return found_mistakes, found_mistakes_count

# if __name__ == "__main__":
#     obj = SpellCheckerModule()
#     message = "Hello world. I like mashine learning. appple. bananana"
    
#     # Correct spelling
#     corrected_spelling = obj.correct_spell(message)
#     print("Corrected Spelling:", corrected_spelling)
    
#     # Correct grammar using Gramformer
#     corrected_grammar = obj.correct_grammar(message)
#     print("Corrected Grammar with Gramformer:", corrected_grammar)
    
#     # Check grammar using LanguageTool
#     mistakes, mistake_count = obj.check_language_tool(message)
#     print("Grammar Mistakes using LanguageTool:", mistakes)
#     print("Total Grammar Mistakes Count:", mistake_count)

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello world. I like mashine learning. appple. bananana"
    
    # Correct spelling
    corrected_spelling = obj.correct_spell(message)
    print("Corrected Spelling:", corrected_spelling)
    
    # Correct grammar using Gramformer (only one value returned)
    corrected_grammar = obj.correct_grammar(message)
    print("Corrected Grammar with Gramformer:", corrected_grammar)
    
    # Check grammar using LanguageTool
    mistakes, mistake_count = obj.check_language_tool(message)
    print("Grammar Mistakes using LanguageTool:", mistakes)
    print("Total Grammar Mistakes Count:", mistake_count)
