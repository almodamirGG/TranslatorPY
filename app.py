from translate import Translator
import translate
data = Translator(from_lang="French",to_lang="English")
res = data.translate("bonjour")
print(res)