from googletrans.client import Translator

translator = Translator()

languages = {
    'ru': 'Русский',

    'en': 'Англиский',

    'de':  'Немецкий'
}
text = input("ВВедите текст:")
def translator_translate(text, dest='en'):
    result = translator.translate(text, dest=dest)
    return result.text

def detect_language(text):
    detection = translator.detect(text)
    return detection.lang

def simple_translator(text):
    scr_lang = detect_language(text)
    print(f"Язык: {languages.get(scr_lang, scr_lang)}")
    dest_lang = input("Код языка перевода (en, ru, de и т.д.): ")
    result = translator_translate(text, dest=dest_lang)
    print(f"Перевод: {result}")

def safe_translate(text, dest='en'):
    try:
        result = translator.translate(text , dest = dest)
        return result.text
    except ValueError:
        return f"Ошибка: неверный код языка'{dest}'"
    except Exception as e:
        return f"Ошибка перевода:{str(e)}"
good_result = safe_translate("Привет", "en")
bad_result = safe_translate("Привет", "xx")
print(f"Успешно: {good_result}")
print(f"С ошибкой: {bad_result}")
import json

def translate_and_save(text, languages, filename="Перевод.txt"):
    result = {"original": text}
    scr_lang = detect_language(text)
    results["source_language"] = scr_lang
    for lang in languages:
        translated = safe_translated(text, lang)
        results[lang] = translated
    with open(filename, "w", encoding="utf-8") as file:
       file.write(f"Оригинал ({scr_lang}): {text}\n\n")
       for lang, translation in results.items():
            if lang not in ["original", "source_language"]:
                file.write(f"Перевод({lang}): {translation}\n")
    with open(f"{filename}.json", "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)
    return "Переводы сохранены!"


translator_translate(text, dest='en')
detect_language(text)
simple_translator(text)
safe_translate(text, dest='en')
translate_and_save(text, languages, filename="Перевод.txt")

